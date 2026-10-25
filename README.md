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

## Latest list — 2026-10-25 09:21 UTC

New packages created between 2026-10-25 08:21 UTC and 2026-10-25 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T09-21-32-893095Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 08:34:10 | [rokastudio/racin](https://www.nuget.org/packages/rokastudio%2Fracin) | v1.2.3 | Roka Studio | A small, fast PHP 8.3+ framework for JSON APIs: Rails-style controllers and gen… |
| 2026-10-25 08:41:44 | [blackcube/injector](https://www.nuget.org/packages/blackcube%2Finjector) | 1.0.0 | Philippe Gaultier | Static PSR-11 container accessor — get DI everywhere |
| 2026-10-25 08:45:58 | [astral-php/astral-worker](https://www.nuget.org/packages/astral-php%2Fastral-worker) | 0.1.0 | astral-php | File d'attente et worker pour Astral — mails et PDF en arrière-plan (sync, data… |
| 2026-10-25 08:46:56 | [blackcube/magic-compose](https://www.nuget.org/packages/blackcube%2Fmagic-compose) | 1.0.0 | Philippe Gaultier | Simple solution for magic methods and method composition using attributes |
| 2026-10-25 08:48:56 | [blackcube/html](https://www.nuget.org/packages/blackcube%2Fhtml) | 1.0.0 | Philippe Gaultier | Extensible HTML tags for Yii framework |
| 2026-10-25 08:52:11 | [blackcube/icons](https://www.nuget.org/packages/blackcube%2Ficons) | 1.0.0 | Philippe Gaultier | Icon sets and SVG renderer for Yii framework |
| 2026-10-25 08:53:53 | [blackcube/assets](https://www.nuget.org/packages/blackcube%2Fassets) | 1.0.0 | Philippe Gaultier | Vite and Webpack asset bundles for Yii with scaffolding command |
| 2026-10-25 08:57:54 | [pradosoft/prado-activerecord](https://www.nuget.org/packages/pradosoft%2Fprado-activerecord) | 1.0.0 | Wei Zhuo; Fabio Bas; Brad And… | Active Record ORM and Scaffold controls for the PRADO PHP Framework |
| 2026-10-25 08:57:57 | [blackcube/oauth2](https://www.nuget.org/packages/blackcube%2Foauth2) | 1.0.0 | Philippe Gaultier | OAuth2/JWT toolbox with multi-population support |
| 2026-10-25 08:59:33 | [blackcube/proxy-middleware](https://www.nuget.org/packages/blackcube%2Fproxy-middleware) | 1.0.0 | Philippe Gaultier | Yiisoft TrustedHostsNetworkResolver fork with CIDR support in withTrustedIps() |
| 2026-10-25 09:02:04 | [blackcube/handler](https://www.nuget.org/packages/blackcube%2Fhandler) | 1.0.0 | Philippe Gaultier | PSR-15 handler abstractions and pipeline for Yii3 applications |
| 2026-10-25 09:15:13 | [blackcube/active-record](https://www.nuget.org/packages/blackcube%2Factive-record) | 1.0.0 | Philippe Gaultier | Scoped queries, elastic dynamic attributes, Hazeltree nested sets — a toolkit f… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
