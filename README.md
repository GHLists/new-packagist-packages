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

## Latest list — 2026-11-22 09:21 UTC

New packages created between 2026-11-22 08:20 UTC and 2026-11-22 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T09-21-08-911712Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 08:25:57 | [datacircle/openai-php-tools](https://www.nuget.org/packages/datacircle%2Fopenai-php-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four function tools for the OpenAI PHP client, for chat… |
| 2026-11-22 08:43:23 | [qiick/laravel-outbound](https://www.nuget.org/packages/qiick%2Flaravel-outbound) | v0.1.0 | Qiick | SSRF-safe outbound HTTP and Standard Webhooks signing for qiick Laravel product… |
| 2026-11-22 08:51:31 | [fiberphp/snowflake](https://www.nuget.org/packages/fiberphp%2Fsnowflake) | v0.1.0 | PangBin | ❄️ FiberPHP 雪花算法 ID 生成器 —— 64 位分布式唯一 ID，支持 Redis 租约自动分配 workerId、时钟回拨保护，零依赖。 |
| 2026-11-22 08:51:36 | [fiberphp/uuid](https://www.nuget.org/packages/fiberphp%2Fuuid) | v0.1.0 | PangBin | 🔢 FiberPHP UUID 组件 —— RFC 9562 规范，支持 v4 随机和 v7 时间排序生成，零依赖纯库。 |
| 2026-11-22 08:59:47 | [fiberphp/encryption](https://www.nuget.org/packages/fiberphp%2Fencryption) | v0.1.0 | PangBin | 🔐 FiberPHP 加密组件 —— AES-CBC/GCM 认证加密、bcrypt/argon2 密码哈希、HMAC 与 RSA 签名，零依赖纯库。 |
| 2026-11-22 08:59:56 | [fiberphp/encryption-gm](https://www.nuget.org/packages/fiberphp%2Fencryption-gm) | v0.1.0 | PangBin | 🛡️ FiberPHP 国密加密 —— SM3/SM4 算法实现，符合国密标准，零框架依赖。 |
| 2026-11-22 09:00:06 | [fiberphp/jwt](https://www.nuget.org/packages/fiberphp%2Fjwt) | v0.1.0 | PangBin | 🎟️ FiberPHP JWT 组件 —— JSON Web Token 编解码，支持 HS256/384/512 与 RS256/384/512，声明验证，… |
| 2026-11-22 09:01:10 | [meetmage/module-payment-script-guard](https://www.nuget.org/packages/meetmage%2Fmodule-payment-script-guard) | v1.0.0 | Meet Shekhat | PCI DSS 4.0.1 payment page script inventory (6.4.3) and tamper detection (11.6.… |
| 2026-11-22 09:02:22 | [courseexe/realtime](https://www.nuget.org/packages/courseexe%2Frealtime) | v1.0.0 | Courseexe; Projectsly AI | Official PHP Server Publisher SDK for Courseexe Realtime Channels |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
