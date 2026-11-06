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

## Latest list — 2026-11-06 14:22 UTC

New packages created between 2026-11-06 13:22 UTC and 2026-11-06 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T14-22-05-716052Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 13:25:06 | [aldanux/statamic-polls](https://www.nuget.org/packages/aldanux%2Fstatamic-polls) | v0.1.0 | Aldanux | Simple, reusable polls and voting for Statamic. Options from any collection or… |
| 2026-11-06 13:48:00 | [filagora/filagora-ai](https://www.nuget.org/packages/filagora%2Ffilagora-ai) | v0.1.0 |  | AI chat, usage records and provider plumbing for Filagora applications. |
| 2026-11-06 13:49:28 | [js199069/mutagent](https://www.nuget.org/packages/js199069%2Fmutagent) | v0.1.0 | js199069 | LLM-written PHPUnit tests, strengthened until they kill mutants (Infection), wi… |
| 2026-11-06 13:51:55 | [muno92/asn1-tools](https://www.nuget.org/packages/muno92%2Fasn1-tools) | v0.1.0 | muno92 | ASN.1 reader and writer (BER/DER) for PHP |
| 2026-11-06 13:59:51 | [itw/gatecha](https://www.nuget.org/packages/itw%2Fgatecha) | 14.0.0 |  | GateCHA (self-hosted ALTCHA) spam protection for TYPO3 EXT:form: direct challen… |
| 2026-11-06 14:10:27 | [nelsius/nelsius-pay-laravel](https://www.nuget.org/packages/nelsius%2Fnelsius-pay-laravel) | v2.0.0 | Nelson Siebi | The official Laravel package and Service Provider for Nelsius Pay API V2 |
| 2026-11-06 14:14:45 | [adachsoft/plugin-discovery](https://www.nuget.org/packages/adachsoft%2Fplugin-discovery) | v0.1.0 | Arkadiusz Adach | Discovers plugin declarations from installed Composer packages. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
