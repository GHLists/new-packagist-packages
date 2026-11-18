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

## Latest list — 2026-11-18 10:23 UTC

New packages created between 2026-11-18 09:19 UTC and 2026-11-18 10:23 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T10-23-33-999193Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 09:29:09 | [mom/connectors](https://www.nuget.org/packages/mom%2Fconnectors) | v6.3.0 | Darwin Luague | A small SDK for describing the outside accounts a Laravel app connects. |
| 2026-11-18 09:31:57 | [shadrackjm/rampart](https://www.nuget.org/packages/shadrackjm%2Frampart) | v0.1.0 | Shadrack Mballah | Roles & permissions for the Laravel Livewire starter kit. One command, Flux fre… |
| 2026-11-18 09:33:26 | [jeromegxj/castor-api](https://www.nuget.org/packages/jeromegxj%2Fcastor-api) | v0.1.0 | Jérôme Gangneux | Expose Castor tasks marked with #[AsApi] over HTTP |
| 2026-11-18 09:33:33 | [mulertech/alerting-bundle](https://www.nuget.org/packages/mulertech%2Falerting-bundle) | v1.0.0 | Sébastien Muler | Symfony bundle reporting whatever malfunctions in an application, over channels… |
| 2026-11-18 09:47:41 | [adachsoft/ai-model-list-tool](https://www.nuget.org/packages/adachsoft%2Fai-model-list-tool) | v0.1.0 | Arkadiusz Adach | An ai-tool-call tool for listing AI providers, models, and optional pricing met… |
| 2026-11-18 09:50:46 | [glassjob/job-executor-php](https://www.nuget.org/packages/glassjob%2Fjob-executor-php) | v0.4.0 |  | GlassJob PHP SDK: Executor (WebSocket protocol 1.1) and Admin HTTP client |
| 2026-11-18 10:03:09 | [reafeicht/prairie](https://www.nuget.org/packages/reafeicht%2Fprairie) | 1.0.1 | Rea Feichtinger | Gorgeous UI components for Livewire powered by daisyUI and Tailwind |
| 2026-11-18 10:19:51 | [charm/composer-pie](https://www.nuget.org/packages/charm%2Fcomposer-pie) | 0.1.0 | Frode Børli | PIE (the PHP Foundation's extension installer), per project: install PHP extens… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
