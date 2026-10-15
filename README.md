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

## Latest list — 2026-10-15 15:20 UTC

New packages created between 2026-10-15 14:21 UTC and 2026-10-15 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T15-20-44-990463Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 14:35:20 | [jslirola/flarum-registration-policy](https://www.nuget.org/packages/jslirola%2Fflarum-registration-policy) | v1.0.0 | jslirola | Do not sign new members in until they confirm their email address. |
| 2026-10-15 14:35:50 | [logipro/snp-php-client](https://www.nuget.org/packages/logipro%2Fsnp-php-client) | v0.1.0 | Frédéric Royet | PHP client for the SocialNetworksPublisher (SNP) external API |
| 2026-10-15 14:57:42 | [netcom/drupal-autoupdate](https://www.nuget.org/packages/netcom%2Fdrupal-autoupdate) | v1.0.0 |  | Mises à jour Composer automatiques (mineures et patchs) pour Drupal 11+, avec r… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
