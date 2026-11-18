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

## Latest list — 2026-11-18 01:20 UTC

New packages created between 2026-11-18 00:20 UTC and 2026-11-18 01:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T01-20-40-559919Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 00:26:37 | [rishadblack/sylloo-pos-core](https://www.nuget.org/packages/rishadblack%2Fsylloo-pos-core) | v1.0.1 | S M Rishad | The shared core of the Sylloo POS tills (PC and Android): the till's models and… |
| 2026-11-18 00:30:09 | [jeffersongoncalves/laravel-us-privacy-opt-out](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-us-privacy-opt-out) | 1.0.0 | Jefferson Gonçalves | Opt-outs of sale, targeted advertising and profiling, and consent for sensitive… |
| 2026-11-18 00:35:42 | [jeffersongoncalves/laravel-us-privacy-requests](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-us-privacy-requests) | 1.0.0 | Jefferson Gonçalves | Consumer requests under the US state privacy laws: access, correct, delete, por… |
| 2026-11-18 00:37:03 | [websvc/yii2-audit](https://www.nuget.org/packages/websvc%2Fyii2-audit) | 1.0.0 | websvcPT | Records ActiveRecord changes and write requests of Yii2 apps in a dedicated aud… |
| 2026-11-18 00:37:27 | [jeffersongoncalves/laravel-us-privacy-notices](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-us-privacy-notices) | 1.0.0 | Jefferson Gonçalves | Privacy notice for the US state privacy laws: processing activities, the disclo… |
| 2026-11-18 00:44:31 | [jeffersongoncalves/laravel-us-privacy-assessments](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-us-privacy-assessments) | 1.0.0 | Jefferson Gonçalves | Data protection assessments under the US state privacy laws: targeted advertisi… |
| 2026-11-18 00:45:44 | [prestashopheaven/build-pitfalls](https://www.nuget.org/packages/prestashopheaven%2Fbuild-pitfalls) | v1.1.0 | George van Engers | The pitfalls index of the Module-Factory: every known pitfall from the Notes of… |
| 2026-11-18 00:49:41 | [jeffersongoncalves/laravel-us-privacy-vendors](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-us-privacy-vendors) | 1.0.0 | Jefferson Gonçalves | Processor register for the US state privacy laws: the contract terms every stat… |
| 2026-11-18 01:11:04 | [jeffersongoncalves/laravel-us-privacy-minors](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-us-privacy-minors) | 1.0.0 | Jefferson Gonçalves | Minors under the US state privacy laws: age assurance, parent or guardian links… |
| 2026-11-18 01:11:40 | [se7enxweb/sevenx_paypal](https://www.nuget.org/packages/se7enxweb%2Fsevenx_paypal) | v1.0.0 | 7x | PayPal Checkout for Exponential: PayPal's current REST APIs (Orders v2, Payment… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
