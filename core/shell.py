import os

def start_shell():
    print("\033[94mOveliq Terminal v1.0.2\033[0m")
    print("Type 'help' to see available commands.")

    while True:
        cmd = input("\033[92moveliq@zantal\033[0m:~$ ").strip().lower()

        if cmd == "help":
            print("Commands: status, network, clear, whoami, exit")
        elif cmd == "status":
            print("CPU: 12% | RAM: 44% | Security: MAXIMUM")
        elif cmd == "whoami":
            print("User: Zantal | Role: Founder | Permissions: Root")
        elif cmd == "network":
            print("Connection: Encrypted via Oveliq-Bridge")
        elif cmd == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd == "exit":
            print("Closing session...")
            break
        elif cmd == "":
            continue
        else:
            print(f"Error: command '{cmd}' not found.")

if __name__ == "__main__":
    start_shell()
