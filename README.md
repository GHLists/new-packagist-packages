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

## Latest list — 2026-11-02 09:22 UTC

New packages created between 2026-11-02 08:20 UTC and 2026-11-02 09:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T09-22-01-439937Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 08:20:55 | [kopexa/mautic-oauth-bundle](https://www.nuget.org/packages/kopexa%2Fmautic-oauth-bundle) | v0.2.1 | Kopexa | OAuth 2.1 authorization server for Mautic (authorization code + PKCE S256, refr… |
| 2026-11-02 08:20:58 | [kopexa/mautic-mcp-bundle](https://www.nuget.org/packages/kopexa%2Fmautic-mcp-bundle) | v0.4.1 | Kopexa | Model Context Protocol (MCP) server for Mautic: lets Claude, ChatGPT and other… |
| 2026-11-02 08:21:00 | [kopexa/mautic-postal-bundle](https://www.nuget.org/packages/kopexa%2Fmautic-postal-bundle) | v0.1.1 | Kopexa | Postal mail server integration for Mautic: bounce and delivery-failure webhooks… |
| 2026-11-02 08:30:52 | [glue-agency/akeneo-glue-backoffice](https://www.nuget.org/packages/glue-agency%2Fakeneo-glue-backoffice) | 1.0.1 |  | Reports an Akeneo PIM to the Glue Dashboard after each deploy |
| 2026-11-02 08:34:15 | [pkc/barcode-qrcode](https://www.nuget.org/packages/pkc%2Fbarcode-qrcode) | v1.0.0 | PKC | Laravel Barcode & QR Code generator with SVG, HTML, and optional PNG output |
| 2026-11-02 08:37:12 | [colombia-kit/colombia-kit](https://www.nuget.org/packages/colombia-kit%2Fcolombia-kit) | v0.1.0 |  | Utilidades para datos colombianos en PHP: NIT con dígito de verificación, depar… |
| 2026-11-02 08:44:15 | [infinityinnovationsdev/codeigniter4-encrypted-env](https://www.nuget.org/packages/infinityinnovationsdev%2Fcodeigniter4-encrypted-env) | v1.1.1 |  | Optional AES-256-GCM encrypted environment values for CodeIgniter 4 |
| 2026-11-02 08:52:44 | [innoge/laravel-msgraph-mailbox](https://www.nuget.org/packages/innoge%2Flaravel-msgraph-mailbox) | v1.0.0 | Tim Geisendoerfer | Observe Microsoft 365 mailboxes via Microsoft Graph change notifications and de… |
| 2026-11-02 09:07:59 | [fivejars/media_directories_element](https://www.nuget.org/packages/fivejars%2Fmedia_directories_element) | 1.0.0 | Five Jars | Provides the media_directories form element: the Media Directories browser widg… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
