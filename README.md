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

## Latest list — 2026-11-17 17:22 UTC

New packages created between 2026-11-17 16:20 UTC and 2026-11-17 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T17-22-05-469065Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 16:24:57 | [jeffersongoncalves/laravel-ccpa-breaches](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-breaches) | 1.0.0 | Jefferson Gonçalves | California data breach register for Laravel (Cal. Civ. Code §1798.82): notify r… |
| 2026-11-17 16:25:31 | [jeffersongoncalves/laravel-ccpa-notices](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-notices) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA notices for Laravel: privacy policy (§1798.130(a)(5)) and notice at c… |
| 2026-11-17 16:32:08 | [hostkurd/flocms-frontend](https://www.nuget.org/packages/hostkurd%2Fflocms-frontend) | v0.1.0 | HostKurd | The public side of a FloCMS website: components written once and used in templa… |
| 2026-11-17 16:34:33 | [jeffersongoncalves/laravel-ccpa-vendors](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-vendors) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA vendor register for Laravel: service providers, contractors and third… |
| 2026-11-17 16:35:10 | [jeffersongoncalves/laravel-ccpa-risk-assessments](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-risk-assessments) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA risk assessments for Laravel (CCPA Regulations Article 10): risks sco… |
| 2026-11-17 16:35:44 | [jeffersongoncalves/laravel-ccpa-minors](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-minors) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA minors for Laravel (§1798.120(c)): no sale or sharing of personal inf… |
| 2026-11-17 16:39:02 | [helori/php-sign](https://www.nuget.org/packages/helori%2Fphp-sign) | v1.0 | Helori Lanos | A framework agnostic PHP library to sign PDF documents |
| 2026-11-17 16:42:59 | [webwizardsusa/rich-editor-plus-code](https://www.nuget.org/packages/webwizardsusa%2Frich-editor-plus-code) | v0.1.1 | Jamie Holly | Code blocks for Rich Editor Plus: pick the language, line numbers and highlight… |
| 2026-11-17 16:48:25 | [tohawk89/plan-block](https://www.nuget.org/packages/tohawk89%2Fplan-block) | v0.1.0 | Nazar | Notion-style block system for Laravel: flexible itineraries, backup plans and l… |
| 2026-11-17 17:05:23 | [ricfreire/mautic-theme-runner](https://www.nuget.org/packages/ricfreire%2Fmautic-theme-runner) | v1.0.0 |  | Runner - A free, responsive MJML email theme for Mautic, designed for sports an… |
| 2026-11-17 17:08:04 | [upassist/neos-ui-sidebarcollapse](https://www.nuget.org/packages/upassist%2Fneos-ui-sidebarcollapse) | v1.0.0 |  | Icon-only collapsed sidebar for the Neos CMS backend modules |
| 2026-11-17 17:10:06 | [mateusjunges/coding-style](https://www.nuget.org/packages/mateusjunges%2Fcoding-style) | v0.1.1 | Mateus Junges | Opinionated coding style tooling for Laravel applications |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
