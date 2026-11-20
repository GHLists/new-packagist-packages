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

## Latest list — 2026-11-20 08:20 UTC

New packages created between 2026-11-20 07:20 UTC and 2026-11-20 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T08-20-46-590786Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 07:27:26 | [tobycroft/think-queue-lts](https://www.nuget.org/packages/tobycroft%2Fthink-queue-lts) | v1.0.1 | tobycroft | The ThinkPHP Queue Package (LTS), support ThinkPHP 8.1 and PHP 8.5+ |
| 2026-11-20 07:33:18 | [shipmonk/turbocov-phpunit](https://www.nuget.org/packages/shipmonk%2Fturbocov-phpunit) | 0.1.0 |  | PHPUnit code coverage driver for the turbocov extension, which runs covered cod… |
| 2026-11-20 07:38:59 | [shipmonk/turbocov](https://www.nuget.org/packages/shipmonk%2Fturbocov) | 0.1.0 |  | Coverage engine for PHP at near-native speed! 400× less driver overhead than Xd… |
| 2026-11-20 07:41:36 | [speedyindex/client](https://www.nuget.org/packages/speedyindex%2Fclient) | v0.1.0 | SpeedyIndex | PHP client for the SpeedyIndex API: Google, Bing and Yandex index checks, link… |
| 2026-11-20 07:50:06 | [z77/kibot](https://www.nuget.org/packages/z77%2Fkibot) | 2.0.0 | Peter Ruepp | KI-Bot with topic routing: answers questions from hand-maintained sources via t… |
| 2026-11-20 07:50:07 | [z77/module-article](https://www.nuget.org/packages/z77%2Fmodule-article) | 2.0.0 | Peter Ruepp | Z77 Article Module \| article master (product + hidden default variant, price wi… |
| 2026-11-20 07:50:08 | [z77/module-api](https://www.nuget.org/packages/z77%2Fmodule-api) | 2.0.0 | Peter Ruepp | Z77 API Module \| stateless, versioned JSON API gateway: bearer-key auth, rate l… |
| 2026-11-20 07:50:08 | [z77/module-order](https://www.nuget.org/packages/z77%2Fmodule-order) | 2.0.0 | Peter Ruepp | Z77 Order Module \| sales orders (quote and order as one record), statuses as da… |
| 2026-11-20 07:50:08 | [z77/module-receipt](https://www.nuget.org/packages/z77%2Fmodule-receipt) | 2.0.0 | Peter Ruepp | Z77 Receipt Module \| receipt templates as master data, the receipt journal a ph… |
| 2026-11-20 07:50:10 | [z77/module-mandator](https://www.nuget.org/packages/z77%2Fmodule-mandator) | 2.0.0 | Peter Ruepp | Z77 Mandator Module \| the installation's own company (Mandant): letterhead iden… |
| 2026-11-20 07:50:10 | [z77/persistence-doctrine](https://www.nuget.org/packages/z77%2Fpersistence-doctrine) | 2.0.0 | Peter Ruepp | Z77 Doctrine driver \| relational persistence behind the kernel's UnifiedEntityM… |
| 2026-11-20 07:50:12 | [z77/module-mailing](https://www.nuget.org/packages/z77%2Fmodule-mailing) | 2.0.0 | Peter Ruepp | Z77 Mailing Module \| the mail outbox: queued e-mails sent in throttled batches… |
| 2026-11-20 07:50:13 | [z77/module-contact](https://www.nuget.org/packages/z77%2Fmodule-contact) | 2.0.0 | Peter Ruepp | Z77 Contact Module \| one contact (person or organisation) with n typed addresse… |
| 2026-11-20 07:50:13 | [z77/module-debtor](https://www.nuget.org/packages/z77%2Fmodule-debtor) | 2.0.0 | Peter Ruepp | Z77 Debtor Module \| receivables: debtor profile per contact, payment terms, pay… |
| 2026-11-20 07:50:13 | [z77/module-member](https://www.nuget.org/packages/z77%2Fmodule-member) | 2.0.0 | Peter Ruepp | Z77 Member Module \| self-registration with confirmed e-mail (double opt-in), ac… |
| 2026-11-20 07:50:14 | [z77/module-creditor](https://www.nuget.org/packages/z77%2Fmodule-creditor) | 2.0.0 | Peter Ruepp | Z77 Creditor Module \| the supplier as a role of a contact (creditor profile wit… |
| 2026-11-20 07:50:15 | [z77/module-vat](https://www.nuget.org/packages/z77%2Fmodule-vat) | 2.0.0 | Peter Ruepp | Z77 VAT Module \| tax codes with dated rates as managed data, rate resolution by… |
| 2026-11-20 07:50:17 | [z77/module-financial](https://www.nuget.org/packages/z77%2Fmodule-financial) | 2.0.0 | Peter Ruepp | Z77 Financial Module \| double-entry bookkeeping: chart of accounts, fiscal year… |
| 2026-11-20 08:09:30 | [young-dogs/typo3-ai-seo](https://www.nuget.org/packages/young-dogs%2Ftypo3-ai-seo) | 1.0.0 |  | AI-powered SEO status and metadata generator for the TYPO3 Content > Status > P… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
