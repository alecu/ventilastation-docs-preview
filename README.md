# Ventilastation documentation preview

Review snapshot of [website PR #13](https://github.com/ventilastation/website/pull/13) and [SDK PR #168](https://github.com/ventilastation/vsdk/pull/168).

Published at https://alecu.protocultura.net/ventilastation-docs-preview/ with homepages under `/en/` and `/es/` and documentation under `/docs/`. The root URL chooses Spanish when configured in the browser and otherwise defaults to English. Developer navigation currently points only to the desktop emulator; browser launch links are hidden.

The manual GitHub Actions workflow builds website commit `c904e47e3058c657842e2dd4d8415f242bcacdc4`, whose SDK submodule is `bf1d94a199a59cb4c2545eebc3e493a4ee4a5463`. Technical content stays in the SDK repository. This separate repository contains only preview deployment configuration and does not deploy to the production domain.

Run **Publish review preview** to rebuild the same snapshot. Update the pinned commit deliberately to review a newer version.
