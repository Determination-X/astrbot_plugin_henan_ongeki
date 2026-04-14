# astrbot-plugin-henan-ongeki

AstrBot 河南音击插件

这是一个简单的 AstrBot 插件，用于根据用户输入随机返回河南音击图片。

## 功能

- 支持命令：`/河南音击`、`/河南音擊`
- 支持纯文本触发：`河南音击`、`河南音擊`
- 随机返回 `data/plugin_data/henan_ongeki/images/1.jpg` 至 `44.jpg` 中的一张图片

## 安装

1. 将 `astrbot_plugin_henan_ongeki` 目录放入 AstrBot 的 `data/plugins/` 下。
2. 确保插件目录包含 `main.py`、`metadata.yaml`、`README.md` 等文件。
3. 启动 AstrBot，插件将自动加载；或在 AstrBot 内重新加载插件。

## 使用

- 发送命令：`/河南音击` 或 `/河南音擊`
- 或直接发送消息：`河南音击` / `河南音擊`

当消息内容与命令词相等时，插件会返回一张随机河南音击图片。

## 相关链接
河南音击资源：
- [MMFC随机音击](https://mmfc.majdata.net/)
