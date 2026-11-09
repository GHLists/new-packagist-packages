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

## Latest list — 2026-11-09 21:21 UTC

New packages created between 2026-11-09 20:21 UTC and 2026-11-09 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T21-21-16-826309Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 20:29:14 | [doska/symfony](https://www.nuget.org/packages/doska%2Fsymfony) | 0.3.2 |  | Dev-only toolbar that turns a clicked element into a Symfony-aware prompt: cont… |
| 2026-11-09 20:36:30 | [agentisend/agent-email-guard](https://www.nuget.org/packages/agentisend%2Fagent-email-guard) | v0.1.0 | AgentiSend | Blast-radius control for agents that send email: budgets, a rate ceiling, loop… |
| 2026-11-09 20:40:00 | [kayiwarahim/relworx](https://www.nuget.org/packages/kayiwarahim%2Frelworx) | v1.0.0 |  | A Laravel package for integrating Relworx mobile money collections, disbursemen… |
| 2026-11-09 20:57:06 | [trianity/laravel-vpos](https://www.nuget.org/packages/trianity%2Flaravel-vpos) | v1.0.0-rc.1 | Istvan Holbok | Payment Gateway for K and H Bank VPOS service |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
