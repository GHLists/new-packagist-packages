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

## Latest list — 2026-10-21 10:20 UTC

New packages created between 2026-10-21 09:19 UTC and 2026-10-21 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T10-20-46-709957Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 09:19:35 | [firstlightui/nativephp](https://www.nuget.org/packages/firstlightui%2Fnativephp) | v1.0.0-RC1 | Firstlight UI | Native controls for NativePHP, shaped for each platform. |
| 2026-10-21 09:33:42 | [iqual/icms-test-suite](https://www.nuget.org/packages/iqual%2Ficms-test-suite) | 1.6.2-rc.1 |  | ICMS product test suite - PHPUnit/DTT tests asserting the ICMS contract in ever… |
| 2026-10-21 09:47:30 | [plagiarismcheckerx/plagx-cite](https://www.nuget.org/packages/plagiarismcheckerx%2Fplagx-cite) | v0.2.1 | Plagiarism Checker X | Free APA and MLA citation generator and reference checker for PHP: reference li… |
| 2026-10-21 09:55:45 | [gboquizosanchez/phpstan-code-limits](https://www.nuget.org/packages/gboquizosanchez%2Fphpstan-code-limits) | v1.0.1 | Germán Boquizo Sánchez | PHPStan rules that enforce size, layout and expression limits on PHP code |
| 2026-10-21 10:01:58 | [the-firehub-project/application](https://www.nuget.org/packages/the-firehub-project%2Fapplication) | v0.1.0 | Danijel Galić | Application lifecycle management and orchestration runtime for The FireHub Proj… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
