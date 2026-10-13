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

## Latest list — 2026-10-13 13:20 UTC

New packages created between 2026-10-13 12:19 UTC and 2026-10-13 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T13-20-40-187586Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 12:26:32 | [j87nl/laravel-mailbox](https://www.nuget.org/packages/j87nl%2Flaravel-mailbox) | 0.1.1 | Johan | Shared IMAP/SMTP mailboxes for Laravel: sync, folder actions, sending and an au… |
| 2026-10-13 12:26:35 | [j87nl/laravel-vue-mailbox](https://www.nuget.org/packages/j87nl%2Flaravel-vue-mailbox) | 0.1.0 | Johan | A VueJS/Inertia shared mailbox UI for j87nl/laravel-mailbox, built on the FormB… |
| 2026-10-13 12:35:06 | [slohmaier/roundcube_caldav_suite](https://www.nuget.org/packages/slohmaier%2Froundcube_caldav_suite) | v1.1.0 | Stefan Lohmaier | CalDAV Calendar & Tasks plugin for Roundcube - connects to any CalDAV server |
| 2026-10-13 12:44:43 | [givanov95/laravel-shipping-boxnow](https://www.nuget.org/packages/givanov95%2Flaravel-shipping-boxnow) | v0.1.1 | Georgi Ivanov | BoxNow lockers as a delivery method of a Laravel shop: the API client and the a… |
| 2026-10-13 12:44:43 | [givanov95/laravel-shipping-econt](https://www.nuget.org/packages/givanov95%2Flaravel-shipping-econt) | v0.1.0 | Georgi Ivanov | Econt as a delivery method of a Laravel shop: the API client and the adapter to… |
| 2026-10-13 12:44:43 | [givanov95/laravel-shipping-speedy](https://www.nuget.org/packages/givanov95%2Flaravel-shipping-speedy) | v0.1.0 | Georgi Ivanov | Speedy as a delivery method of a Laravel shop: the API client and the adapter t… |
| 2026-10-13 12:45:46 | [balpom/simple-cache](https://www.nuget.org/packages/balpom%2Fsimple-cache) | v0.1.1 | Mikhail (Balpom) | Simple realisation of simple PSR16 cache. |
| 2026-10-13 12:50:52 | [mtubis/html-translator](https://www.nuget.org/packages/mtubis%2Fhtml-translator) | v0.4.0 | Magdalena Tubis | Translate HTML with LLMs (OpenAI, Anthropic, Gemini, Ollama, …) while preservin… |
| 2026-10-13 12:50:55 | [artisan-build/wake-client](https://www.nuget.org/packages/artisan-build%2Fwake-client) | v0.1.0 |  | The Laravel log client for a self-hosted Wake server. |
| 2026-10-13 12:50:58 | [artisan-build/wake-contracts](https://www.nuget.org/packages/artisan-build%2Fwake-contracts) | v0.1.0 |  | The versioned wire contracts shared by the Wake client and server. |
| 2026-10-13 12:51:01 | [artisan-build/wake-server](https://www.nuget.org/packages/artisan-build%2Fwake-server) | v0.1.0 |  | The ingest, storage, and MCP server package for Wake. |
| 2026-10-13 12:59:12 | [keychat/bots](https://www.nuget.org/packages/keychat%2Fbots) | v0.1.0 |  | Official PHP SDK for Key Chat bots |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
