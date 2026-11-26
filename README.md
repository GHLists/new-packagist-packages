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

## Latest list — 2026-11-26 11:19 UTC

New packages created between 2026-11-26 10:22 UTC and 2026-11-26 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T11-19-11-904306Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 10:31:37 | [kraz/json-rpc-server](https://www.nuget.org/packages/kraz%2Fjson-rpc-server) | 1.0.0 | Krasen Borisov | JSON-RPC 2.0 Server: transport-agnostic core, PSR-15 HTTP handler, attribute-dr… |
| 2026-11-26 10:34:32 | [upassist/neos-useravatar](https://www.nuget.org/packages/upassist%2Fneos-useravatar) | 0.1.0 |  | Profile photo (upload or Gravatar) for Neos backend users, shown in the Neos UI… |
| 2026-11-26 10:34:50 | [restruct/silverstripe-rendered-content-extractor](https://www.nuget.org/packages/restruct%2Fsilverstripe-rendered-content-extractor) | 0.1.0 | Restruct | Render a CMS page in-process (draft or live, as any member) and extract its HTM… |
| 2026-11-26 10:53:51 | [kraz/json-rpc-server-bundle](https://www.nuget.org/packages/kraz%2Fjson-rpc-server-bundle) | 1.0.0 | Krasen Borisov | Symfony bundle for kraz/json-rpc-server: JSON-RPC 2.0 endpoints with Security,… |
| 2026-11-26 10:53:57 | [beffroi/framework](https://www.nuget.org/packages/beffroi%2Fframework) | 0.1.0 | All contributors | An identity provider for the Symfony ecosystem: identity core, OAuth 2.0 / Open… |
| 2026-11-26 10:54:54 | [loamhill/api-php-sdk](https://www.nuget.org/packages/loamhill%2Fapi-php-sdk) | v1.0.1 |  | PHP SDK for the Loamhill crypto payment API |
| 2026-11-26 11:09:17 | [studio-variable/kirby-typography](https://www.nuget.org/packages/studio-variable%2Fkirby-typography) | v1.0.0 | Studio Variable | French typography for Kirby: automatic non-breaking spaces on output and a visi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
