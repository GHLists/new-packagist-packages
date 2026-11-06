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

## Latest list — 2026-11-06 15:19 UTC

New packages created between 2026-11-06 14:22 UTC and 2026-11-06 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T15-19-39-061187Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 14:27:52 | [digitalgdn/oauth2-sheepcrm](https://www.nuget.org/packages/digitalgdn%2Foauth2-sheepcrm) | v1.0.0 | DigitalGdn | SheepCRM OAuth 2.0 support for the PHP League's OAuth 2.0 Client |
| 2026-11-06 14:35:35 | [silin/magento-perf-check](https://www.nuget.org/packages/silin%2Fmagento-perf-check) | v0.1.1 | Mykola Silin | Static analysis for Magento 2 and Mage-OS performance and Full Page Cache anti-… |
| 2026-11-06 14:47:13 | [browser-grpc/eventbus-grpc](https://www.nuget.org/packages/browser-grpc%2Feventbus-grpc) | v0.38.0 |  | Event bus over gRPC for PHP: generated grpcdc.events.v1 publish/subscribe clien… |
| 2026-11-06 14:53:56 | [tinvar/framework](https://www.nuget.org/packages/tinvar%2Fframework) | v0.4.0 |  | Tinvar: a PHP 8.5 core with a React Server Components renderer. |
| 2026-11-06 14:53:56 | [tinvar/skeleton](https://www.nuget.org/packages/tinvar%2Fskeleton) | v0.4.0 |  | A new Tinvar application: composer create-project tinvar/skeleton my-app |
| 2026-11-06 14:58:00 | [damconsultants/cmcpro](https://www.nuget.org/packages/damconsultants%2Fcmcpro) | 1.0.0 | DamConsultants | DamConsultants Cmcpro for Magento 2 |
| 2026-11-06 14:58:42 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.20.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-06 14:58:49 | [js199069/agentlock](https://www.nuget.org/packages/js199069%2Fagentlock) | v0.1.0 | js199069 | Catch AI coding agents that weaken tests to make them pass, and lock the tests… |
| 2026-11-06 15:02:33 | [xelqun/panels](https://www.nuget.org/packages/xelqun%2Fpanels) | v0.1.0 | Jay-Are Ocero | PHP-defined admin panels for Laravel, Inertia and Vue, with navigation, authent… |
| 2026-11-06 15:12:55 | [vanilo/snapshot](https://www.nuget.org/packages/vanilo%2Fsnapshot) | 6.1.0 |  | Vanilo Snapshot Module |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
