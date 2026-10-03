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

## Latest list — 2026-10-03 22:20 UTC

New packages created between 2026-10-03 21:20 UTC and 2026-10-03 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T22-20-04-418615Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 21:21:05 | [themusicdev/trailing-slash](https://www.nuget.org/packages/themusicdev%2Ftrailing-slash) | v1.0.0 | TheMusicDev | CakePHP 5 plugin: one middleware that 301-redirects trailing-slash URLs to the… |
| 2026-10-03 21:41:38 | [marcinwolnyeu/slopshape-php](https://www.nuget.org/packages/marcinwolnyeu%2Fslopshape-php) | v1.0.0 | Marcin Wolny | Explainable AI text detector for PHP: scores how likely an English text is AI/L… |
| 2026-10-03 22:02:16 | [ernestdefoe/folio](https://www.nuget.org/packages/ernestdefoe%2Ffolio) | 1.0.0 | Ernest Defoe | Export a Flarum discussion as a PDF, a Word document or Markdown — styled in th… |
| 2026-10-03 22:04:55 | [lambda-twelve/one-record](https://www.nuget.org/packages/lambda-twelve%2Fone-record) | 1.0.0-beta1 | Nick Andriopoulos | A framework-agnostic PHP server (PSR-15) and client (PSR-18) implementation for… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
