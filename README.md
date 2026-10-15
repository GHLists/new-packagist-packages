# New Packagist packages

Hourly lists of packages newly created on
[Packagist.org](https://packagist.org/), the default package registry for
[Composer](https://getcomposer.org/). New packages are discovered through
Packagist's [metadata changes feed](
https://packagist.org/metadata/changes.json), which lists every package
updated since a cursor timestamp; because the feed does not distinguish new
packages from updates, each touched package is checked against its p2
metadata, whose earliest version release date decides whether the package was
created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-packagist-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 09:21 UTC

New packages created between 2026-10-15 08:21 UTC and 2026-10-15 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T09-21-43-376221Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 08:22:18 | [asyntai/neos-ai-chatbot](https://www.nuget.org/packages/asyntai%2Fneos-ai-chatbot) | 1.0.0 | Asyntai | Asyntai AI Chatbot for Neos CMS: an AI chat assistant on every page that answer… |
| 2026-10-15 08:33:51 | [asyntai/filament-ai-chatbot](https://www.nuget.org/packages/asyntai%2Ffilament-ai-chatbot) | v1.0.0 | Asyntai | Asyntai AI chatbot for Filament. Adds an AI chat assistant to your Filament pan… |
| 2026-10-15 08:36:48 | [sala/console](https://www.nuget.org/packages/sala%2Fconsole) | 1.0.0 |  | Console commands for Sala Framework (make, migrate, db, serve) |
| 2026-10-15 08:41:26 | [asyntai/thelia-ai-chatbot](https://www.nuget.org/packages/asyntai%2Fthelia-ai-chatbot) | 1.0.0 | Asyntai | Asyntai AI Chatbot for Thelia: an AI chatbot that answers your customers 24/7 f… |
| 2026-10-15 08:43:12 | [iq2i/tailwind-cs-fixer](https://www.nuget.org/packages/iq2i%2Ftailwind-cs-fixer) | 1.0.0 | Loïc Sapone | A tool to automatically sort Tailwind CSS classes in HTML and Twig files |
| 2026-10-15 08:43:13 | [fylgja/props-builder](https://www.nuget.org/packages/fylgja%2Fprops-builder) | v2.3.0 | Fylgja | Effortlessly generate Design Tokens (CSS custom properties) from PHP arrays or… |
| 2026-10-15 09:03:04 | [clesson-de/silverstripe-household-budget](https://www.nuget.org/packages/clesson-de%2Fsilverstripe-household-budget) | 1.0.0 | Kai Feldmaier | Track household income and recurring expenses in Silverstripe. |
| 2026-10-15 09:10:57 | [clesson-de/silverstripe-scheduler](https://www.nuget.org/packages/clesson-de%2Fsilverstripe-scheduler) | 1.0.0 | Kai Feldmaier | Zentralisierter Scheduler für Silverstripe 6 — verwaltet mehrere BuildTasks in… |
| 2026-10-15 09:17:55 | [pollora/assets](https://www.nuget.org/packages/pollora%2Fassets) | v0.1.0 | Amphibee | Scripts, styles and Vite builds for WordPress: enqueue an asset with a fluent A… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
