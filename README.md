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

## Latest list — 2026-11-14 13:19 UTC

New packages created between 2026-11-14 12:20 UTC and 2026-11-14 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T13-19-41-293296Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 12:21:03 | [tacman/opencv-php](https://www.nuget.org/packages/tacman%2Fopencv-php) | 0.1.0 |  | PHP bindings for OpenCV 5, generated from OpenCV's own header annotations |
| 2026-11-14 12:37:54 | [tavy315/sylius-two-factor-plugin](https://www.nuget.org/packages/tavy315%2Fsylius-two-factor-plugin) | v0.1 |  | Two-factor authentication for Sylius administrators and shop users. |
| 2026-11-14 12:39:09 | [sandritsch91/yii2-widget-yad](https://www.nuget.org/packages/sandritsch91%2Fyii2-widget-yad) | 1.0.0 | Sandritsch91 | Yii2 input widget for yad (Yet Another Datepicker): a dependency-free date, dat… |
| 2026-11-14 12:48:41 | [lornequinn/blog-core](https://www.nuget.org/packages/lornequinn%2Fblog-core) | v0.1.0 | Lorne Quinn | Core package for the LQ blog suite — Post, Tag, DataType registry, Component re… |
| 2026-11-14 12:48:41 | [lornequinn/blog-markdown](https://www.nuget.org/packages/lornequinn%2Fblog-markdown) | v0.1.0 | Lorne Quinn | Markdown body renderer for the LQ blog suite — CommonMark-backed pre-pass on th… |
| 2026-11-14 12:48:41 | [lornequinn/blog-mcp](https://www.nuget.org/packages/lornequinn%2Fblog-mcp) | v0.1.0 | Lorne Quinn | MCP server tools for the LQ blog suite — the editor surface. No web admin. |
| 2026-11-14 12:57:57 | [jdecool/scaleway-runtime](https://www.nuget.org/packages/jdecool%2Fscaleway-runtime) | v0.1.0 | Jeremy Decool | Symfony Runtime to run PHP applications on Scaleway Serverless Functions |
| 2026-11-14 13:07:32 | [ryckakas/fsum](https://www.nuget.org/packages/ryckakas%2Ffsum) | v0.1.0 | Ricardas Kauneckas | Exact, correctly rounded float summation for PHP: JavaScript Math.sumPrecise se… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
