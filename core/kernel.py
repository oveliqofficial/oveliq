import time
import sys
import os

# Функція для ефекту друку тексту
def type_effect(text, speed=0.03, color="\033[92m"):
    reset = "\033[0m"
    for char in text:
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Анімований індикатор завантаження
def loading_bar(duration=3):
    print("\033[94m[OVELIQ BOOT]\033[0m ", end="")
    for _ in range(20):
        time.sleep(duration / 20)
        sys.stdout.write("█")
        sys.stdout.flush()
    print(" [ COMPLETE ]")

def boot_sequence():
    # Очищення екрану (працює на Windows та Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Логотип Oveliq
    logo = """
    \033[96m
       ___              _ _       
      / _ \__   _____  | (_) __ _ 
     | | | \ \ / / _ \ | | |/ _` |
     | |_| |\ V /  __/ | | | (_| |
      \___/  \_/ \___| |_|_|\__, |
                             |___/ 
    \033[0m
    """
    print(logo)
    type_effect(">>> Oveliq Kernel v2.1.0 Initializing...", speed=0.02, color="\033[94m")
    time.sleep(1)
    
    # Симуляція завантаження модулів
    modules = ["Security Core", "Network Bridge", "FileSystem Auth", "UI Engine"]
    for module in modules:
        type_effect(f" > Loading {module}...", speed=0.01)
        time.sleep(0.5)
    
    loading_bar()
    print("-" * 40)
    
    # Система авторизації
    type_effect("CRITICAL ACCESS REQUIRED.", speed=0.05, color="\033[91m")
    
    # Пароль за замовчуванням (зміни його!)
    correct_key = "zantal2026" 
    
    for attempt in range(3):
        access_key = input("\033[93mENTER ACCESS KEY:\033[0m ")
        if access_key == correct_key:
            type_effect("\nACCESS GRANTED. Welcome, Founder Zantal.", color="\033[92m")
            time.sleep(1)
            # Тут можна викликати shell.py, якщо він в тій же папці
            # import shell
            # shell.start_shell()
            return True
        else:
            print(f"\033[91mINVALID KEY. Attempts left: {2 - attempt}\033[0m")
    
    type_effect("\nSYSTEM LOCKED. TERMINATING SESSION.", speed=0.05, color="\033[41m\033[97m")
    time.sleep(2)
    sys.exit()

if __name__ == "__main__":
    boot_sequence()
