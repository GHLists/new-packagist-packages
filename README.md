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

## Latest list — 2026-11-15 03:19 UTC

New packages created between 2026-11-15 02:21 UTC and 2026-11-15 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T03-19-30-556552Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 02:23:49 | [lowelllab/hyperf-dpop](https://www.nuget.org/packages/lowelllab%2Fhyperf-dpop) | v0.2.1 |  | Hyperf integration for strict DPoP authentication, nonce and atomic replay prot… |
| 2026-11-15 02:31:32 | [nowo-tech/transaction-contract](https://www.nuget.org/packages/nowo-tech%2Ftransaction-contract) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Framework-free transaction port: TransactionRunnerInterface::run(callable) and… |
| 2026-11-15 02:39:39 | [configdirector/server-sdk](https://www.nuget.org/packages/configdirector%2Fserver-sdk) | v0.1.0 | ConfigDirector | PHP server SDK for ConfigDirector. ConfigDirector is a remote configuration and… |
| 2026-11-15 02:44:49 | [nowo-tech/transaction-doctrine](https://www.nuget.org/packages/nowo-tech%2Ftransaction-doctrine) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Safe plain-Doctrine default for nowo-tech/transaction-contract: a one-attempt T… |
| 2026-11-15 03:15:00 | [zydbkqf/ext-onnxruntime](https://www.nuget.org/packages/zydbkqf%2Fext-onnxruntime) | 0.4.7 | Denis Cheung | Native ONNX Runtime inference for PHP: Tensor conversion, I/O Binding, async ta… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
