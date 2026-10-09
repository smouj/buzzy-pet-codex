"""Build a versioned distribution with checksums; run after reviewing changes."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def public_files() -> list[Path]:
    excluded = {'.git', '.venv', '__pycache__', 'dist', 'downloads'}
    return sorted(path for path in ROOT.rglob('*') if path.is_file()
        and not excluded.intersection(path.relative_to(ROOT).parts)
        and path.name != 'SHA256SUMS' and path.suffix not in {'.pyc', '.pyo'})

def write_zip(target: Path, files: list[Path], prefix: str = '') -> None:
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            info = zipfile.ZipInfo(prefix+path.relative_to(ROOT).as_posix(), (2026,10,9,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())

def main() -> None:
    manifest = json.loads((ROOT / 'pet.json').read_text())
    version = manifest['version']
    files = public_files()
    sums = '\n'.join(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+path.relative_to(ROOT).as_posix() for path in files)+'\n'
    (ROOT / 'SHA256SUMS').write_text(sums,encoding='utf-8',newline='\n')
    subprocess.run([sys.executable,str(ROOT/'scripts/validate.py')],check=True)
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    write_zip(dist/f'buzzy-pet-codex-v{version}.zip', files+[ROOT/'SHA256SUMS'], f'buzzy-pet-codex-v{version}/')
    write_zip(dist/f'buzzy-frames-v{version}.zip', [path for path in files if path.relative_to(ROOT).parts[0]=='frames'])
    assets = [ROOT/'assets/buzzy-mascota.png',dist/f'buzzy-pet-codex-v{version}.zip',dist/f'buzzy-frames-v{version}.zip']
    (dist/'SHA256SUMS').write_text('\n'.join(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+path.name for path in assets)+'\n',encoding='utf-8')
    print(f'Release archives and checksums written to {dist}')

if __name__ == '__main__':
    main()
