# Python 编程示例代码

## 目录结构

在 `demos` 目录中，以 `<期>-<编号>-<标题>` 的格式存放示例代码。其中：

```text
.
├── demos/
│   ├── common/                 # 公共代码
│   └── m1-01-cli-input-echo/   # 最简单的交互式命令行
│   ├── m1-02-cli-getopt/       # 使用 `getopt` 模块解析命令行参数
│   ├── m1-03-cli-interactive/  # 命令行界面交互式的扫雷游戏
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
