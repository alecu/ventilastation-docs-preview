# Ventilastation documentation preview

Review snapshot of [website PR #13](https://github.com/ventilastation/website/pull/13) and [SDK PR #168](https://github.com/ventilastation/vsdk/pull/168).

Published at https://alecu.protocultura.net/ventilastation-docs-preview/ with homepages under `/en/` and `/es/` and documentation under `/docs/`. The root URL chooses Spanish when configured in the browser and otherwise defaults to English. Developer navigation currently points only to the desktop emulator; browser launch links are hidden.

The manual GitHub Actions workflow builds website commit `2a47fc5606a1f720b2c19735b09338dbdd5415b2`, whose SDK submodule is `df5af332e6978fa16d39bbcd4314f26f26696e9e`. Technical content stays in the SDK repository. This separate repository contains only preview deployment configuration and does not deploy to the production domain.

Run **Publish review preview** to rebuild the same snapshot. Update the pinned commit deliberately to review a newer version.
