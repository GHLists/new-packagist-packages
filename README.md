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

## Latest list — 2026-10-03 21:20 UTC

New packages created between 2026-10-03 20:19 UTC and 2026-10-03 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T21-20-52-312094Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 20:30:59 | [formatsoft/content-reminder](https://www.nuget.org/packages/formatsoft%2Fcontent-reminder) | 0.1.0 | Andreas Kessel, format Softwa… | Content Reminder - Reminders for TYPO3 pages: due dates, recurrence, assignment… |
| 2026-10-03 20:44:15 | [26b/joiner](https://www.nuget.org/packages/26b%2Fjoiner) | 1.0.0 |  | Join strings with conditional values |
| 2026-10-03 20:51:03 | [ijeffro/laralocker](https://www.nuget.org/packages/ijeffro%2Flaralocker) | v3.0.0 | Phil Graham | A Laravel API connector for Learning Locker®, the open-source Learning Record S… |
| 2026-10-03 20:51:58 | [ssmiff/entabula](https://www.nuget.org/packages/ssmiff%2Fentabula) | v1.0.0 |  | Entabula, an entity-based admin panel, without any framework. Served by Laravel… |
| 2026-10-03 20:51:58 | [ssmiff/entabula-laravel](https://www.nuget.org/packages/ssmiff%2Fentabula-laravel) | v1.0.1 |  | Serves the ssmiff/entabula entity-based admin panel, from Laravel, with Eloquen… |
| 2026-10-03 20:51:58 | [ssmiff/entabula-mezzio](https://www.nuget.org/packages/ssmiff%2Fentabula-mezzio) | v1.0.1 |  | Serves the ssmiff/entabula entity-based admin panel, from Mezzio, with Doctrine… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
