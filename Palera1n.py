import sys
import subprocess
import platform
import shutil

def is_macos():
    return platform.system() == "Darwin"

def is_linux():
    return platform.system() == "Linux"

def get_terminal_command(command):
    if is_macos():
        # AppleScript to open Terminal on macOS
        return ["osascript", "-e", f'tell application "Terminal" to do script "{command}; exit"']
    elif is_linux():
        # Try common Linux terminals
        terminals = ["gnome-terminal", "konsole", "xfce4-terminal", "x-terminal-emulator", "xterm"]
        for term in terminals:
            if shutil.which(term):
                return [term, "--", "bash", "-c", f"{command}; exec bash"]
        raise RuntimeError("No supported terminal found on this system.")
    else:
        raise RuntimeError("Unsupported operating system.")

def run_palera1n(arguments):
    command = ["palera1n"] + arguments
    full_command = ' '.join(command)

    try:
        terminal_cmd = get_terminal_command(full_command)
        subprocess.run(terminal_cmd)
    except Exception as e:
        print(f"Error launching command in terminal: {e}")

def main():
    if len(sys.argv) < 2:
        print("Error: You must specify arguments.")
        return

    args = sys.argv[1:]
    valid_args = [
        ["-f", "-c"],
        ["-f", "-B"],
        ["-f"],
        ["-l"],
        ["-f", "--force-revert"],
        ["-l", "--force-revert"],
        ["-n"],
    ]

    if args in valid_args:
        run_palera1n(args)
    else:
        print("Error: Invalid arguments.")

if __name__ == "__main__":
    main()
