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

## Latest list — 2026-11-13 00:21 UTC

New packages created between 2026-11-12 23:19 UTC and 2026-11-13 00:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T00-21-46-215797Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 23:21:44 | [phil/api-contract](https://www.nuget.org/packages/phil%2Fapi-contract) | 0.1.0-alpha | Philippe Gamache | Both sides of an unversioned HTTP API contract in plain PHP: RFC 9457 problem d… |
| 2026-11-12 23:21:44 | [phil/api-contract-bundle](https://www.nuget.org/packages/phil%2Fapi-contract-bundle) | 0.1.0-alpha | Philippe Gamache | Both sides of an unversioned HTTP API contract for Symfony, on phil/api-contrac… |
| 2026-11-12 23:21:44 | [phil/browser-security-bundle](https://www.nuget.org/packages/phil%2Fbrowser-security-bundle) | 0.1.0-alpha | Philippe Gamache | The protections a Symfony application asks of the browser, adjustable page by p… |
| 2026-11-12 23:21:44 | [phil/calendar-sync](https://www.nuget.org/packages/phil%2Fcalendar-sync) | 0.1.0-alpha | Philippe Gamache | External calendar synchronization: busy times read from iCalendar feeds, CalDAV… |
| 2026-11-12 23:21:44 | [phil/contact](https://www.nuget.org/packages/phil%2Fcontact) | 0.1.0-alpha | Philippe Gamache | Contact cards for PHP: a person or an organisation with a structured name order… |
| 2026-11-12 23:21:44 | [phil/contact-bundle](https://www.nuget.org/packages/phil%2Fcontact-bundle) | 0.1.0-alpha | Philippe Gamache | phil/contact in Symfony: a contact card form with its emails, phone lines, web… |
| 2026-11-12 23:21:44 | [phil/directory-bundle](https://www.nuget.org/packages/phil%2Fdirectory-bundle) | 0.1.0-alpha | Philippe Gamache | A directory for Symfony: listings in genres, each a content of phil/content-bun… |
| 2026-11-12 23:21:44 | [phil/forms-autosave](https://www.nuget.org/packages/phil%2Fforms-autosave) | 0.1.0-alpha | Philippe Gamache | A form's input kept while it is filled, for Symfony: a form option and a Stimul… |
| 2026-11-12 23:21:44 | [phil/legal-notices](https://www.nuget.org/packages/phil%2Flegal-notices) | 0.1.0-alpha | Philippe Gamache | The legal notice and the privacy policy of a site as versioned, localized docum… |
| 2026-11-12 23:21:44 | [phil/media-bundle](https://www.nuget.org/packages/phil%2Fmedia-bundle) | 0.1.0-alpha | Philippe Gamache | A media library for Symfony: files and versions on any Flysystem storage, colle… |
| 2026-11-12 23:21:45 | [phil/content-bundle](https://www.nuget.org/packages/phil%2Fcontent-bundle) | 0.1.0-alpha | Philippe Gamache | Dimensioned content for Symfony and Doctrine: a root and its rows by locale, st… |
| 2026-11-12 23:21:45 | [phil/social-cards](https://www.nuget.org/packages/phil%2Fsocial-cards) | 0.1.0-alpha | Philippe Gamache | Share metadata as values: Open Graph, X and fediverse tags, 1200×630 share card… |
| 2026-11-12 23:21:45 | [phil/social-cards-bundle](https://www.nuget.org/packages/phil%2Fsocial-cards-bundle) | 0.1.0-alpha | Philippe Gamache | phil/social-cards in Symfony: social_meta() for each page, its share card drawn… |
| 2026-11-12 23:21:45 | [phil/structured-data-bundle](https://www.nuget.org/packages/phil%2Fstructured-data-bundle) | 0.1.0-alpha | Philippe Gamache | phil/structured-data in Symfony: the schema.org graph of each request, fed by c… |
| 2026-11-12 23:21:45 | [phil/translation-bundle](https://www.nuget.org/packages/phil%2Ftranslation-bundle) | 0.1.0-alpha | Philippe Gamache | Translation by segments for Symfony: UJO documents cut into segments kept in Do… |
| 2026-11-12 23:34:11 | [se7enxweb/exp_request_shield](https://www.nuget.org/packages/se7enxweb%2Fexp_request_shield) | v0.0.1.0 | 7x; JAC Systeme GmbH (CJW Net… | request-shield for Exponential: a mini web application firewall that decides ev… |
| 2026-11-12 23:47:43 | [arwin009/pohoda-export](https://www.nuget.org/packages/arwin009%2Fpohoda-export) | v1.0.0 |  | Export do POHODA ucetnictvi |
| 2026-11-12 23:58:21 | [a4hmad1/laravel-autotranslate-ai](https://www.nuget.org/packages/a4hmad1%2Flaravel-autotranslate-ai) | v1.0.0 |  | Headless, on-demand translation for explicitly authorized Laravel website conte… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
