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

## Latest list — 2026-11-25 22:19 UTC

New packages created between 2026-11-25 21:21 UTC and 2026-11-25 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T22-19-50-69273Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 21:22:13 | [dmstr/firecrawl-bundle](https://www.nuget.org/packages/dmstr%2Ffirecrawl-bundle) | 0.1.0 | diemeisterei GmbH | Symfony bundle for self-hosted Firecrawl v2: a `firecrawl` connection type of d… |
| 2026-11-25 21:33:37 | [atom-fm/sql](https://www.nuget.org/packages/atom-fm%2Fsql) | v0.1.0 |  | Parameterized SQL query builder and dialect compilers for PHP |
| 2026-11-25 21:33:47 | [atom-fm/orm](https://www.nuget.org/packages/atom-fm%2Form) | v0.1.0 |  | Attribute-based PHP models and persistence using PDO |
| 2026-11-25 21:44:05 | [owner888/php-http](https://www.nuget.org/packages/owner888%2Fphp-http) | v1.0.0 | owner888 | Zero-dependency pure-PHP 8.3+ async event loop (stream_select / Io\Poll + Fiber… |
| 2026-11-25 21:46:04 | [goodport/laravel-ai-journal](https://www.nuget.org/packages/goodport%2Flaravel-ai-journal) | v1.0.0 | goodport | Journal and response replay for Laravel AI agent calls. |
| 2026-11-25 21:51:38 | [aymericcucherousset/d2-symfony](https://www.nuget.org/packages/aymericcucherousset%2Fd2-symfony) | v0.1.0 | Aymeric Cucherousset | Render D2 diagrams (d2lang.com) in Symfony & Twig: local binary or Kroki, cache… |
| 2026-11-25 21:54:36 | [ghazali/laravel-hybrid-crypto](https://www.nuget.org/packages/ghazali%2Flaravel-hybrid-crypto) | v1.0.1 |  | A Laravel package for hybrid encryption using P-384, X25519, and ML-KEM-768. |
| 2026-11-25 21:54:47 | [ghazali/universal-probabilistic-engine](https://www.nuget.org/packages/ghazali%2Funiversal-probabilistic-engine) | v1.0.1 | Ghazali | Universal Probabilistic Engine (UPE) providing O(1) Bloom Filter shielding and… |
| 2026-11-25 22:07:06 | [kaizendeveloper/iniparser](https://www.nuget.org/packages/kaizendeveloper%2Finiparser) | v1.0.0 | Miguel Delli Carpini; Austin… | A Zend_Config_Ini like parser for .ini files. Forked from austinhyde/iniparser… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
