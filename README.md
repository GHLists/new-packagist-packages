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

## Latest list — 2026-11-10 19:20 UTC

New packages created between 2026-11-10 18:20 UTC and 2026-11-10 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T19-20-45-880432Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 18:22:27 | [foorschtbar/applecolorflags](https://www.nuget.org/packages/foorschtbar%2Fapplecolorflags) | v1.0.1 | foorschtbar | Shows Apple Mail colour flags in Roundcube and adds colour entries to the Mark… |
| 2026-11-10 18:44:30 | [moudarir/mailer](https://www.nuget.org/packages/moudarir%2Fmailer) | 1.0.1 | Abdessamad MOUDARIR | A lightweight and flexible PHP mail library supporting native mail(), sendmail,… |
| 2026-11-10 18:46:44 | [beziworld/laravel-globkurier](https://www.nuget.org/packages/beziworld%2Flaravel-globkurier) | v1.0.0 | Kamil Ćwiertnia | GlobKurier.pl REST API v1 client for Laravel: product search and quotes, add-on… |
| 2026-11-10 18:48:18 | [beziworld/laravel-label-printing](https://www.nuget.org/packages/beziworld%2Flaravel-label-printing) | v1.0.0 | Kamil Ćwiertnia | Label and receipt printing for Laravel: named printers over TCP 9100, CUPS and… |
| 2026-11-10 18:49:39 | [beziworld/laravel-xades](https://www.nuget.org/packages/beziworld%2Flaravel-xades) | v1.0.0 | Kamil Ćwiertnia | XAdES-BES and XAdES-B-B signing and verification of XML documents in Laravel wi… |
| 2026-11-10 18:54:38 | [ernestdefoe/story-chain](https://www.nuget.org/packages/ernestdefoe%2Fstory-chain) | 1.0.0 | Ernest Defoe | Story Chain: the forum writes a story together, one line at a time. Members eac… |
| 2026-11-10 19:07:10 | [ernestdefoe/hype-market](https://www.nuget.org/packages/ernestdefoe%2Fhype-market) | 1.0.0 | Ernest Defoe | Hype Market: members back the new discussions they think will take off. Free da… |
| 2026-11-10 19:15:54 | [danog/mongo-php-async-driver](https://www.nuget.org/packages/danog%2Fmongo-php-async-driver) | v0.1.0 | Daniil Gentili | Drop-in replacement for the mongodb PHP extension (ext-mongodb 2.5.6) in pure R… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
