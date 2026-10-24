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

## Latest list — 2026-10-24 06:19 UTC

New packages created between 2026-10-24 05:20 UTC and 2026-10-24 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T06-19-29-278057Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 05:23:16 | [axitdev/phpunit-ai-evals](https://www.nuget.org/packages/axitdev%2Fphpunit-ai-evals) | v0.0.2 | Oleksii Ivanov | Framework-agnostic AI Evals, LLM-as-a-Judge & Smart VCR for PHPUnit |
| 2026-10-24 05:31:17 | [e9li/kirby-consent](https://www.nuget.org/packages/e9li%2Fkirby-consent) | 0.1.0 | Rafael Egli | Cookie consent banner with script gating and Google Consent Mode v2 for Kirby |
| 2026-10-24 05:56:57 | [xnrcms-package/hyperf-wechat](https://www.nuget.org/packages/xnrcms-package%2Fhyperf-wechat) | 1.2.3 |  | Wechat SDK For Hyperf |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
