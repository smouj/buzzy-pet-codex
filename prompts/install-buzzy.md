# Copy-ready agent prompt

Copy the following into an agent conversation with the Pets integration available:

```text
Install and activate Buzzy from https://github.com/smouj/buzzy-pet-codex.

First read the repository README, docs/INSTALL.md, docs/FORMAT.md and
THIRD_PARTY_NOTICES.md. This is an existing v1 asset with nine states;
do not generate or modify artwork or claim it has cursor look directions.

Discover the supported Pets tools. If validation, prepare-upload, creation,
selection or listing tools are missing, explain the missing integration
and stop before attempting activation. Do not edit app internals.

List my existing pets first. If an existing Buzzy installation can be
verified against this asset (including a known stable ID and exact asset
hash where available), reuse it. Do not assume that a matching name alone
identifies the same sprite sheet, and do not create a duplicate after a
timeout without checking the result.

Download this exact pinned release file to a local workspace:
https://github.com/smouj/buzzy-pet-codex/releases/download/v1.0.1/buzzy-mascota.png
Verify SHA-256:
425476ee25c31a83597ffc9ba3485ddaa0859a8124067e0787ee34c674ed4143

Validate its absolute local path with validate_pet_spritesheet. Require
valid=true, sprite_version=1, dimensions 1536x1872 and frame counts
[6,8,8,4,5,8,6,6,6]. Show the all-state GIF from the repository before upload.

Call prepare_pet_upload with the exact validated PNG. The host uploads
it automatically; use the returned upload.upload_session_id in create_pet,
with name Buzzy and description "A transparent animated fan adaptation
of the Theme Park World advisor." Retry transient create failures with
the same session/name/description; prepare a new session only when needed.

Persist the resulting stable pet.id in a local installation record,
excluding credentials, upload sessions and signed URLs. Call select_pet
with that ID, require active_pet_id to match, and page through list_pets
until the custom pet appears as active. Report success only after those
checks, or state the precise failure and the completed steps.
```
