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

## Latest list — 2026-10-30 14:25 UTC

New packages created between 2026-10-30 13:19 UTC and 2026-10-30 14:25 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T14-25-45-051466Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 13:32:41 | [mageenv/module-total-savings-hyva](https://www.nuget.org/packages/mageenv%2Fmodule-total-savings-hyva) | 1.2.0 |  | Hyva storefront integration for MageEnv Total Savings - an Alpine.js Cart Page… |
| 2026-10-30 13:39:44 | [torno/tcrud](https://www.nuget.org/packages/torno%2Ftcrud) | v1.0.1 |  | CRUD virtual para CodeIgniter 4 con Bootstrap 5 |
| 2026-10-30 13:48:15 | [phrosthesis/run-tests](https://www.nuget.org/packages/phrosthesis%2Frun-tests) | v0.1.0 | Alexey Tsarkov | Prosthesis for run-tests.php. |
| 2026-10-30 14:14:07 | [sendora/sendora-laravel](https://www.nuget.org/packages/sendora%2Fsendora-laravel) | v0.1.0 |  | Sendora for Laravel: the API's clients in the container, with a facade, and Lar… |
| 2026-10-30 14:15:23 | [drupal/art_gallery](https://www.nuget.org/packages/drupal%2Fart_gallery) | 1.0.0 |  | A typography-led Drupal CMS site template for artists and galleries: artworks,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
