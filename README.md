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

## Latest list — 2026-11-05 15:21 UTC

New packages created between 2026-11-05 14:21 UTC and 2026-11-05 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T15-21-44-780114Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 14:22:25 | [julienbohy/git-profiler-bundle](https://www.nuget.org/packages/julienbohy%2Fgit-profiler-bundle) | 0.3.0 | Julien Bohy | Displays Git information (branch, commit and working state) in the Symfony Web… |
| 2026-11-05 14:24:04 | [browserpilot/browserpilot](https://www.nuget.org/packages/browserpilot%2Fbrowserpilot) | v0.1.0 | Ross Ewing | Give your Laravel agents a browser, with a human on standby. |
| 2026-11-05 14:24:20 | [happenv-com/laravel-model-search](https://www.nuget.org/packages/happenv-com%2Flaravel-model-search) | v0.1.0 |  | Universal record search for Laravel models, backed by PostgreSQL trigram indexe… |
| 2026-11-05 14:37:05 | [rpayvn/rpay-sdk](https://www.nuget.org/packages/rpayvn%2Frpay-sdk) | v1.0.0 |  | Official RPAY Payment & Banking SDK for PHP (Laravel, WordPress, Pure PHP) — Un… |
| 2026-11-05 14:49:47 | [thunder-solution/sdk](https://www.nuget.org/packages/thunder-solution%2Fsdk) | v1.0.0 | Thunder Solution Co., Ltd. | Official Thunder SDK for PHP: verify Thai bank slips and TrueMoney Wallet recei… |
| 2026-11-05 14:50:03 | [intragile/laravel-hungarian-validation](https://www.nuget.org/packages/intragile%2Flaravel-hungarian-validation) | v1.0.1 | IntrAgile Kft. | Validation, normalisation, formatting and test data for Hungarian identifiers:… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
