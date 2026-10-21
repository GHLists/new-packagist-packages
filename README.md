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

## Latest list — 2026-10-21 15:22 UTC

New packages created between 2026-10-21 14:22 UTC and 2026-10-21 15:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T15-22-47-028079Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 14:25:07 | [ernestdefoe/shutter](https://www.nuget.org/packages/ernestdefoe%2Fshutter) | 1.1.0 | ernestdefoe | Photo contests for Flarum 2: staff run themed contests on a schedule, members s… |
| 2026-10-21 14:41:58 | [ernestdefoe/bouncer](https://www.nuget.org/packages/ernestdefoe%2Fbouncer) | 1.0.0 | ernestdefoe | Bot guard for Flarum 2, on your own server: turn away AI crawlers you don't wan… |
| 2026-10-21 14:43:08 | [ernestdefoe/gauntlet](https://www.nuget.org/packages/ernestdefoe%2Fgauntlet) | 1.0.0 | Ernest Defoe | Gauntlet — tournaments for Flarum. Single and double elimination, round robin a… |
| 2026-10-21 14:50:04 | [elife/api-sdk](https://www.nuget.org/packages/elife%2Fapi-sdk) | v1.0.0 |  | eLife Sciences API SDK |
| 2026-10-21 14:51:22 | [zeitpulse/minimaxcms](https://www.nuget.org/packages/zeitpulse%2Fminimaxcms) | 1.0.0 | Philipp Staender | minimaxcms - a minimal flat file markdown first cms |
| 2026-10-21 14:59:37 | [amjadiqbal/laravel-webhook-console](https://www.nuget.org/packages/amjadiqbal%2Flaravel-webhook-console) | v1.0.0 | Amjad Iqbal | Dashboard and replay tool for spatie/laravel-webhook-client: browse every recei… |
| 2026-10-21 15:14:13 | [haunt/settings](https://www.nuget.org/packages/haunt%2Fsettings) | 0.1 | crotanite | Sitewide settings for a Haunt application. |
| 2026-10-21 15:16:57 | [phasync/babel](https://www.nuget.org/packages/phasync%2Fbabel) | 0.1.0 | Frode Børli | Source rewriting tool that redirects function calls and class names to alternat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
