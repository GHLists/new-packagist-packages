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

## Latest list — 2026-10-12 08:21 UTC

New packages created between 2026-10-12 07:23 UTC and 2026-10-12 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T08-21-03-438924Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 07:29:19 | [cymdeveloppement/roundcube-gdrive-attachments](https://www.nuget.org/packages/cymdeveloppement%2Froundcube-gdrive-attachments) | v1.0.0 | Yann Challet | Uploads attachments larger than the message size limit to a Google shared drive… |
| 2026-10-12 07:36:42 | [tancky/upscale-calculator](https://www.nuget.org/packages/tancky%2Fupscale-calculator) | v1.0.0 | Tancky AI | Dependency-free PHP helpers for image upscaling math: scaled dimensions, the sm… |
| 2026-10-12 07:39:15 | [jnana/jnana](https://www.nuget.org/packages/jnana%2Fjnana) | v1.0.2 |  | Project skeleton for the Jnana framework. Run `composer create-project jnana/jn… |
| 2026-10-12 07:47:06 | [alengo/sulu-content-assistant-bundle](https://www.nuget.org/packages/alengo%2Fsulu-content-assistant-bundle) | 0.1 | Alexander Huber-De Monte | Sulu 3 admin assistant: create pages, articles and snippets from content templa… |
| 2026-10-12 07:56:48 | [irondome/mail-canon](https://www.nuget.org/packages/irondome%2Fmail-canon) | v0.1.0 |  | Bounded, provider-aware email normalization |
| 2026-10-12 08:15:07 | [saeedmohsenii/laravel-atlasm-sms](https://www.nuget.org/packages/saeedmohsenii%2Flaravel-atlasm-sms) | v1.0.0 | Saeed Mohseni | Laravel package for sending SMS and checking credit / delivery status through t… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
