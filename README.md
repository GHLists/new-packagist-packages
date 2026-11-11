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

## Latest list — 2026-11-11 13:22 UTC

New packages created between 2026-11-11 12:19 UTC and 2026-11-11 13:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T13-22-10-121027Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 12:31:13 | [limegreentangerine/banner_manager_kit](https://www.nuget.org/packages/limegreentangerine%2Fbanner_manager_kit) | 1.1.0 | Dave Hendy | Concrete CMS package for managing scheduled banners and slideshows from the das… |
| 2026-11-11 12:38:26 | [txlemetry/txlemetry-php](https://www.nuget.org/packages/txlemetry%2Ftxlemetry-php) | 5.0.0 | PostHog <engineering@posthog.… | Txlemetry PHP SDK |
| 2026-11-11 12:39:07 | [xakki/cli-backup](https://www.nuget.org/packages/xakki%2Fcli-backup) | v0.2.0 |  | Python backup CLI source and AI agent skills for databases and file archives |
| 2026-11-11 12:48:21 | [letterncms/consent](https://www.nuget.org/packages/letterncms%2Fconsent) | 0.2.0 |  | A cookie-consent banner in your site’s own design: visitors choose analytics an… |
| 2026-11-11 12:48:50 | [letterncms/import](https://www.nuget.org/packages/letterncms%2Fimport) | 0.2.0 |  | Bring a site over: WordPress exports with their media and old addresses, CSV fi… |
| 2026-11-11 12:49:18 | [letterncms/webhooks](https://www.nuget.org/packages/letterncms%2Fwebhooks) | 0.2.0 |  | Tell other services what happens on your site: signed webhooks for entries, med… |
| 2026-11-11 12:51:19 | [mailgatewayid/php](https://www.nuget.org/packages/mailgatewayid%2Fphp) | v0.1.0 |  | Official zero-dependency PHP client for MailGateway.id Email API |
| 2026-11-11 12:54:39 | [olegacy/bitrix-user-discounts-resolver](https://www.nuget.org/packages/olegacy%2Fbitrix-user-discounts-resolver) | 0.1.0 |  | User discount rules resolver for 1C-Bitrix |
| 2026-11-11 12:59:25 | [mailgatewayid/laravel](https://www.nuget.org/packages/mailgatewayid%2Flaravel) | v0.1.0 |  | Laravel mail transport for MailGateway.id (MAIL_MAILER=mailgateway) |
| 2026-11-11 13:14:52 | [jeromeborg/blade-starter-kit](https://www.nuget.org/packages/jeromeborg%2Fblade-starter-kit) | v1.0.0 |  | A minimal Laravel starter kit using Blade and Tailwind CSS: authentication, pro… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
