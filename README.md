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

## Latest list — 2026-11-19 00:22 UTC

New packages created between 2026-11-18 23:19 UTC and 2026-11-19 00:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T00-22-09-867607Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 23:59:51 | [artisan-toolbox/permit](https://www.nuget.org/packages/artisan-toolbox%2Fpermit) | 1.0.0-beta.1 | Allan Mariucci Carvalho | Declare Laravel Gates and manage per-user permissions and roles. |
| 2026-11-19 00:00:22 | [vested-networks/phonemgr-socialite](https://www.nuget.org/packages/vested-networks%2Fphonemgr-socialite) | v0.1.1 | Werner Garcia | Sign in with Phone Manager: a Socialite driver for Phone Manager's OpenID Conne… |
| 2026-11-19 00:00:39 | [dply/laravel](https://www.nuget.org/packages/dply%2Flaravel) | 1.6.0 |  | Run Laravel queues on Cloudflare Queues when your app is deployed as a dply Edg… |
| 2026-11-19 00:01:22 | [0x15f/agent-traffic](https://www.nuget.org/packages/0x15f%2Fagent-traffic) | v0.1.0 | Jake Casto | Tell AI agents, crawlers and bots apart from people. A PHP port of Mintlify age… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
