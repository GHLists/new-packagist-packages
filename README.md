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

## Latest list — 2026-10-28 03:19 UTC

New packages created between 2026-10-28 02:21 UTC and 2026-10-28 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T03-19-11-203123Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 02:29:48 | [privatus/neos-analytics](https://www.nuget.org/packages/privatus%2Fneos-analytics) | v1.0.0 | Two Phase LLC | Adds the cookieless Privatus Analytics tracking script to your Neos site. No co… |
| 2026-10-28 02:33:11 | [pushinbr/pam-native-analytics](https://www.nuget.org/packages/pushinbr%2Fpam-native-analytics) | v0.1.0 |  | Privacy-safe product analytics (Firebase Analytics without advertising identifi… |
| 2026-10-28 02:33:30 | [pushinbr/pam-native-lottie](https://www.nuget.org/packages/pushinbr%2Fpam-native-lottie) | v0.1.0 |  | Native Lottie animations for PAM Native: lottie-android and lottie-ios behind o… |
| 2026-10-28 03:04:06 | [privatus/bolt-privatus-analytics](https://www.nuget.org/packages/privatus%2Fbolt-privatus-analytics) | v1.0.0 | Privatus Analytics | See how many real people visit your Bolt CMS site, without cookies. Adds the Pr… |
| 2026-10-28 03:04:14 | [privatus/automad-privatus-analytics](https://www.nuget.org/packages/privatus%2Fautomad-privatus-analytics) | v1.0.0 | Privatus Analytics | See how many real people visit your Automad site, without cookies. Adds the Pri… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
