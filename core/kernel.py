import time
import sys

def boot_sequence():
    print("\033[94m[OVELIQ]\033[0m Initializing System...")
    time.sleep(1)
    
    tasks = ["Loading Drivers", "Establishing Secure Bridge", "Mounting Filesystem"]
    for task in tasks:
        print(f" > {task}...", end="\r")
        time.sleep(0.7)
        print(f" [ OK ] {task}          ")

    print("-" * 30)
    print("\033[91mACCESS RESTRICTED\033[0m")
    
    password = input("ENTER ACCESS KEY: ")
    
    if password == "zantal2026":  # Твій пароль (можеш змінити)
        print("\033[92mACCESS GRANTED\033[0m")
        time.sleep(1)
        print("Welcome back, Zantal.")
    else:
        print("\033[91mACCESS DENIED. SYSTEM LOCKED.\033[0m")
        sys.exit()

if __name__ == "__main__":
    boot_sequence()
