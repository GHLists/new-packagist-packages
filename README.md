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

## Latest list — 2026-10-08 18:23 UTC

New packages created between 2026-10-08 17:22 UTC and 2026-10-08 18:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T18-23-23-334025Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 17:57:56 | [coffeemail/coffeemail-php](https://www.nuget.org/packages/coffeemail%2Fcoffeemail-php) | v0.1.0 | CoffeeMail Team | SDK oficial do CoffeeMail para PHP moderno (8.2+). Envio transacional de e-mail… |
| 2026-10-08 17:58:04 | [coffeemail/coffeemail-laravel](https://www.nuget.org/packages/coffeemail%2Fcoffeemail-laravel) | v0.1.0 | CoffeeMail Team | Driver oficial do CoffeeMail para Laravel Mailer, notificações e webhooks, com… |
| 2026-10-08 18:05:35 | [wotz/socialite-zenith](https://www.nuget.org/packages/wotz%2Fsocialite-zenith) | v0.1.0 |  | Laravel Socialite provider for Zenith, the WOTZ OAuth2 server |
| 2026-10-08 18:13:47 | [semitexa/crud](https://www.nuget.org/packages/semitexa%2Fcrud) | 2026.10.08.0620 | Semitexa | Semitexa CRUD: admin screens declared in one class — a list with its live feed,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
