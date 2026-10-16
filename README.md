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

## Latest list — 2026-10-16 21:18 UTC

New packages created between 2026-10-16 20:21 UTC and 2026-10-16 21:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T21-18-52-047198Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 20:25:12 | [bushcraftcn/ccot](https://www.nuget.org/packages/bushcraftcn%2Fccot) | v0.1.0 | YerenChina | CCOT — China Compliance Operations Toolkit：中国合规运营工具包，为 Flarum 提供手机号认证、运营单页、私人工单… |
| 2026-10-16 20:28:26 | [sendclipper/sendclipper-php](https://www.nuget.org/packages/sendclipper%2Fsendclipper-php) | v0.1.0 | SendClipper | Official PHP SDK for the SendClipper email API: send mail, manage domains, temp… |
| 2026-10-16 20:33:17 | [samuelheer/contao-churchtools-bundle](https://www.nuget.org/packages/samuelheer%2Fcontao-churchtools-bundle) | v0.2.0 | Samuel Heer | ChurchTools-Integration für Contao: Termine samt Flyer und Personen aus ChurchT… |
| 2026-10-16 20:45:09 | [itools/htmlsecuritycheck](https://www.nuget.org/packages/itools%2Fhtmlsecuritycheck) | v1.0.0 | interactivetools.com | Allowlist check for HTML that has to be printed unencoded, such as rich text fr… |
| 2026-10-16 20:46:36 | [arodu/cakelte-tools](https://www.nuget.org/packages/arodu%2Fcakelte-tools) | v1.0.0 |  | CakeLteTools plugin for CakePHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
