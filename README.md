# Ventilastation documentation preview

Review snapshot of [website PR #13](https://github.com/ventilastation/website/pull/13) and [SDK PR #168](https://github.com/ventilastation/vsdk/pull/168).

Published at https://alecu.protocultura.net/ventilastation-docs-preview/ with homepages under `/en/` and `/es/` and documentation under `/docs/`. The root URL chooses Spanish when configured in the browser and otherwise defaults to English. Developer navigation currently points only to the desktop emulator; browser launch links are hidden.

The manual GitHub Actions workflow builds website commit `ed8baf032306516a9650b800fe0abb293c187ba2`, whose SDK submodule is `4173d494f7412c893b36811f8202ac782f8aaa8e`. Technical content stays in the SDK repository. This separate repository contains only preview deployment configuration and does not deploy to the production domain.

Run **Publish review preview** to rebuild the same snapshot. Update the pinned commit deliberately to review a newer version.
