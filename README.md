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

## Latest list — 2026-11-02 18:22 UTC

New packages created between 2026-11-02 17:20 UTC and 2026-11-02 18:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T18-22-50-204224Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 17:36:12 | [liberusoftware/real-estate-vr-design-api](https://www.nuget.org/packages/liberusoftware%2Freal-estate-vr-design-api) | 1.0.0 |  | Versioned API adapter for real-estate VR designs. |
| 2026-11-02 17:36:24 | [liberusoftware/real-estate-vr-design-livewire](https://www.nuget.org/packages/liberusoftware%2Freal-estate-vr-design-livewire) | 1.0.0 |  | Livewire VR property design studio. |
| 2026-11-02 17:40:56 | [janalis/porta-assist](https://www.nuget.org/packages/janalis%2Fporta-assist) | v0.1.1 |  | Work on one project together, live: a host shares it over the network, guests j… |
| 2026-11-02 17:42:34 | [pdftoolkit/html-to-pdf](https://www.nuget.org/packages/pdftoolkit%2Fhtml-to-pdf) | v0.1.0 | Mathias STRASSER | Object-oriented HTML and CSS pagination to tagged PDF in native PHP |
| 2026-11-02 17:49:25 | [balt1794/contao-alt-text-generator-ai](https://www.nuget.org/packages/balt1794%2Fcontao-alt-text-generator-ai) | 1.0.0 | Bryam Loaiza | Write SEO-friendly alt text for the images in your Contao file manager with AI,… |
| 2026-11-02 18:08:05 | [damconsultants/tectake](https://www.nuget.org/packages/damconsultants%2Ftectake) | 1.0.0 | DamConsultants | DamConsultants Tectake for Magento 2 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
