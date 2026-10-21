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

## Latest list — 2026-10-21 03:19 UTC

New packages created between 2026-10-21 02:19 UTC and 2026-10-21 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T03-19-25-307216Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 02:31:29 | [pd4ml/pd4ml-php](https://www.nuget.org/packages/pd4ml%2Fpd4ml-php) | v1.0.0 | PD4ML | PD4ML for PHP: HTML to PDF, PDF/A, PDF/UA, DOCX, RTF and image conversion (the… |
| 2026-10-21 02:32:11 | [lyyteam/hyperf-graphic-captcha](https://www.nuget.org/packages/lyyteam%2Fhyperf-graphic-captcha) | v1.0.0 |  | Graphic captcha component for Hyperf 3.1+ |
| 2026-10-21 02:50:39 | [contenir-extension/consent](https://www.nuget.org/packages/contenir-extension%2Fconsent) | v0.1.0 |  | The Consent add-on for Contenir CMS: a cookie banner and preferences, regional… |
| 2026-10-21 02:50:39 | [contenir/contenir-consent-laminas-mvc](https://www.nuget.org/packages/contenir%2Fcontenir-consent-laminas-mvc) | v0.1.0 |  | Laminas MVC adapter for contenir/contenir-consent: consent()->head() and consen… |
| 2026-10-21 03:01:25 | [hazelchat/craft-hazelchat](https://www.nuget.org/packages/hazelchat%2Fcraft-hazelchat) | 1.0.0 | Hazelchat | Adds the Hazelchat AI chat agent to Craft sites from one pasted installation co… |
| 2026-10-21 03:01:59 | [hazelchat/contao-hazelchat](https://www.nuget.org/packages/hazelchat%2Fcontao-hazelchat) | 1.0.0 | Hazelchat | Adds the Hazelchat AI chat agent to Contao websites from one pasted installatio… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
