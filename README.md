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

## Latest list — 2026-10-12 06:20 UTC

New packages created between 2026-10-12 05:19 UTC and 2026-10-12 06:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T06-20-07-167812Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 05:40:28 | [drevops/eddy-tooling](https://www.nuget.org/packages/drevops%2Feddy-tooling) | 1.0.0 | Alex Skrypnyk | Commands that build, run, test and deploy Drupal extensions created from Eddy. |
| 2026-10-12 05:47:23 | [phattarachai/git-prompt](https://www.nuget.org/packages/phattarachai%2Fgit-prompt) | v1.0.1 | Phattarachai | A PHPStorm-style git branch popup for the terminal — search branches and action… |
| 2026-10-12 05:54:05 | [apricot/shoutbox](https://www.nuget.org/packages/apricot%2Fshoutbox) | 0.5.0 | Alex Brindley | An example apricot extension. Tiny shoutbox that touches all basics |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
