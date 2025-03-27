import getopt
import os
import select
import sys
import time


PROMPT = ">>>"
BREAK_TIME_SECONDS = 2

input_echo_enabled = True

if os.name == "nt":
    EOFValue = 0x1A      # Ctrl+Z

    import msvcrt
    import ctypes
    import ctypes.wintypes


    def get_terminal_settings():
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-10)     # STD_INPUT_HANDLE
        mode = ctypes.wintypes.DWORD()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        return mode.value


    def disable_input_echo():
        global input_echo_enabled
        input_echo_enabled = False
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-10)     # STD_INPUT_HANDLE

        mode = ctypes.wintypes.DWORD()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))

        new_mode = mode.value & ~0x0004
        kernel32.SetConsoleMode(handle, new_mode)

        return mode.value


    def enable_input_echo(old_mode):
        global input_echo_enabled
        input_echo_enabled = True
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-10)
        kernel32.SetConsoleMode(handle, old_mode)


    def keyboard_producer() -> str | None:
        if msvcrt.kbhit():
            char = msvcrt.getch().decode("utf-8")
            return char
        return None

elif os.name == "posix":
    EOFValue = 0x04      # Ctrl+D

    import tty
    import termios


    def get_terminal_settings():
        fd = sys.stdin.fileno()
        settings = termios.tcgetattr(fd)
        return settings

    def disable_input_echo():
        global input_echo_enabled
        input_echo_enabled = False
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(fd)
        return old_settings


    def enable_input_echo(old_settings):
        global input_echo_enabled
        input_echo_enabled = True
        fd = sys.stdin.fileno()
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


    def keyboard_producer() -> str | None:
        if select.select([sys.stdin], [], [], 0)[0]:
            char = sys.stdin.read(1)
            if char == "":
                raise EOFError
            return char
        return None

def main_processing():
    origin_settings = get_terminal_settings()
    try:
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
                    old_settings = disable_input_echo()
                    print(line)
                    if os.name == "posix":
                        print("\r", end="")
                    print(f"等待 {BREAK_TIME_SECONDS} 秒...期间的输入将被忽略")
                    if os.name == "posix":
                        print("\r", end="")
                    time.sleep(BREAK_TIME_SECONDS)

                    # 在输出 prompt 之前，吞掉之前所有的输入
                    while True:
                        c = keyboard_producer()
                        if not c:        # 没有按键输入
                            break
                        if ord(c) == EOFValue:
                            raise EOFError 
                    enable_input_echo(old_settings)
            except EOFError:
                exit()
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print("发生错误: ", e)
                sys.exit(1)
    finally:
        ## 有异常发生时，恢复终端设置
        enable_input_echo(origin_settings)


def usage():
    print("用法:")
    print(f"    python3 {sys.argv[0]} [-h] [-p prompt] [-b number]")
    print("")
    print("    -h, --help 显示本帮助")
    print("    -p, --prompt 设置提示符，默认为 >>>")
    print("    -b, --break 设置等待时间，默认为 2 秒")
    print("")
    print("    输入 Ctrl-C 退出，另外")
    print("    - Windows 中输入 Ctrl+Z 并回车后退出")
    print("    - Linux 或 macOS 中输入 Ctrl+C 退出")
    print("")


def exit():
    print("Bye!")
    sys.exit(0)


def main():
    global PROMPT, BREAK_TIME_SECONDS
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'b:hp:', ['break', 'help', 'prompt='])
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                usage()
                sys.exit(0)
            elif opt in ('-p', '--prompt'):
                PROMPT = arg
            elif opt in ('-b', '--break'):
                BREAK_TIME_SECONDS = int(arg)
            else:
                usage(f"未知参数: {opt}")
                sys.exit(1)
    except getopt.error as e:
        print("参数错误: ", e)
        usage()
        sys.exit(1)

    main_processing()


if __name__ == "__main__":
    main()
