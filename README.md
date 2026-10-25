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

## Latest list — 2026-10-25 16:19 UTC

New packages created between 2026-10-25 15:21 UTC and 2026-10-25 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T16-19-18-531773Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 15:23:03 | [crustum/ai-interaction](https://www.nuget.org/packages/crustum%2Fai-interaction) | 1.0.0 | Evgeny Tomenko | AiInteraction plugin for CakePHP |
| 2026-10-25 15:27:00 | [crustum/ai-tui](https://www.nuget.org/packages/crustum%2Fai-tui) | 1.0.0 | Evgeny Tomenko | AiTui plugin for CakePHP |
| 2026-10-25 15:39:38 | [opendbs/client](https://www.nuget.org/packages/opendbs%2Fclient) | v1.0.1 | OpenDBS Team | Official PHP client for OpenDBS: documents, SQL, aggregation, transactions, clu… |
| 2026-10-25 15:48:37 | [el-schneider/statamic-greenwashing-checker](https://www.nuget.org/packages/el-schneider%2Fstatamic-greenwashing-checker) | v0.1.0 | Jonas List | Checks marketing copy for greenwashing risks under EU rules (EmpCo), with Germa… |
| 2026-10-25 16:15:26 | [ugeek/php-errors](https://www.nuget.org/packages/ugeek%2Fphp-errors) | v1.0.0 | ugeek | 重写PHP错误处理程序，捕获所有PHP运行时错误并支持通过设置日志器将错误日志记录到日志中。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
