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

## Latest list — 2026-09-27 14:21 UTC

New packages created between 2026-09-27 13:19 UTC and 2026-09-27 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T14-21-07-512664Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 13:20:59 | [weldist/spatie-medialibrary-media-hasher](https://www.nuget.org/packages/weldist%2Fspatie-medialibrary-media-hasher) | v1.1.0 | X-Adam | Computes one or more hashes (checksum, perceptual) of every file added to spati… |
| 2026-09-27 13:29:50 | [leobard/kirby-linkeddata](https://www.nuget.org/packages/leobard%2Fkirby-linkeddata) | 0.0.1 | Leo "Leobard" Sauermann | Kirby LinkedData for SEO |
| 2026-09-27 13:45:50 | [hydrakit/filesystem](https://www.nuget.org/packages/hydrakit%2Ffilesystem) | v0.9.16 | William Hleucka | File storage behind one contract: a private disk served through the app, a publ… |
| 2026-09-27 14:18:18 | [adamjenkins/moodle-filter_ruby](https://www.nuget.org/packages/adamjenkins%2Fmoodle-filter_ruby) | v1.0.1 |  | A Moodle text filter that adds furigana (ruby) readings above difficult kanji,… |
| 2026-09-27 14:18:59 | [snipershady/emailvalidator](https://www.nuget.org/packages/snipershady%2Femailvalidator) | v1.0.0 | Stefano Perrini | Simple, clean and reliable email validator for PHP >= 8.3: syntax, RFC 5322 for… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
