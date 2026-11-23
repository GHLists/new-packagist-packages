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

## Latest list — 2026-11-23 22:20 UTC

New packages created between 2026-11-23 21:19 UTC and 2026-11-23 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T22-20-10-302268Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 21:22:00 | [blokbay/module-payment](https://www.nuget.org/packages/blokbay%2Fmodule-payment) | v1.1.0 | Blokbay | Blokbay crypto payments for Magento Open Source and Adobe Commerce: Bitcoin, US… |
| 2026-11-23 21:28:57 | [datacircle/bedrock-tools](https://www.nuget.org/packages/datacircle%2Fbedrock-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four tools for Amazon Bedrock's Converse API in the AWS… |
| 2026-11-23 21:29:09 | [mgamadeus/ddd-browser](https://www.nuget.org/packages/mgamadeus%2Fddd-browser) | 0.1.0-rc.4 | Marius-Eugen Gerdan | Browser sessions and website analysis for mgamadeus/ddd: agent-controllable bro… |
| 2026-11-23 21:29:43 | [puzzlesoft/activitylog-ui](https://www.nuget.org/packages/puzzlesoft%2Factivitylog-ui) | v1.0.0 | Puzzlesoft | A modern, friendly interface to browse activity logs recorded with spatie/larav… |
| 2026-11-23 21:31:34 | [freyr/message-broker-storage-postgresql](https://www.nuget.org/packages/freyr%2Fmessage-broker-storage-postgresql) | v0.1.0 | Freyr Development Team | PostgreSQL storage adapter for freyr/message-broker: outbox, deduplication and… |
| 2026-11-23 21:31:39 | [freyr/message-broker-transport-amqp](https://www.nuget.org/packages/freyr%2Fmessage-broker-transport-amqp) | v0.1.0 | Freyr Development Team | AMQP (RabbitMQ) transport adapter for freyr/message-broker: outbox relay publis… |
| 2026-11-23 21:31:43 | [freyr/message-broker-webhook-http](https://www.nuget.org/packages/freyr%2Fmessage-broker-webhook-http) | v0.1.0 | Freyr Development Team | HTTP webhook sender for freyr/message-broker: signed parallel requests (Standar… |
| 2026-11-23 21:31:48 | [freyr/message-broker-ratelimit-redis](https://www.nuget.org/packages/freyr%2Fmessage-broker-ratelimit-redis) | v0.1.0 | Freyr Development Team | Redis rate limit store for freyr/message-broker: the token buckets of the webho… |
| 2026-11-23 21:44:04 | [php-io-extensions/multicurl](https://www.nuget.org/packages/php-io-extensions%2Fmulticurl) | 0.11.1 | Project Saturn Studios, LLC | libcurl's multi socket API bound 1:1 into PHP on top of ext-curl handles |
| 2026-11-23 21:54:27 | [abolaradev/visitor-insight](https://www.nuget.org/packages/abolaradev%2Fvisitor-insight) | v1.0.0 | abolaradev | A Laravel package that provides comprehensive visitor information, including us… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
