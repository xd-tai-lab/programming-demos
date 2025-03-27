# Python 编程示例代码

## 目录结构

在 `demos` 目录中，以 `<期>-<编号>-<标题>` 的格式存放示例代码。其中：

```text
.
├── demos/
│   ├── common/                 # 公共代码
│   └── m1-01-cli-input-echo/   # 最简单的交互式命令行
│   ├── m1-02-cli-getopt/       # 使用 `getopt` 模块解析命令行参数
│   ├── m1-03-cli-interactive/  # 非阻塞式命令行界面交互示例
```

## 运行方式

- Windows: 使用 `cmd` 或 `powershell`
- Linux: 使用 `bash` 或 `zsh`
- MacOS: 使用 `终端` 或 `iTerm2`

如：


`cd` 到示例代码所在目录，然后运行直接运行。如：

```shell
python3 demos/m1-01-cli-input-echo/main.py
```

## Demos

### [m1-01-cli-input-echo](demos/m1-01-cli-input-echo/README.md)

最简单的交互式命令行，输入 `exit` 退出，输入 `help` 显示帮助，输入其他内容回显输入内容

### [m1-02-cli-getopt](demos/m1-02-cli-getopt/README.md)

在 [m1-01-cli-input-echo](demos/m1-01-cli-input-echo/README.md) 的基础上，使用 `getopt` 模块解析命令行参数

### [m1-03-cli-interactive](demos/m1-03-cli-interactive/README.md)

非阻塞式命令行界面交互示例

该示例演示了通过短期内把终端设置成非阻塞模式，以忽略在等待期间内的按键输入，从而实现非阻塞式命令行界面交互。

非阻塞 IO 通常还会配合其他技术，如 `select`、`poll`、`epoll`、`kqueue` 等，以实现定制化的和更高效的 IO 处理。

本示例的重点在于理解非阻塞 IO、输入回显的概念，用于在命令行界面中模拟各 AI 平台的聊天界面在 AI 输出时禁止输入的效果。

当非阻塞 IO 具体用于终端、网络套接字（socket）、文件等 IO 操作时，在不同操作系统上的实现方式可能有所不同，所以这本身并不是重点。
