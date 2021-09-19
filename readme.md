# SwitchProxy-Rules

## 说明

本项目Forked from  [Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)  因为原作者h2y已宣布终止其后续维护，为了方便个人使用，所以有了本项目。

本项目初衷只是个人使用，因为方便部署，所以将其设置为 public ，如果你有使用的需求，可以结合自身的情况 Fork 源项目。

### 特征

这里是一系列好用的~~翻墙规则~~ 回国规则，针对 [Shadowrocket](https://liguangming.com/Shadowrocket) 开发，支持广告过滤。

规则定义了哪些网站可以直连，哪些必须走代理，规则是一个纯文本文件，并不提供代理服务器。使用 Python 按照一定的规则和模板定期自动生成，并且使用开源的力量，集众人之力逐渐完善。

**本规则具有以下特点：**

- 黑名单由最新版 GFWList 自动转换；白名单针对全球 top500 站点的连通情况定期自动生成。
- 自动转换最新版本的 `EasyList, Eaylist China, 乘风规则, CJX’sAnnoyance, 以及补充的一些规则 ` 为 Shadowrocket 规则，全面去除广告。
- 也包括自定义的广告过滤规则，针对 iOS 端的网页广告、App 广告和视频广告。（[常见广告过滤效果统计](https://github.com/h2y/Shadowrocket-ADBlock-Rules/issues/40)）
- 提供2个规则文件，均包含`.cn` 域名和常见国内流媒体的代理设置。

### 后续计划

- 规则会以季度为单位进行更新。
- 除去Shadowrocket，后续为了方便个人使用，可能增加包括不限于Clash for Windows等软件的支持。
- 如有余力，可能会在逐渐恢复更新源项目中的其他配置。

### 鸣谢

- 原始构建 [h2y](https://github.com/h2y)
- StreamingCN.list 提取自 DivineEngine 规则
- ad.list 规则来自 [o0HalfLife0o](https://github.com/o0HalfLife0o/list)
- 以及其他来自贡献库的朋友们

## 使用方法

在 ShadowRocket 应用中，进入 [配置] 页面，点击 `扫描[左上角]` 或 `添加[右上角]` 按钮添加规则。再激活添加的规则文件即可。

最好让 ShadowRocket 断开并重新连接一次，以确保新的规则文件生效。 

### 回国规则

- 直连：国外网站
- 代理：中国网站 + 国内常见流媒体
- 不包含广告过滤

规则地址：

```
https://github.com/Wolfsin/SwitchProxy-Rules/raw/master/Shadowrocket_backcn.conf
```

### 回国规则 + 广告过滤

- 直连：国外网站
- 代理：中国网站 + 国内常见流媒体
- 包含广告过滤

规则地址：

```
https://github.com/Wolfsin/SwitchProxy-Rules/raw/master/Shadowrocket_backcn_ad.conf
```

## 问题反馈

任何问题欢迎在 [Issues](https://github.com/Wolfsin/SwitchProxy-Rules/issues) 中反馈，因为初衷只是个人使用，可能无法让所有人满意。

如果你有更好的规则，欢迎提交。

**一般情况**

对 [factory 目录](https://github.com/Wolfsin/SwitchProxy-Rules/tree/master/factory) 下的 3 个 `manual_*.txt` 文件做对应修改即可。

**国内流媒体**

对 [resultant 目录](https://github.com/Wolfsin/SwitchProxy-Rules/tree/master/factory/resultant) 下的`StreamingCN.list` 文件做对应修改即可。