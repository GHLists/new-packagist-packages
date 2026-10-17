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

## Latest list — 2026-10-17 15:19 UTC

New packages created between 2026-10-17 14:21 UTC and 2026-10-17 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T15-19-07-037302Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 14:29:27 | [alantiller/permission](https://www.nuget.org/packages/alantiller%2Fpermission) | v1.0.0 | Alan Tiller | PDO permissions, optional roles and application-defined policies for PHP |
| 2026-10-17 14:30:20 | [zeusi/circuit-breaker](https://www.nuget.org/packages/zeusi%2Fcircuit-breaker) | 0.1.0 | Antonio Turdo | A circuit breaker for PHP with bucketed sliding windows and configurable half-o… |
| 2026-10-17 14:50:41 | [utab/laravel-backup-kit](https://www.nuget.org/packages/utab%2Flaravel-backup-kit) | v1.0.0 | Utab Platform | Encrypted, monitored database backups for Laravel on S3-compatible storage, bui… |
| 2026-10-17 14:54:48 | [wuninsu/nativephp-biometrics](https://www.nuget.org/packages/wuninsu%2Fnativephp-biometrics) | v0.1.0 | Fuseini Abdul-Hafiz | Fingerprint, Face ID and Touch ID prompts for NativePHP Mobile apps. |
| 2026-10-17 14:55:43 | [wuninsu/nativephp-secure-storage](https://www.nuget.org/packages/wuninsu%2Fnativephp-secure-storage) | v0.1.0 | Fuseini Abdul-Hafiz | Keep small secrets (such as API tokens) in the iOS Keychain or the Android Keys… |
| 2026-10-17 15:01:12 | [cosmemilton/acbr-php](https://www.nuget.org/packages/cosmemilton%2Facbr-php) | v0.1.0-alpha1 |  | Framework-independent PHP client for the pinned ACBr NF-e/NFC-e Linux worker |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
