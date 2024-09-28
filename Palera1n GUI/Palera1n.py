import sys
import subprocess
import os

def run_palera1n(arguments):
    command = ["palera1n"] + arguments
    terminal_command = f"tell application \"Terminal\" to do script \"{' '.join(command)}; exit\""

    try:
        # Esegui il comando tramite AppleScript per aprire il Terminale esternamente
        subprocess.run(["osascript", "-e", terminal_command])
    except subprocess.CalledProcessError as e:
        print(f"Errore nell'esecuzione del comando nel terminale: {e}")
        
def main():
    if len(sys.argv) < 2:
        print("Errore: Devi specificare gli argomenti.")
        return

    args = sys.argv[1:]

    if args == ["-f", "-c"]:
        run_palera1n(["-f", "-c"])
    elif args == ["-f", "-B"]:
        run_palera1n(["-f", "-B"])
    elif args == ["-f"]:
        run_palera1n(["-f"])
    elif args == ["-l"]:
        run_palera1n(["-l"])
    elif args == ["-f", "--force-revert"]:
        run_palera1n(["-f", "--force-revert"])
    elif args == ["-l", "--force-revert"]:
        run_palera1n(["-l", "--force-revert"])
    elif args == ["-n"]:
        run_palera1n(["-n"])
    else:
        print("Errore: Argomenti non validi.")

if __name__ == "__main__":
    main()
