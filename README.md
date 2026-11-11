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

## Latest list — 2026-11-11 00:22 UTC

New packages created between 2026-11-10 23:19 UTC and 2026-11-11 00:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T00-22-06-248678Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 23:31:49 | [delgraf/module-passkey-auth-popup](https://www.nuget.org/packages/delgraf%2Fmodule-passkey-auth-popup) | v1.0.0 | Delgraf | Adds passkey (WebAuthn) sign-in to Magento 2's authentication popup, as an add-… |
| 2026-11-10 23:33:39 | [totalcms/starter-hvac](https://www.nuget.org/packages/totalcms%2Fstarter-hvac) | v1.0.0 | Joe Workman | Foxtail Heating & Air: a heating and cooling company's site for Total CMS, with… |
| 2026-11-11 00:00:13 | [n2ns/laravel-stats](https://www.nuget.org/packages/n2ns%2Flaravel-stats) | v0.1.0 | Datafrog LLC | N2N Stats: cookieless, multi-site web analytics for Laravel. Only daily aggrega… |
| 2026-11-11 00:03:55 | [mkrawczyk/configurable-wysiwyg](https://www.nuget.org/packages/mkrawczyk%2Fconfigurable-wysiwyg) | v0.0.1 |  | Backend for Wysiwyg editor that can be configured and can be converted to any f… |
| 2026-11-11 00:05:37 | [delgraf/module-passkey-auth-translations](https://www.nuget.org/packages/delgraf%2Fmodule-passkey-auth-translations) | v1.0.0 | Delgraf | Italian, German, French and Spanish translations for mage-os/module-passkey-aut… |
| 2026-11-11 00:17:44 | [ernestdefoe/spoiler-shield](https://www.nuget.org/packages/ernestdefoe%2Fspoiler-shield) | 1.0.0 | Ernest Defoe | Spoiler Shield: discussions and posts gated to each member's progress through a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
