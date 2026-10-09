# Contributing

Thank you for helping improve Buzzy's packaging and documentation. For installation problems, include the app context, whether Pets tools are available, release version and exact validation error. Do not post credentials, pet IDs, signed URLs or private screenshots.

## Development

Use Python 3.10 or newer, install `requirements.txt`, then run:

```sh
python scripts/validate.py
```

The validator checks release integrity. Visual changes additionally require reviewing every animation at native size and validating the exact PNG with the host's Pets tool before uploading it.

## Artwork changes

Preserve the character's construction, transparent background, readable white eyes and attached gloves. Keep shared scale and registration, unclipped poses and the required row counts. `running` means working/thinking; the directional rows handle movement. Never relabel the nine-row v1 sheet as v2 or add blank direction rows.

`scripts/export_previews.py` derives all public frames and GIFs from the distributed atlas. When changing the atlas, regenerate previews, inspect motion and update `pet.json` and `SHA256SUMS`. The existing release's pinned downloader must keep its original checksum; update it only as part of a new versioned release.

## Release checklist

1. Validate the exact PNG with the Pets host and review every state.
2. Export the frames and previews; review the contact sheet and jump transition.
3. Update metadata, checksums, changelog and any pinned version references.
4. Run `python scripts/validate.py` and check GitHub Actions.
5. Create the version tag and release, with the PNG, full ZIP, frame ZIP and release checksums.
6. Test a fresh download through `scripts/download.py`.

Keep user-specific installation records outside Git. The repository's license does not grant rights to the original character or other third-party artwork.
