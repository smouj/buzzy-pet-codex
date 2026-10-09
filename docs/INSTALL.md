# Install Buzzy

## Requirements

- An app/account that exposes the Pets integration. The author tested the Pets tools in the desktop environment's ChatGPT Work mode.
- An agent able to download a public file and pass an absolute local path to those tools.
- Support for the existing v1 sprite format. The release is not a v2 upgrade.

The instructions below describe the actual tested tool flow, not a universal Codex configuration setting. Tool namespace prefixes may differ between environments. An ordinary CLI or app without the Pets integration cannot activate this asset simply by cloning the repository.

## Asset and verification

Download [the v1.0.1 PNG](https://github.com/smouj/buzzy-pet-codex/releases/download/v1.0.1/buzzy-mascota.png), or use `python scripts/download.py` after cloning the repository.

Expected SHA-256:

```text
425476ee25c31a83597ffc9ba3485ddaa0859a8124067e0787ee34c674ed4143
```

PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath './downloads/buzzy-mascota.png'
```

macOS / Linux:

```sh
shasum -a 256 downloads/buzzy-mascota.png
```

Use the PNG itself for installation, not a GIF, video, contact sheet or individual frame.

## Agent workflow

1. Discover the available Pets tools. If any required tool is unavailable, explain the missing integration; do not modify app internals or fabricate a configuration key.
2. List existing pets. Reuse a locally recorded stable ID when its ownership and asset identity can be verified. If necessary, inspect the existing asset with the supported download-link tool and compare its hash. Matching the name alone is not proof of an identical installation.
3. Download the pinned sprite PNG and verify its SHA-256. Pass its absolute local path to `validate_pet_spritesheet`. Require `valid: true`, version 1 and dimensions 1536 × 1872.
4. Show the repository's GIF preview, or render a preview from the exact validated PNG, before creating the pet.
5. Call `prepare_pet_upload` with that exact file. The host transfers it automatically. Read `upload.upload_session_id` from the returned metadata.
6. Call `create_pet` with that session, name `Buzzy`, and a short description such as `A transparent animated fan adaptation of the Theme Park World advisor.`
7. Save the returned stable `pet.id` in a local installation record outside this repository. Do not publish the user's ID, upload session or expiring URLs.
8. Call `select_pet` with the stable ID and require the returned `active_pet_id` to match.
9. Page through `list_pets` until that ID appears. Verify its name, custom status and active state before reporting success.

For a transient create failure, retry using the same upload session, name and description. Prepare a new upload only when the previous session has expired or the transfer/finalization failed. Avoid duplicate pets after an ambiguous timeout: verify the result first.

## Common questions

**I cannot see the Pets tools.** Installation through this repository requires them. Ask your agent to identify whether the integration is available in your current app/account. The download helper only retrieves the asset.

**Does Buzzy follow my cursor?** This v1 release does not contain the sixteen directional look poses. Its nine animated states remain usable in a compatible host.

**Do I need a GLB / 3D model?** No. This asset is a 2D transparent sprite sheet.

**Can I change the name?** Yes, the agent can set a different display name at creation. The artwork and layout remain the same.

**How do I turn it off?** In an environment exposing the supported selection tool, ask the agent to call `select_pet` with `pet_id: "default"`, or choose another available pet. Turning it off does not delete the custom pet.

**The app rejects the image.** Keep the original release bytes and recheck the checksum. If the host no longer supports v1, report that limitation rather than relabeling this file as v2 or adding blank direction rows.
