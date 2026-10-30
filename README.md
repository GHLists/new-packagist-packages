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

## Latest list — 2026-10-30 23:19 UTC

New packages created between 2026-10-30 22:20 UTC and 2026-10-30 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T23-19-59-719667Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 22:37:37 | [supportmanager/sdk](https://www.nuget.org/packages/supportmanager%2Fsdk) | v0.0.1 |  | PHP client SDK for the SupportManager backend API — authentication, session, an… |
| 2026-10-30 22:44:55 | [hostily/captcha-typo3](https://www.nuget.org/packages/hostily%2Fcaptcha-typo3) | 0.1.1 | hostily | hostily Captcha spam protection for TYPO3 (EXT:form and powermail), captcha.hos… |
| 2026-10-30 22:45:02 | [hostily/contao-captcha](https://www.nuget.org/packages/hostily%2Fcontao-captcha) | 0.1.0 | hostily | hostily Captcha spam protection for Contao: form field for the form generator (… |
| 2026-10-30 22:45:09 | [hostily/craft-captcha](https://www.nuget.org/packages/hostily%2Fcraft-captcha) | 0.1.0 |  | hostily Captcha for Craft CMS: privacy-friendly spam protection (no cookies) fo… |
| 2026-10-30 22:45:16 | [hostily/module-captcha](https://www.nuget.org/packages/hostily%2Fmodule-captcha) | 0.1.0 |  | hostily Captcha as a CAPTCHA type for Magento 2 (storefront forms and checkout) |
| 2026-10-30 23:11:57 | [dravencms/api](https://www.nuget.org/packages/dravencms%2Fapi) | 0.1.0 | Adam Schubert | Modular read-only REST API for DravenCMS, powered by Apitte |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
