"""Deterministically export the distributed atlas into frames and GIF previews."""
from __future__ import annotations
import json
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    manifest = json.loads((ROOT / 'pet.json').read_text(encoding='utf-8'))
    with Image.open(ROOT / manifest['spritesheet']['path']) as opened:
        atlas = opened.convert('RGBA')
    preview_dir = ROOT / 'previews'
    preview_dir.mkdir(exist_ok=True)
    all_frames, all_durations = [], []
    contact = Image.new('RGB', (8*192, 9*238), '#edf0f4')
    draw = ImageDraw.Draw(contact)
    by_state = {}
    for state in manifest['states']:
        row = state['row']
        directory = ROOT / 'frames' / state['name']
        directory.mkdir(parents=True, exist_ok=True)
        frames = []
        draw.rectangle((0, row*238, 1536, row*238+29), fill='#17202e')
        draw.text((12, row*238+8), f"{row:02d}  {state['name']}  /  {state['frames']} frames", fill='white')
        for col in range(state['frames']):
            cell = atlas.crop((col*192, row*208, (col+1)*192, (row+1)*208))
            cell.save(directory / f'{col:02d}.png')
            background = Image.new('RGB', cell.size, '#edf0f4')
            background.paste(cell, mask=cell.getchannel('A'))
            contact.paste(background, (col*192, row*238+30))
            label_frame = Image.new('RGB', (288, 256), '#edf0f4')
            label_frame.paste(background, (48, 12))
            ImageDraw.Draw(label_frame).text((16, 234), f"{state['name']} / {col+1:02d}", fill='#17202e')
            all_frames.append(label_frame)
            all_durations.append(state['durations_ms'][col])
            frames.append(cell)
        by_state[state['name']] = frames
        frames[0].save(preview_dir / f"{state['name']}.gif", save_all=True,
            append_images=frames[1:], duration=state['durations_ms'], loop=0, disposal=2, optimize=False)
    contact.save(preview_dir / 'contact-sheet.png')
    all_frames[0].save(preview_dir / 'all-states.gif', save_all=True,
        append_images=all_frames[1:], duration=all_durations, loop=0, disposal=2, optimize=False)
    jump = by_state['idle'] + by_state['jumping'] + by_state['idle']
    times = manifest['states'][0]['durations_ms'] + manifest['states'][4]['durations_ms'] + manifest['states'][0]['durations_ms']
    jump[0].save(preview_dir / 'idle-jump-idle.gif', save_all=True, append_images=jump[1:],
        duration=times, loop=0, disposal=2, optimize=False)
    by_state['idle'][0].save(preview_dir / 'buzzy.png')
    print('Exported 57 PNG frames, 9 state GIFs, all-state GIF, jump transition and contact sheet.')

if __name__ == '__main__':
    main()
