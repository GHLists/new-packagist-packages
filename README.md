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

## Latest list — 2026-09-28 19:20 UTC

New packages created between 2026-09-28 18:19 UTC and 2026-09-28 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T19-20-04-191041Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 18:32:44 | [jeytekdev/explain-lint](https://www.nuget.org/packages/jeytekdev%2Fexplain-lint) | v1.0.0 | Jeytekdev | Re-runs EXPLAIN against every SQL query captured during your test suite and fai… |
| 2026-09-28 18:32:45 | [jeytekdev/explain-lint-laravel](https://www.nuget.org/packages/jeytekdev%2Fexplain-lint-laravel) | v1.0.0 | Jeytekdev | Laravel bridge for jeytekdev/explain-lint — captures queries via DB::listen() a… |
| 2026-09-28 18:32:46 | [jeytekdev/explain-lint-yii2](https://www.nuget.org/packages/jeytekdev%2Fexplain-lint-yii2) | v1.0.0 | Jeytekdev | Yii2 bridge for jeytekdev/explain-lint — wraps the DB connection's PDO handle a… |
| 2026-09-28 18:32:49 | [jeytekdev/explain-lint-doctrine](https://www.nuget.org/packages/jeytekdev%2Fexplain-lint-doctrine) | v1.0.0 | Jeytekdev | Doctrine DBAL bridge for jeytekdev/explain-lint — captures queries via a Driver… |
| 2026-09-28 18:34:06 | [erag/inertia-forms](https://www.nuget.org/packages/erag%2Finertia-forms) | v0.0.1 | Er Amit Gupta | Define Laravel forms in PHP and render them with Inertia.js in Vue, React, or S… |
| 2026-09-28 18:42:31 | [sailantis/clarity-engine](https://www.nuget.org/packages/sailantis%2Fclarity-engine) | v0.1.0 | Sailantis | A fast and powerful Template engine for PHP inspired by Twig. |
| 2026-09-28 18:51:18 | [pigagent/pig](https://www.nuget.org/packages/pigagent%2Fpig) | v0.1.0 | owner888 | pi, ported to PHP: agent core, unified LLM API, terminal UI, coding agent CLI |
| 2026-09-28 19:06:55 | [codingducksrl/laravel-queue-monitor](https://www.nuget.org/packages/codingducksrl%2Flaravel-queue-monitor) | 1.0.0 | Coding Duck s.r.l. | Queue monitoring for Laravel applications |
| 2026-09-28 19:14:19 | [yossuf/laravel-geocoding](https://www.nuget.org/packages/yossuf%2Flaravel-geocoding) | v0.1.0 |  | Minimalist, self-hosted geocoding using datasets from national registry. |
| 2026-09-28 19:19:29 | [lenorix/laravel-beel](https://www.nuget.org/packages/lenorix%2Flaravel-beel) | v0.1.0 | Jesus Hernandez | Laravel integration for the BeeL invoicing API unofficial PHP SDK |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
