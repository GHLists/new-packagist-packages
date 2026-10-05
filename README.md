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

## Latest list — 2026-10-05 09:19 UTC

New packages created between 2026-10-05 08:21 UTC and 2026-10-05 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T09-19-37-271615Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 08:32:14 | [amirkateb/payment-core-client](https://www.nuget.org/packages/amirkateb%2Fpayment-core-client) | v1.0.0 |  | Secure Laravel client SDK for AvazTek Payment Platform |
| 2026-10-05 08:45:19 | [justpush/prestashop-module-notify](https://www.nuget.org/packages/justpush%2Fprestashop-module-notify) | v1.0.0 | JustPush | Push notifications from PrestaShop through JustPush Studio: orders, payments, r… |
| 2026-10-05 08:46:03 | [cetera-labs/library](https://www.nuget.org/packages/cetera-labs%2Flibrary) | 13.0.0 | Roman Romanov | Сторонние JS-библиотеки старого back-office Fastsite CMS 3.x: ExtJS 4.2, ace, j… |
| 2026-10-05 08:52:09 | [aimeos/ai-admin-mcp](https://www.nuget.org/packages/aimeos%2Fai-admin-mcp) | 2026.10.1 |  | Framework-neutral MCP tools for Aimeos administration |
| 2026-10-05 08:55:02 | [mage2kishan/module-malware-scanner](https://www.nuget.org/packages/mage2kishan%2Fmodule-malware-scanner) | 1.3.7 | Kishan Savaliya | Active malware prevention + on-disk scanner for Magento 2. Three real-time guar… |
| 2026-10-05 08:55:50 | [max-dernovyi/netsuite-php](https://www.nuget.org/packages/max-dernovyi%2Fnetsuite-php) | v2025.2.0 | Ryan Winchester (fungku); Max… | NetSuite PHP API wrapper |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
