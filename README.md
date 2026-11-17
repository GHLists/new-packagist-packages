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

## Latest list — 2026-11-17 22:21 UTC

New packages created between 2026-11-17 21:21 UTC and 2026-11-17 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T22-21-50-397964Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 21:35:43 | [sharpfy/nextapi](https://www.nuget.org/packages/sharpfy%2Fnextapi) | v0.2.0 | Sharpfy | SDK oficial da NextAPI para PHP: CNPJ (inclusive alfanumérico), CEP, sócios e m… |
| 2026-11-17 21:51:46 | [backdrop-dev/template-manager](https://www.nuget.org/packages/backdrop-dev%2Ftemplate-manager) | v1.0.0 | Benjamin Lu | Custom templates for registering custom post templates, it works for any object… |
| 2026-11-17 21:52:20 | [nubo-db/dynoxide](https://www.nuget.org/packages/nubo-db%2Fdynoxide) | v1.7.0 |  | Start a Dynoxide DynamoDB emulator from PHP tests: downloads, verifies and runs… |
| 2026-11-17 22:04:31 | [sirthxalot/symfoniq](https://www.nuget.org/packages/sirthxalot%2Fsymfoniq) | v1.0.0 | Alexander Bösch | A demonstration web application based on the Symfony PHP framework following be… |
| 2026-11-17 22:07:46 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.33.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-17 22:14:41 | [rishadblack/sylloo-app-base](https://www.nuget.org/packages/rishadblack%2Fsylloo-app-base) | v1.0.0 | S M Rishad | The shared base of the Sylloo device apps (Sylloo POS, Sylloo App desktop and m… |
| 2026-11-17 22:14:42 | [rishadblack/sylloo-app-native](https://www.nuget.org/packages/rishadblack%2Fsylloo-app-native) | v0.1.0 | S M Rishad | Sylloo App's phone package: the native faces of the shared screens and the smal… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
