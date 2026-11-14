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

## Latest list — 2026-11-14 21:19 UTC

New packages created between 2026-11-14 20:19 UTC and 2026-11-14 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T21-19-40-635614Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 20:32:02 | [omnitrix/core](https://www.nuget.org/packages/omnitrix%2Fcore) | v0.1.1 | Ajmal Alkhaledi | Omnitrix: an asynchronous PHP framework for HTTP APIs on OpenSwoole (framework… |
| 2026-11-14 20:32:02 | [omnitrix/installer](https://www.nuget.org/packages/omnitrix%2Finstaller) | v0.1.0 | Ajmal Alkhaledi | Creates new Omnitrix applications: omnitrix new my-api |
| 2026-11-14 20:32:02 | [omnitrix/omnitrix](https://www.nuget.org/packages/omnitrix%2Fomnitrix) | v0.1.0 | Ajmal Alkhaledi | The Omnitrix application template: asynchronous PHP APIs on OpenSwoole. |
| 2026-11-14 20:37:59 | [diddyy/plumbline](https://www.nuget.org/packages/diddyy%2Fplumbline) | v0.1.0 |  | A precision-first static security scanner for Laravel applications. The scanner… |
| 2026-11-14 20:41:17 | [rmb32/barnspek](https://www.nuget.org/packages/rmb32%2Fbarnspek) | v0.1.0 | Roger Barnfather | Capture user stories and Given/When/Then acceptance scenarios as a living Speci… |
| 2026-11-14 20:41:18 | [rmb32/barnspek-cli](https://www.nuget.org/packages/rmb32%2Fbarnspek-cli) | v0.1.0 | Roger Barnfather | Barnspek CLI — the wizard plus Writer/Glossary/StoryMap rendering commands as a… |
| 2026-11-14 20:41:18 | [rmb32/barnspek-gui](https://www.nuget.org/packages/rmb32%2Fbarnspek-gui) | v0.1.0 | Roger Barnfather | A web GUI for managing Barnspek (Given When Then) Specification data, including… |
| 2026-11-14 20:41:39 | [itk/cms](https://www.nuget.org/packages/itk%2Fcms) | v0.1.0 |  | Symfony bundle that adds a CMS to a site: pages built from sections, collection… |
| 2026-11-14 21:02:31 | [generoi/gds-rate-limiter](https://www.nuget.org/packages/generoi%2Fgds-rate-limiter) | v1.0.0 | Genero | Answers 429 to IPs that flood PHP with uncached requests, before WordPress load… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
