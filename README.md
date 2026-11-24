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

## Latest list — 2026-11-24 20:19 UTC

New packages created between 2026-11-24 19:20 UTC and 2026-11-24 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T20-19-04-603535Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 19:23:23 | [mrcaspan/flarum2-email-editor](https://www.nuget.org/packages/mrcaspan%2Fflarum2-email-editor) | v1.0.0 | MrCaspan | Edit the subject and wording of every email your Flarum 2.0 forum sends, and st… |
| 2026-11-24 19:37:57 | [wpcerber/wp-cerber](https://www.nuget.org/packages/wpcerber%2Fwp-cerber) | 10.0.0 | Cerber Tech Inc. | Advanced WordPress security plugin featuring a web application firewall (WAF),… |
| 2026-11-24 19:56:09 | [konradmichalik/phpstan-exception-codes](https://www.nuget.org/packages/konradmichalik%2Fphpstan-exception-codes) | 0.1.0 | Konrad Michalik | PHPStan rules for unique, plausible exception codes, as TYPO3 expects them |
| 2026-11-24 19:57:21 | [konradmichalik/phpstan-typo3-dead-code](https://www.nuget.org/packages/konradmichalik%2Fphpstan-typo3-dead-code) | 0.1.0 | Konrad Michalik | TYPO3 entry points for shipmonk/dead-code-detector: DI constructors, route targ… |
| 2026-11-24 20:00:09 | [konradmichalik/ttt-phpstan](https://www.nuget.org/packages/konradmichalik%2Fttt-phpstan) | 0.1.0 | Konrad Michalik | PHPStan rules that point to ttt attributes instead of hand-written test state |
| 2026-11-24 20:08:57 | [eshimischi/vendor-cleanup](https://www.nuget.org/packages/eshimischi%2Fvendor-cleanup) | v2.1.2 | eshimischi | Global CLI tool & Composer plugin to strip tests, docs, and dev files from vend… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
