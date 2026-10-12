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

## Latest list — 2026-10-12 11:18 UTC

New packages created between 2026-10-12 10:21 UTC and 2026-10-12 11:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T11-18-53-17237Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 10:27:29 | [ssekyanzijackson/laravel-agent-web-search](https://www.nuget.org/packages/ssekyanzijackson%2Flaravel-agent-web-search) | v0.1.0 | Jackson Mwesigwa | Keyless web search and read tools for any Laravel AI agent: measured deadlines,… |
| 2026-10-12 10:27:47 | [invoicexml/zugferd-xrechnung](https://www.nuget.org/packages/invoicexml%2Fzugferd-xrechnung) | v1.0.0 | InvoiceXML | PHP client for ZUGFeRD and XRechnung e-invoices: create, validate, embed, rende… |
| 2026-10-12 10:27:50 | [invoicexml/facturx](https://www.nuget.org/packages/invoicexml%2Ffacturx) | v1.0.0 | InvoiceXML | PHP client for Factur-X e-invoices: create, validate, embed and extract EN 1693… |
| 2026-10-12 10:32:09 | [echo-fusion/databasemanager](https://www.nuget.org/packages/echo-fusion%2Fdatabasemanager) | v1.0.0 | Amir Shadanfar | A small, replaceable database layer for EchoFusion: a PDO connection, a query b… |
| 2026-10-12 10:44:49 | [stejac/guarded-chat-bundle](https://www.nuget.org/packages/stejac%2Fguarded-chat-bundle) | v1.0.1 | Stefan Jacomeit | Guardrails for public AI chats in Symfony apps: prompt versioning, injection pr… |
| 2026-10-12 10:52:17 | [echo-fusion/authmanager](https://www.nuget.org/packages/echo-fusion%2Fauthmanager) | v1.0.0 | Amir Shadanfar | Authentication for EchoFusion: session and token guards, pluggable user provide… |
| 2026-10-12 11:08:42 | [ravenrelay/php](https://www.nuget.org/packages/ravenrelay%2Fphp) | v0.1.0 |  | Server-side PHP SDK for the RavenRelay email API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
