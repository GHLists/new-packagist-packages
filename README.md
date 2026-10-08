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

## Latest list — 2026-10-08 19:19 UTC

New packages created between 2026-10-08 18:23 UTC and 2026-10-08 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T19-19-17-266549Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 18:26:51 | [rmb32/barn](https://www.nuget.org/packages/rmb32%2Fbarn) | v1.0.0 | Roger Barnfather | Build a barn: a PHP project with its story map (Barnspec) and its architecture… |
| 2026-10-08 18:26:51 | [rmb32/barn-layout](https://www.nuget.org/packages/rmb32%2Fbarn-layout) | v1.0.0 | Roger Barnfather | Finds a barn (the nearest .barn/barn.json) and says where each tool's files liv… |
| 2026-10-08 18:27:15 | [joetjen/cooper](https://www.nuget.org/packages/joetjen%2Fcooper) | v0.1.0 | Jan Oetjen | Loads CASC config files -- a hierarchical, extensible config language with impo… |
| 2026-10-08 18:34:23 | [joetjen/cooper-config](https://www.nuget.org/packages/joetjen%2Fcooper-config) | v0.1.0 | Jan Oetjen | Loads an application's CASC configuration once, at startup, with joetjen/cooper… |
| 2026-10-08 18:39:03 | [joetjen/cooper-symfony](https://www.nuget.org/packages/joetjen%2Fcooper-symfony) | v0.1.0 | Jan Oetjen | Symfony integration of Cooper: bundle configuration and container parameters fr… |
| 2026-10-08 18:44:12 | [joetjen/cooper-laravel](https://www.nuget.org/packages/joetjen%2Fcooper-laravel) | v0.1.0 | Jan Oetjen | Laravel integration of Cooper: the configuration repository filled from a CASC… |
| 2026-10-08 18:46:07 | [adeildo-jr/http-logs-laravel](https://www.nuget.org/packages/adeildo-jr%2Fhttp-logs-laravel) | v1.0.0 | Adeildo Amorim | Configurable database logging for outgoing Laravel HTTP client requests. |
| 2026-10-08 19:04:05 | [onetracepro/onetrace-magento2](https://www.nuget.org/packages/onetracepro%2Fonetrace-magento2) | v1.0.0 |  | Magento 2 / Adobe Commerce module for the OneTrace.pro customer data platform:… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
