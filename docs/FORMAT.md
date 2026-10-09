# Sprite format

This release distributes a supported **existing v1** sprite sheet. It contains nine states, not the eleven rows used by v2. It must not be advertised as having directional cursor gaze.

The atlas is RGBA PNG, exactly **1536 × 1872 px**, with eight columns and nine rows. Each cell is **192 × 208 px**. Rows and columns use zero-based indices. Required frames occupy the leftmost cells of each row; all remaining cells are fully transparent.

| Row | State key | Frames | Meaning |
| --- | --- | --- | --- |
| 0 | `idle` | 6 | Resting, subtle breathing and expression changes |
| 1 | `running-right` | 8 | Directional floating movement toward screen-right |
| 2 | `running-left` | 8 | Directional floating movement toward screen-left |
| 3 | `waving` | 4 | Greeting with a glove |
| 4 | `jumping` | 5 | Rise above the resting baseline and return |
| 5 | `failed` | 8 | Failure / disappointment reaction |
| 6 | `waiting` | 6 | Waiting for approval, help or input |
| 7 | `running` | 6 | Working / thinking; the key does not mean locomotion |
| 8 | `review` | 6 | Reviewing or checking completed work |

There are **57 populated frames and 15 empty cells**. `frames/<state>/<index>.png` is an exact crop from the distributed PNG, including transparent padding. Frame order is unchanged during left/right reflection.

## Metadata

`pet.json` is repository metadata, not a host app configuration file. It records the asset path and checksum, release version, layout, frame order and GIF preview timings. Import the PNG through the Pets tools; do not copy this JSON into undocumented application directories.

`SHA256SUMS` records the distributed asset and preview hashes. `scripts/validate.py` verifies those files and their pixel correspondence. It is a distribution check, distinct from the host's Pets validation and from visual review.

The original release PNG passed the host's `validate_pet_spritesheet` tool before being created and selected. Its structural result was `valid: true`, with sprite version 1 and frame counts `[6, 8, 8, 4, 5, 8, 6, 6, 6]`.

## Edge treatment

The final atlas has transparent background, soft alpha edges and no remaining detected magenta chroma fringe in the recorded final validation. Fully transparent pixels have zero RGB values. GIF exports use a limited palette and cannot preserve every soft alpha value; use the PNG as the source of truth.

## Limitations

- No v2 look-direction rows or cursor-gaze animation.
- Appearance and playback timing depend on the host.
- Left movement is a frame-by-frame reflection of the right movement, preserving temporal order.
- The art is a fan adaptation, not an extraction of original game animation assets.
