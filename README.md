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

## Latest list — 2026-11-28 14:21 UTC

New packages created between 2026-11-28 13:19 UTC and 2026-11-28 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T14-21-51-923018Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 13:36:04 | [jaizendra-netizen/lead-source-conversion-report](https://www.nuget.org/packages/jaizendra-netizen%2Flead-source-conversion-report) | v1.0.0 | OneGTMLab | PHP CLI and library: funnel conversion by lead source from a CSV of leads and t… |
| 2026-11-28 13:36:16 | [jaizendra-netizen/sdr-activity-report](https://www.nuget.org/packages/jaizendra-netizen%2Fsdr-activity-report) | v1.0.0 | OneGTMLab | PHP CLI and library: activity report per sales development rep from a CSV of lo… |
| 2026-11-28 13:51:12 | [saascity/typo3-ai-robots](https://www.nuget.org/packages/saascity%2Ftypo3-ai-robots) | v1.0.0 | SaaSCity | TYPO3 CMS extension that serves clean, configurable AI crawler robots.txt direc… |
| 2026-11-28 13:51:16 | [saascity/contao-ai-robots-bundle](https://www.nuget.org/packages/saascity%2Fcontao-ai-robots-bundle) | v1.0.0 | SaaSCity | Contao CMS 5 bundle hooking contao.robots_txt to manage AI search and training… |
| 2026-11-28 13:51:20 | [saascity/mautic-ai-robots-bundle](https://www.nuget.org/packages/saascity%2Fmautic-ai-robots-bundle) | v1.0.0 | SaaSCity | Mautic 5 marketing automation plugin serving clean AI crawler robots.txt direct… |
| 2026-11-28 13:51:23 | [saascity/neos-ai-robots](https://www.nuget.org/packages/saascity%2Fneos-ai-robots) | v1.0.0 | SaaSCity | Neos CMS 8/9 package providing configurable AI crawler robots.txt generation an… |
| 2026-11-28 13:51:27 | [saascity/bolt-ai-robots](https://www.nuget.org/packages/saascity%2Fbolt-ai-robots) | v1.0.0 | SaaSCity | Bolt CMS 5 extension that generates and serves clean AI crawler robots.txt dire… |
| 2026-11-28 13:59:35 | [klsoft/auth-session](https://www.nuget.org/packages/klsoft%2Fauth-session) | 1.0.0 |  | Session based authentication |
| 2026-11-28 14:03:58 | [sec/cms-element-css-class](https://www.nuget.org/packages/sec%2Fcms-element-css-class) | 1.0.1 | Stefan Eik Christiansen | Adds CSS classes and HTML attributes to CMS elements. |
| 2026-11-28 14:06:05 | [bugo/scss-parser](https://www.nuget.org/packages/bugo%2Fscss-parser) | 0.1 | Bugo | Standalone SCSS, Sass and CSS syntax parser |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
