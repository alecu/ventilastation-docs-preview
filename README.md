# Ventilastation documentation preview

Review snapshot of [website PR #14](https://github.com/ventilastation/website/pull/14), which fixes the homepage's initial flash, with the merged SDK documentation and tutorial updates from [PR #168](https://github.com/ventilastation/vsdk/pull/168) and [PR #170](https://github.com/ventilastation/vsdk/pull/170).

Published at https://alecu.protocultura.net/ventilastation-docs-preview/ with homepages under `/en/` and `/es/` and documentation under `/docs/`. The root URL chooses Spanish when configured in the browser and otherwise defaults to English. Developer navigation currently points only to the desktop emulator; browser launch links are hidden.

The manual GitHub Actions workflow builds website commit `c635519f34b806c869026decf25c8d6bec08d20b`, whose SDK submodule is `647670e015da1fe5b7f1cbae869607566a2b3911`. The homepage starts dark and its original fade reveals the background video. Technical content stays in the SDK repository. This separate repository contains only preview deployment configuration and does not deploy to the production domain.

Run **Publish review preview** to rebuild the same snapshot. Update the pinned commit deliberately to review a newer version.
