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

## Latest list — 2026-10-12 10:21 UTC

New packages created between 2026-10-12 09:23 UTC and 2026-10-12 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T10-21-54-020101Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 09:24:33 | [sdjgroup/mail-proxy-php](https://www.nuget.org/packages/sdjgroup%2Fmail-proxy-php) | v1.0.0 | sdjgroup | Framework-agnostic PHP SDK for the mail proxy service: hand a mail with many re… |
| 2026-10-12 09:26:28 | [gnnpls/wp-kit](https://www.nuget.org/packages/gnnpls%2Fwp-kit) | v0.3.1 | Nikos Giannopoulos | Declare a WordPress feature once and expose it as a REST route, a WP-CLI comman… |
| 2026-10-12 09:28:10 | [echo-fusion/configmanager](https://www.nuget.org/packages/echo-fusion%2Fconfigmanager) | v1.0.0 | Amir Shadanfar | Immutable, deeply merged application configuration with dot-notation access for… |
| 2026-10-12 09:36:01 | [echo-fusion/sessionmanager](https://www.nuget.org/packages/echo-fusion%2Fsessionmanager) | v1.0.0 | Amir Shadanfar | Session handling for the EchoFusion framework: native and in-memory sessions wi… |
| 2026-10-12 09:39:34 | [hyperf-apex/apex](https://www.nuget.org/packages/hyperf-apex%2Fapex) | v0.1.0 | lbg-sys | Apex generic infrastructure, API engine and components for Hyperf (Metapackage) |
| 2026-10-12 09:41:00 | [echo-fusion/responsemanager](https://www.nuget.org/packages/echo-fusion%2Fresponsemanager) | v1.0.0 | Amir Shadanfar | PSR-7 HTML, JSON, XML and redirect response classes for the EchoFusion framewor… |
| 2026-10-12 09:51:18 | [pollora/discovery](https://www.nuget.org/packages/pollora%2Fdiscovery) | v0.1.0 | Amphibee | Find the PHP classes that carry attributes in themes, plugins and modules, and… |
| 2026-10-12 09:51:24 | [smartness/laravel-logging](https://www.nuget.org/packages/smartness%2Flaravel-logging) | v0.1.2 |  | Structured JSON logging for Laravel with bounded normalization, redaction and r… |
| 2026-10-12 09:51:36 | [silarhi/tabler-ux-components](https://www.nuget.org/packages/silarhi%2Ftabler-ux-components) | v0.1.0 | Guillaume Sainthillier | Tabler-flavored Twig UX components for Symfony, following the shadcn compositio… |
| 2026-10-12 09:51:38 | [wexample/symfony-builder](https://www.nuget.org/packages/wexample%2Fsymfony-builder) | 1.0.2 |  |  |
| 2026-10-12 09:52:34 | [wexample/symfony-remote-pdf-factory](https://www.nuget.org/packages/wexample%2Fsymfony-remote-pdf-factory) | 1.0.1 |  |  |
| 2026-10-12 09:52:36 | [echo-fusion/modulemanager](https://www.nuget.org/packages/echo-fusion%2Fmodulemanager) | v1.0.0 | Amir Shadanfar | Module registry for the EchoFusion framework: modules declare their config, ser… |
| 2026-10-12 10:04:43 | [ongudidan/laravel-multi-2fa](https://www.nuget.org/packages/ongudidan%2Flaravel-multi-2fa) | v1.0.0 | Ongudidan | Unified Multi-Method Two-Factor Authentication for Laravel: Email OTP, Authenti… |
| 2026-10-12 10:06:39 | [framesnpictures/el-code-format](https://www.nuget.org/packages/framesnpictures%2Fel-code-format) | 0.1 | Chris Cynarski | Custom PHP-CS-Fixer rules |
| 2026-10-12 10:14:36 | [shopwell/conflicts](https://www.nuget.org/packages/shopwell%2Fconflicts) | 0.6.4 |  | Shopwell 6 conflicting packages |
| 2026-10-12 10:17:17 | [ongudidan/vscu-php-sdk](https://www.nuget.org/packages/ongudidan%2Fvscu-php-sdk) | v1.0.0 | Ongudidan | PHP SDK for VSCU eTIMS API |
| 2026-10-12 10:18:44 | [echo-fusion/templatemanager](https://www.nuget.org/packages/echo-fusion%2Ftemplatemanager) | v1.0.0 | Amir Shadanfar | Framework-independent template manager for EchoFusion: a built-in Twig/Smarty-s… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
