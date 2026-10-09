"""Verify the distributed v1 atlas, frame pixels, metadata, and checksums."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    manifest = json.loads((ROOT / 'pet.json').read_text(encoding='utf-8'))
    atlas_path = ROOT / manifest['spritesheet']['path']
    digest = hashlib.sha256(atlas_path.read_bytes()).hexdigest()
    assert digest == manifest['spritesheet']['sha256'], 'Atlas checksum mismatch'
    with Image.open(atlas_path) as opened:
        assert opened.format == 'PNG' and opened.mode == 'RGBA', 'Expected an RGBA PNG'
        assert opened.size == (1536, 1872), 'Expected a v1 1536x1872 atlas'
        atlas = opened.copy()
    assert manifest['sprite_version'] == 1
    assert [(s['name'], s['frames']) for s in manifest['states']] == [
        ('idle', 6), ('running-right', 8), ('running-left', 8), ('waving', 4),
        ('jumping', 5), ('failed', 8), ('waiting', 6), ('running', 6), ('review', 6)]
    frames = 0
    for row, state in enumerate(manifest['states']):
        assert state['row'] == row and len(state['durations_ms']) == state['frames']
        paths = sorted((ROOT / 'frames' / state['name']).glob('*.png'))
        assert len(paths) == state['frames'], f"Wrong frame count: {state['name']}"
        for col in range(8):
            cell = atlas.crop((col*192, row*208, (col+1)*192, (row+1)*208))
            if col >= state['frames']:
                assert cell.getbbox() is None, f'Unused cell {row},{col} is not empty'
                continue
            assert cell.getchannel('A').getbbox(), f'Blank cell {row},{col}'
            with Image.open(paths[col]) as exported:
                assert exported.mode == 'RGBA' and exported.size == (192, 208)
                assert exported.tobytes() == cell.tobytes(), f'Frame differs: {paths[col].name}'
            frames += 1
    raw = atlas.tobytes()
    residue = sum(a == 0 and (r or g or b) != 0 for r,g,b,a in zip(raw[0::4], raw[1::4], raw[2::4], raw[3::4]))
    assert residue == 0, 'Hidden color in fully transparent pixels'
    for line in (ROOT / 'SHA256SUMS').read_text().splitlines():
        expected, relative = line.split('  ', 1)
        path = ROOT / relative
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, f'Checksum mismatch: {relative}'
    print(f'PASS: v1 atlas, {frames} exact exported frames, transparent padding, metadata and SHA256SUMS.')
    print('This checks distribution integrity, not animation semantics or future host compatibility.')

if __name__ == '__main__':
    main()
