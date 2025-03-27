import getopt
import sys


PROMPT = ">>>"


def usage():
    print("用法:")
    print(f"    python3 {sys.argv[0]} [-h] [-p prompt]")
    print("")
    print("    -h, --help 显示本帮助")
    print("    -p, --prompt 设置提示符，默认为 >>>")
    print("")
    print("    输入 exit 退出交互，输入 help 显式本帮助，输入其他内容其他回显输入内容")
    print("")
    print("    输入 Ctrl-C 退出，另外")
    print("    - Windows 中输入 Ctrl+Z 并回车后退出")
    print("    - Linux 或 macOS 中输入 Ctrl+C 退出")
    print("")


def interactive():
    while True:
        try:
            line = input(f"{PROMPT} ")
            if line == "exit":
                exit()
            elif line == "help":
                usage()
            elif line == "":
                continue
            else:
                print(line)
        except EOFError:
            exit()
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print("发生错误: ", e)
            sys.exit(1)


def exit():
    print("Bye!")
    sys.exit(0)


def main():
    global PROMPT
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hp:', ['help', 'prompt='])
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                usage()
                sys.exit(0)
            elif opt in ('-p', '--prompt'):
                PROMPT = arg
            else:
                usage(f"未知参数: {opt}")
                sys.exit(1)
    except getopt.error as e:
        print("参数错误: ", e)
        usage()
        sys.exit(1)
    interactive()


if __name__ == "__main__":
    main()
