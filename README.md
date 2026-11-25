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

## Latest list — 2026-11-25 18:20 UTC

New packages created between 2026-11-25 17:20 UTC and 2026-11-25 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T18-20-37-015733Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 17:23:09 | [dmstr/symfony-app-settings-bundle](https://www.nuget.org/packages/dmstr%2Fsymfony-app-settings-bundle) | 0.1.0 | diemeisterei GmbH | Symfony bundle for runtime application settings: sections contributed by the ap… |
| 2026-11-25 17:31:33 | [cohete/skeleton](https://www.nuget.org/packages/cohete%2Fskeleton) | v0.2.0 | Pascual Munoz | Skeleton project for Cohete async PHP framework |
| 2026-11-25 17:32:35 | [serversmtp/serversmtp-symfony-mailer](https://www.nuget.org/packages/serversmtp%2Fserversmtp-symfony-mailer) | v0.1.0 | Think AI SRL | ServerSMTP API transport for Symfony Mailer (Symfony 6/7, Drupal 10/11, Shopwar… |
| 2026-11-25 17:33:08 | [ergebnis/rector-config](https://www.nuget.org/packages/ergebnis%2Frector-config) | 0.1.0 | Andreas Möller | Provides a configuration factory and rule sets for rector/rector. |
| 2026-11-25 17:50:43 | [do-while/contao-manager-blank](https://www.nuget.org/packages/do-while%2Fcontao-manager-blank) | 1.0.0 |  | Öffnet den Menüpunkt 'Contao-Manager' im Contao-Backend in einem neuen Browser-… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
