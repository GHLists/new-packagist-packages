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

## Latest list — 2026-10-13 09:20 UTC

New packages created between 2026-10-13 08:21 UTC and 2026-10-13 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T09-20-01-021234Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 08:27:32 | [jonathandelacruz/yii2-user-management](https://www.nuget.org/packages/jonathandelacruz%2Fyii2-user-management) | v2.0.1 |  | Yii2 user management and RBAC with Bootstrap 5 and PHP 8.2-8.5 |
| 2026-10-13 08:29:59 | [software-technologies-limited/stl-rich-text-editor](https://www.nuget.org/packages/software-technologies-limited%2Fstl-rich-text-editor) | v3.0.0 | Software Technologies Limited… | A standalone, framework-agnostic rich text editor for PHP applications. |
| 2026-10-13 08:31:55 | [plenta/plenta-casa-core-bundle](https://www.nuget.org/packages/plenta%2Fplenta-casa-core-bundle) | 1.0.1 | Plenta.io |  |
| 2026-10-13 08:39:15 | [graystackit/laravel-dymo-printer](https://www.nuget.org/packages/graystackit%2Flaravel-dymo-printer) | v1.2.0 | Graystack | A Laravel package for DYMO LabelWriter integration with Alpine.js and Livewire… |
| 2026-10-13 08:40:49 | [networkrailbusinesssystems/directory-link](https://www.nuget.org/packages/networkrailbusinesssystems%2Fdirectory-link) | 1.2.9 | Anthony Edmonds | Resources for connecting to the Directory system |
| 2026-10-13 08:45:55 | [mmnewmedia/schematron-parser](https://www.nuget.org/packages/mmnewmedia%2Fschematron-parser) | 1.0.0 | Marcel Maaß | XPath expression parser and compiler for Schematron rule files |
| 2026-10-13 08:55:12 | [smpackbuilder/laravel-payammatni-sms](https://www.nuget.org/packages/smpackbuilder%2Flaravel-payammatni-sms) | v1.0.0 | payammatni | Laravel package for sending SMS and checking credit / delivery status through t… |
| 2026-10-13 08:56:52 | [ptadmin/core](https://www.nuget.org/packages/ptadmin%2Fcore) | v0.0.1 | Zane | PTAdmin core package with Admin, Addon, Schema and Core runtime. |
| 2026-10-13 09:08:26 | [cakewire/cakewire](https://www.nuget.org/packages/cakewire%2Fcakewire) | v1.0.0 | arbims | Live server-driven components for CakePHP powered by Alpine.js. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
