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

## Latest list — 2026-11-10 21:22 UTC

New packages created between 2026-11-10 20:21 UTC and 2026-11-10 21:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T21-22-18-514045Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 20:26:57 | [versatecnologiaoficial/cadsus-client](https://www.nuget.org/packages/versatecnologiaoficial%2Fcadsus-client) | v1.1.1 |  | Cliente privado para autenticação e consultas CADSUS/CNS-PDQ. |
| 2026-11-10 20:31:26 | [beziworld/laravel-mailcow](https://www.nuget.org/packages/beziworld%2Flaravel-mailcow) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the mailcow API: domains, mailboxes, aliases, quotas, DKIM,… |
| 2026-11-10 20:32:04 | [beziworld/laravel-hestiacp](https://www.nuget.org/packages/beziworld%2Flaravel-hestiacp) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Hestia Control Panel API: users, web domains, DNS, mail,… |
| 2026-11-10 20:34:22 | [beziworld/laravel-emaillabs](https://www.nuget.org/packages/beziworld%2Flaravel-emaillabs) | v1.0.0 | Kamil Ćwiertnia | Laravel integration for EmailLabs (Vercom): mail transport, templates, tags and… |
| 2026-11-10 20:35:07 | [beziworld/laravel-getresponse](https://www.nuget.org/packages/beziworld%2Flaravel-getresponse) | v1.0.0 | Kamil Ćwiertnia | Laravel integration for GetResponse API v3: contacts with custom fields and tag… |
| 2026-11-10 20:35:48 | [beziworld/laravel-salesmanago](https://www.nuget.org/packages/beziworld%2Flaravel-salesmanago) | v1.0.0 | Kamil Ćwiertnia | Laravel client for SALESmanago (Manago AI): contacts, external events, consents… |
| 2026-11-10 20:36:34 | [beziworld/laravel-livespace](https://www.nuget.org/packages/beziworld%2Flaravel-livespace) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Livespace CRM API: persons, companies, deals, tasks, not… |
| 2026-11-10 20:37:01 | [beziworld/laravel-autenti](https://www.nuget.org/packages/beziworld%2Flaravel-autenti) | v1.0.0 | Kamil Ćwiertnia | Autenti e-signature API v2 for Laravel: document processes, participants, files… |
| 2026-11-10 20:38:47 | [beziworld/laravel-comfino](https://www.nuget.org/packages/beziworld%2Flaravel-comfino) | v1.0.0 | Kamil Ćwiertnia | ComfinoPay installments and buy now, pay later for Laravel: financial products,… |
| 2026-11-10 20:58:52 | [codifytech/asaas-sdk-laravel](https://www.nuget.org/packages/codifytech%2Fasaas-sdk-laravel) | 1.0.0 | CodifyTech | SDK Laravel para a API Asaas v3: cliente HTTP com retry, serviços tipados, Mode… |
| 2026-11-10 21:05:04 | [makermind/erd4dev](https://www.nuget.org/packages/makermind%2Ferd4dev) | v0.1.0 | Makermind | A Laravel/Livewire ER-diagram editor that turns visual database designs into re… |
| 2026-11-10 21:08:38 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.28.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-10 21:11:05 | [juaniquillo/svg-backend-components](https://www.nuget.org/packages/juaniquillo%2Fsvg-backend-components) | v0.1.0 | Juaniquillo | Build SVG graphics from PHP with typed elements and Tailwind themes for Laravel… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
