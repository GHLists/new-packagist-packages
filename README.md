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

## Latest list — 2026-10-25 21:20 UTC

New packages created between 2026-10-25 20:21 UTC and 2026-10-25 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T21-20-29-654772Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 20:38:46 | [mj-zana/communication](https://www.nuget.org/packages/mj-zana%2Fcommunication) | v2.1.0 |  | Email for Zana applications: messages, configured senders, Symfony Mailer trans… |
| 2026-10-25 20:38:46 | [mj-zana/translation](https://www.nuget.org/packages/mj-zana%2Ftranslation) | v2.1.0 |  | Translation catalogs, locale negotiation and the request locale for Zana applic… |
| 2026-10-25 20:38:46 | [mj-zana/view](https://www.nuget.org/packages/mj-zana%2Fview) | v2.1.0 |  | HTML views for Zana applications: templates per module, layouts, escaping by de… |
| 2026-10-25 20:38:46 | [mj-zana/view-twig](https://www.nuget.org/packages/mj-zana%2Fview-twig) | v2.1.0 |  | Twig templates for mj-zana/view |
| 2026-10-25 20:43:27 | [makallio85/rocksoftware-cakephp-ui](https://www.nuget.org/packages/makallio85%2Frocksoftware-cakephp-ui) | v1.0.1 | Marko Kallio | CakePHP 5 plugin with the shared screen frame of a Rock Software application: p… |
| 2026-10-25 20:58:30 | [alex-kassel/site-cloner](https://www.nuget.org/packages/alex-kassel%2Fsite-cloner) | v1.0.0 | AlexKassel | Full website and demo-template offline cloner for Laravel with asset rewriting,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
