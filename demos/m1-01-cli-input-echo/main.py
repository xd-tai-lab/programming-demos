import sys


def usage():
    print("用法:")
    print(f"   python3 {sys.argv[0]}")
    print("")
    print("    输入 exit 退出交互，输入 help 显式本帮助，输入其他内容其他回显输入内容")
    print("")
    print("    输入 Ctrl-C 退出，另外")
    print("    - Windows 中输入 Ctrl+Z 并回车后退出")
    print("    - Linux 或 macOS 中输入 Ctrl+C 退出")
    print("")


def exit():
    print("Bye!")
    sys.exit(0)


def main():
    while True:
        try:
            line = input(">>> ")
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


if __name__ == "__main__":
    main()
