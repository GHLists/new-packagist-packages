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

## Latest list — 2026-10-24 05:20 UTC

New packages created between 2026-10-24 04:21 UTC and 2026-10-24 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T05-20-22-779142Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 04:37:18 | [bpmore/statamic-reel](https://www.nuget.org/packages/bpmore%2Fstatamic-reel) | 0.1.1 | Brent Passmore | Caption and transcript governance for the video and audio on a Statamic site. R… |
| 2026-10-24 04:50:35 | [daacreators/creators-audio-rooms](https://www.nuget.org/packages/daacreators%2Fcreators-audio-rooms) | v1.0.0 | DAA Creators | Live audio rooms for Laravel: hosts, speakers and listeners with hand raising a… |
| 2026-10-24 04:56:08 | [axitdev/phpunit-ai-evals](https://www.nuget.org/packages/axitdev%2Fphpunit-ai-evals) | v0.0.1 | Oleksii Ivanov | Framework-agnostic AI Evals, LLM-as-a-Judge & Smart VCR for PHPUnit |
| 2026-10-24 05:15:07 | [malikad/php2shell-guard](https://www.nuget.org/packages/malikad%2Fphp2shell-guard) | v0.3.1 | Malik Adnan | Read-only runtime, SAPI, stale-worker, configuration, and IaC auditor for PHP2S… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
