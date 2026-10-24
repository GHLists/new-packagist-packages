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

## Latest list — 2026-10-24 01:19 UTC

New packages created between 2026-10-24 00:20 UTC and 2026-10-24 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T01-19-36-909085Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 00:23:21 | [jeffersongoncalves/peek-cli](https://www.nuget.org/packages/jeffersongoncalves%2Fpeek-cli) | v1.0.0 | Jefferson Goncalves | Read-only inspection of remote servers over SSH (ls, cat, tail, grep, ps, df, f… |
| 2026-10-24 00:26:20 | [pulse-app/pulse-php](https://www.nuget.org/packages/pulse-app%2Fpulse-php) | v0.0.1 |  | Cœur commun des paquets PHP de Pulse : rapports, sondes, tâches planifiées, jou… |
| 2026-10-24 00:26:21 | [pulse-app/pulse-laravel](https://www.nuget.org/packages/pulse-app%2Fpulse-laravel) | v0.0.1 |  | Surveillance Pulse pour Laravel : signal de vie, base de données, Redis, files… |
| 2026-10-24 00:26:23 | [pulse-app/pulse-symfony](https://www.nuget.org/packages/pulse-app%2Fpulse-symfony) | v0.0.1 |  | Surveillance Pulse pour Symfony : signal de vie, Doctrine, Redis, Messenger et… |
| 2026-10-24 00:43:43 | [particle-academy/prism-acp](https://www.nuget.org/packages/particle-academy%2Fprism-acp) | v0.1.0-alpha.1 |  | Agent Client Protocol for the signed-in Claude CLI from PHP. Initial Windows pr… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
