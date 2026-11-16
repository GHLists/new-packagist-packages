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

## Latest list — 2026-11-16 03:19 UTC

New packages created between 2026-11-16 02:22 UTC and 2026-11-16 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T03-19-05-457325Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 02:31:30 | [configdirector/openfeature-server-provider](https://www.nuget.org/packages/configdirector%2Fopenfeature-server-provider) | v0.1.0 | ConfigDirector | OpenFeature server provider for ConfigDirector. ConfigDirector is a remote conf… |
| 2026-11-16 02:38:39 | [thuraaung2493/laravel-nrc-kit](https://www.nuget.org/packages/thuraaung2493%2Flaravel-nrc-kit) | v0.1.0 |  | Offline Myanmar NRC validation, conversion and native Blade selector |
| 2026-11-16 02:42:26 | [otaqq/form-datalayer](https://www.nuget.org/packages/otaqq%2Fform-datalayer) | v0.2.0 | otaqq | Measure every form step (input, confirm, complete, error) with Google Tag Manag… |
| 2026-11-16 02:43:29 | [sailantis/laravel-volucer](https://www.nuget.org/packages/sailantis%2Flaravel-volucer) | v0.4.2 |  | Run a Laravel application on volucer's persistent worker protocol. |
| 2026-11-16 02:43:31 | [sailantis/symfony-volucer](https://www.nuget.org/packages/sailantis%2Fsymfony-volucer) | v0.4.2 |  | Run a Symfony application on volucer's persistent worker protocol: kernel reboo… |
| 2026-11-16 02:43:33 | [sailantis/spiral-volucer](https://www.nuget.org/packages/sailantis%2Fspiral-volucer) | v0.4.2 |  | Run a Spiral application on volucer's persistent worker protocol. |
| 2026-11-16 02:48:21 | [campkitchenus/flarum-camp-water](https://www.nuget.org/packages/campkitchenus%2Fflarum-camp-water) | v1.0.0 | Camp Kitchen US | Add a [campwater] tag to Flarum posts that shows how much water a car-camping t… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
