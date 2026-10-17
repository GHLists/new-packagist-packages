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

## Latest list — 2026-10-17 03:20 UTC

New packages created between 2026-10-17 02:22 UTC and 2026-10-17 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T03-20-16-469893Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 02:43:13 | [b4n1/b4n1-web](https://www.nuget.org/packages/b4n1%2Fb4n1-web) | v0.16.0 | Bani Montoya | Ultra-lightweight agentic browser for AI agents - PHP SDK wrapping the b4n1web… |
| 2026-10-17 03:00:58 | [jeavenguitar/web3php](https://www.nuget.org/packages/jeavenguitar%2Fweb3php) | v1.0.0 | jeavenguitar | PHP Ethereum/EVM toolkit in web3.js style: robust JSON-RPC client (multi-endpoi… |
| 2026-10-17 03:13:45 | [evopixel/socialiteproviders-minecraft-evopixel](https://www.nuget.org/packages/evopixel%2Fsocialiteproviders-minecraft-evopixel) | 1.0.0 | EvoPixel | Minecraft EvoPixel OAuth2 provider for Laravel Socialite |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
