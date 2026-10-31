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

## Latest list — 2026-10-31 19:21 UTC

New packages created between 2026-10-31 18:19 UTC and 2026-10-31 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T19-21-02-808471Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 18:27:31 | [cacheerphp/laravel](https://www.nuget.org/packages/cacheerphp%2Flaravel) | v1.0.0 | Silvio Silva | A Laravel cache driver backed by CacheerPHP: keep using Cache:: and get Cacheer… |
| 2026-10-31 18:43:52 | [forumify/forumify-ecommerce-plugin](https://www.nuget.org/packages/forumify%2Fforumify-ecommerce-plugin) | 1.0.0 |  | Bring e-commerce to your forumify powered community! |
| 2026-10-31 19:09:12 | [mammothwp/wp-kit](https://www.nuget.org/packages/mammothwp%2Fwp-kit) | v2.0.2 | Mammoth WP | Declare a WordPress feature once and expose it as a REST route, a WP-CLI comman… |
| 2026-10-31 19:10:54 | [matthewaprice/phossil-starter](https://www.nuget.org/packages/matthewaprice%2Fphossil-starter) | v0.1.0 | Matthew Price | Starter site for phossil: routes, typed views and components that build to plai… |
| 2026-10-31 19:11:25 | [mammothwp/wp-self-test](https://www.nuget.org/packages/mammothwp%2Fwp-self-test) | v2.2.5 | Mammoth WP | Manifest-driven self-test suite for WordPress plugins: register a manifest of c… |
| 2026-10-31 19:11:36 | [mammothwp/support](https://www.nuget.org/packages/mammothwp%2Fsupport) | v1.1.1 | Mammoth WP | One shared Support screen for every plugin that bundles it: the customer fills… |
| 2026-10-31 19:13:15 | [mammothwp/wp-release](https://www.nuget.org/packages/mammothwp%2Fwp-release) | v1.0.1 | Mammoth WP | Prepare, verify and ship a Mammoth WP plugin release to wordpress.org and GitHu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
