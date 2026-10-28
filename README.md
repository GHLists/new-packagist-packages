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

## Latest list — 2026-10-28 23:20 UTC

New packages created between 2026-10-28 22:19 UTC and 2026-10-28 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T23-20-29-575582Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 22:37:18 | [pushonltd/magento-patchline](https://www.nuget.org/packages/pushonltd%2Fmagento-patchline) | v0.0.2 | PushON Ltd; Jiří Brada | Checks and syncs Adobe's isolated security patches for a Magento store. |
| 2026-10-28 23:02:45 | [io/auth](https://www.nuget.org/packages/io%2Fauth) | v0.1.0 |  | Sign-in for Io sites: users with Argon2id passwords, database sessions, TOTP wi… |
| 2026-10-28 23:02:58 | [labskai/shopmade-shop](https://www.nuget.org/packages/labskai%2Fshopmade-shop) | v0.1.0 |  | Products, cart, guest checkout with optional Stripe, and orders for Shopmade. |
| 2026-10-28 23:03:58 | [labskai/shopmade-core](https://www.nuget.org/packages/labskai%2Fshopmade-core) | v0.1.0 |  | Shopmade core: a small website and customer system you run in Docker, edit over… |
| 2026-10-28 23:11:47 | [pushinbr/pam-native-drawer](https://www.nuget.org/packages/pushinbr%2Fpam-native-drawer) | 0.1.0 |  | Optional native drawer for PAM Native. |
| 2026-10-28 23:11:47 | [pushinbr/pam-native-toast](https://www.nuget.org/packages/pushinbr%2Fpam-native-toast) | 0.1.0 |  | Optional native toast for PAM Native. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
