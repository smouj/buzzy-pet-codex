"""Download the pinned release atlas and verify its SHA-256. Does not activate a pet."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import urllib.request

URL = 'https://github.com/smouj/buzzy-pet-codex/releases/download/v1.0.1/buzzy-mascota.png'
SHA256 = '425476ee25c31a83597ffc9ba3485ddaa0859a8124067e0787ee34c674ed4143'

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('downloads/buzzy-mascota.png'))
    args = parser.parse_args()
    if args.output.exists():
        if hashlib.sha256(args.output.read_bytes()).hexdigest() == SHA256:
            print(f'Already verified: {args.output.resolve()}')
            return
        raise SystemExit('The destination already exists with different content. Choose another --output path.')
    request = urllib.request.Request(URL, headers={'User-Agent': 'buzzy-pet-codex-downloader'})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read(20*1024*1024 + 1)
    if len(data) > 20*1024*1024 or hashlib.sha256(data).hexdigest() != SHA256:
        raise SystemExit('Download failed size or SHA-256 verification; no file was written.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(data)
    print(f'Verified download: {args.output.resolve()}')
    print('To activate it, use a compatible app with the Pets tools and follow docs/INSTALL.md.')

if __name__ == '__main__':
    main()
