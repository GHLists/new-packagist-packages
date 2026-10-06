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

## Latest list — 2026-10-06 19:20 UTC

New packages created between 2026-10-06 18:20 UTC and 2026-10-06 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T19-20-31-455204Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 18:25:31 | [sumvee/drupalens](https://www.nuget.org/packages/sumvee%2Fdrupalens) | v0.1.1 | Sumit Vig | A lens on your Drupal site's health: security, support status, and hygiene from… |
| 2026-10-06 18:43:36 | [caiquebispo/focus-nfe](https://www.nuget.org/packages/caiquebispo%2Ffocus-nfe) | v1.0.0 | Caique Bispo | PHP SDK para a API Focus NFe com suporte multi-CNPJ - Emissão de NFe, NFCe, NFS… |
| 2026-10-06 18:50:18 | [arnoldduo2/cast-template-engine](https://www.nuget.org/packages/arnoldduo2%2Fcast-template-engine) | 1.0.0 | arnoldduo2 | CastTemplateEngine: React-style components (tags, props, children, slots) on to… |
| 2026-10-06 18:50:29 | [florentingarnier/spam-protection](https://www.nuget.org/packages/florentingarnier%2Fspam-protection) | v0.1.0 | Florentin Garnier | Invisible CAPTCHA alternative: honeypot, single-use timed tokens, proof of work… |
| 2026-10-06 18:56:25 | [florentingarnier/spam-protection-bundle](https://www.nuget.org/packages/florentingarnier%2Fspam-protection-bundle) | v0.1.0 | Florentin Garnier | Symfony integration of florentingarnier/spam-protection: a form type, its JavaS… |
| 2026-10-06 18:58:19 | [devable/shopware6-sitemap-domain-filter](https://www.nuget.org/packages/devable%2Fshopware6-sitemap-domain-filter) | 7.0.0-rc1 | Jan Matthiesen | Symfony bundle that excludes configured domains from the Shopware 6 sitemap gen… |
| 2026-10-06 19:08:31 | [osintcat/osintcat-php](https://www.nuget.org/packages/osintcat%2Fosintcat-php) | v1.0.0 | OsintCat | Official SDK for the OsintCat API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
