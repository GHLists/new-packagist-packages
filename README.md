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

## Latest list — 2026-11-11 22:21 UTC

New packages created between 2026-11-11 21:20 UTC and 2026-11-11 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T22-21-52-738923Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 21:22:28 | [phil/ux-kit](https://www.nuget.org/packages/phil%2Fux-kit) | 0.1.0-alpha | Philippe Gamache | PHIL UX kit for the Symfony UX Toolkit: the same recipes as the Shadcn kit, sty… |
| 2026-11-11 21:22:29 | [phil/ux-css](https://www.nuget.org/packages/phil%2Fux-css) | 0.1.0-alpha | Philippe Gamache | phil-ux, the CSS framework of PHIL: real, mostly classless CSS with --phil-* to… |
| 2026-11-11 21:23:31 | [ernestdefoe/latest-replies](https://www.nuget.org/packages/ernestdefoe%2Flatest-replies) | 1.0.0 | Ernest Defoe | Latest Replies: a widget of the newest replies on your forum, in the sidebar, a… |
| 2026-11-11 21:29:33 | [stackradar/laravel](https://www.nuget.org/packages/stackradar%2Flaravel) | v0.1.0 |  | Laravel integration for StackRadar runtime dependency inventory. |
| 2026-11-11 21:38:44 | [ernestdefoe/stances](https://www.nuget.org/packages/ernestdefoe%2Fstances) | 1.0.0 | Ernest Defoe | Stances: one-click Agree/Disagree, Yes/No, This-or-That and Rating blocks anywh… |
| 2026-11-11 21:46:33 | [blemli/splitbutton-for-filament](https://www.nuget.org/packages/blemli%2Fsplitbutton-for-filament) | v0.1.0 | grafst | The button that adapts to how you work. |
| 2026-11-11 22:06:45 | [php-io-extensions/libsoundio](https://www.nuget.org/packages/php-io-extensions%2Flibsoundio) | v0.11.0 | Project Saturn Studios, LLC | 1:1 PHP bindings of libsoundio 2.0: backends, devices, channel layouts, formats… |
| 2026-11-11 22:19:20 | [mattitja/bad-ip-blocker](https://www.nuget.org/packages/mattitja%2Fbad-ip-blocker) | v1.0.0 | Mattitja AB | Block bad IPs in Laravel using a local JSON list with automatic blocking of sca… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
