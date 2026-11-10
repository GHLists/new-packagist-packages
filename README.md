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

## Latest list — 2026-11-10 20:21 UTC

New packages created between 2026-11-10 19:20 UTC and 2026-11-10 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T20-21-23-204016Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 19:21:22 | [beziworld/laravel-docx-templates](https://www.nuget.org/packages/beziworld%2Flaravel-docx-templates) | v1.0.0 | Kamil Ćwiertnia | Word (.docx) templates for Laravel on PHPWord: filesystem disks, variables, blo… |
| 2026-11-10 19:22:11 | [beziworld/laravel-unifi](https://www.nuget.org/packages/beziworld%2Flaravel-unifi) | v1.0.0 | Kamil Ćwiertnia | Laravel client for UniFi Network: official API and classic controller API for s… |
| 2026-11-10 19:22:17 | [ernestdefoe/who-said-it](https://www.nuget.org/packages/ernestdefoe%2Fwho-said-it) | 1.0.0 | Ernest Defoe | Who Said It? A daily quiz made from your forum's own posts: five real quotes, f… |
| 2026-11-10 19:22:44 | [beziworld/laravel-proxmox](https://www.nuget.org/packages/beziworld%2Flaravel-proxmox) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Proxmox VE API: nodes, QEMU VMs, LXC containers, snapsho… |
| 2026-11-10 19:23:11 | [beziworld/laravel-ispconfig](https://www.nuget.org/packages/beziworld%2Flaravel-ispconfig) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the ISPConfig 3 remote API: clients, websites, DNS, mail, da… |
| 2026-11-10 19:30:45 | [ernestdefoe/forum-pet](https://www.nuget.org/packages/ernestdefoe%2Fforum-pet) | 1.0.0 | Ernest Defoe | Forum Pet: a shared mascot the whole community takes care of. It lives in the s… |
| 2026-11-10 19:33:44 | [cengizkemec/flarum-social](https://www.nuget.org/packages/cengizkemec%2Fflarum-social) | v1.1.0 | Cengiz Kemec | Discord-inspired social community platform for Flarum 2.0: public visitor brows… |
| 2026-11-10 19:40:44 | [ernestdefoe/community-goals](https://www.nuget.org/packages/ernestdefoe%2Fcommunity-goals) | 1.0.0 | Ernest Defoe | Community Goals: the whole forum works together toward a shared target. Replies… |
| 2026-11-10 19:41:32 | [ernestdefoe/question-of-the-day](https://www.nuget.org/packages/ernestdefoe%2Fquestion-of-the-day) | 1.0.0 | Ernest Defoe | Question of the Day: one prompt a day on your forum's front page. Members answe… |
| 2026-11-10 19:50:17 | [ernestdefoe/mural](https://www.nuget.org/packages/ernestdefoe%2Fmural) | 1.0.0 | Ernest Defoe | Mural: one shared pixel canvas the whole forum paints together. One tile per co… |
| 2026-11-10 20:02:00 | [ernestdefoe/fanfare](https://www.nuget.org/packages/ernestdefoe%2Ffanfare) | 1.0.0 | Ernest Defoe | Fanfare: the forum marks the moment. Member birthdays and join anniversaries, t… |
| 2026-11-10 20:03:16 | [ernestdefoe/sticker-book](https://www.nuget.org/packages/ernestdefoe%2Fsticker-book) | 1.0.0 | Ernest Defoe | Sticker Book: members collect stickers in an album. A free pack every day with… |
| 2026-11-10 20:11:21 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.27.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-10 20:15:32 | [xudid/mistral-client](https://www.nuget.org/packages/xudid%2Fmistral-client) | 0.1.1 | Didier Moindreau |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
