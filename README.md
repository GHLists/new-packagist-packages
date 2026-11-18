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

## Latest list — 2026-11-18 13:20 UTC

New packages created between 2026-11-18 12:19 UTC and 2026-11-18 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T13-20-25-928911Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 12:40:23 | [mcarrowsmith-packages/smtp-debug](https://www.nuget.org/packages/mcarrowsmith-packages%2Fsmtp-debug) | v1.0.0 |  | A trivial tool to test and debug SMTP connectivity using PHPMailer. Works stand… |
| 2026-11-18 12:44:15 | [aivcsb/nova-system-settings](https://www.nuget.org/packages/aivcsb%2Fnova-system-settings) | 1.0.2 |  | Nova 后台系统设置页: Schema 驱动的自定义设置表单 (常规/用户/安全/通知), 替代资源列表页 |
| 2026-11-18 12:49:33 | [limegreentangerine/zumika_social_wall](https://www.nuget.org/packages/limegreentangerine%2Fzumika_social_wall) | v1.0.0 | Dave Hendy | Show a Zumika social wall on your Concrete CMS site. |
| 2026-11-18 13:10:15 | [blackbird/customeritemstockalert-hyva-compatibility](https://www.nuget.org/packages/blackbird%2Fcustomeritemstockalert-hyva-compatibility) | 1.0.0 |  | Blackbird Customer Item Stock Alert Compatibility with Hÿva Theme check https:/… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
