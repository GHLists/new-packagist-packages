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

## Latest list — 2026-10-28 09:20 UTC

New packages created between 2026-10-28 08:20 UTC and 2026-10-28 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T09-20-52-29602Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 08:39:34 | [tevkert/queue-prefork](https://www.nuget.org/packages/tevkert%2Fqueue-prefork) | v1.0.0 | Ando Hakobyan | Cut the memory of Laravel queue workers by up to 80 %: queue:work and Horizon w… |
| 2026-10-28 08:45:36 | [lck/swoft](https://www.nuget.org/packages/lck%2Fswoft) | v2.0.13 |  | Swoft skeleton application, PHP 8.4 ready maintained fork |
| 2026-10-28 08:50:22 | [bensomething/craft-namecheck](https://www.nuget.org/packages/bensomething%2Fcraft-namecheck) | 1.0.0-beta.1 |  | Automatically link the names of your entries wherever your content mentions the… |
| 2026-10-28 08:52:43 | [vinh0809it/keycloak-bundle](https://www.nuget.org/packages/vinh0809it%2Fkeycloak-bundle) | v0.1.0 | Vinh Vo | Keycloak for Symfony: a firewall authenticator over Symfony's OIDC token handle… |
| 2026-10-28 08:55:47 | [queuey/queuey](https://www.nuget.org/packages/queuey%2Fqueuey) | v1.0.0 | Jaap Elst | A pure-PHP job queue with RabbitMQ transport, wire-compatible with the queuey R… |
| 2026-10-28 09:02:17 | [queuey/symfony](https://www.nuget.org/packages/queuey%2Fsymfony) | v1.0.0 | Jaap Elst | Symfony bundle for queuey: container wiring, configuration, console commands, e… |
| 2026-10-28 09:12:20 | [mdestafadilah/satusehat-sdk](https://www.nuget.org/packages/mdestafadilah%2Fsatusehat-sdk) | 0.9.0 | Agung Gumilang | Unofficial API wrapper package to integrate with SATUSEHAT platform (fork of ag… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
