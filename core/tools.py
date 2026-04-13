import base64
import os
import sys

def get_input(prompt):
    return input(f"\033[96m[Oveliq Tools]\033[0m {prompt}")

def encrypt_data():
    data = get_input("Введіть текст для захисту: ")
    if not data: return
    # Просте шифрування Base64 (для стилю)
    encoded = base64.b64encode(data.encode()).decode()
    print(f"\033[92mЗашифровано:\033[0m {encoded}")
    
    save = get_input("Зберегти у файл vault.db? (y/n): ").lower()
    if save == 'y':
        with open("vault.db", "a") as f:
            f.write(encoded + "\n")
        print("\033[92mДані збережені.\033[0m")

def decrypt_data():
    data = get_input("Введіть зашифрований текст: ")
    if not data: return
    try:
        decoded = base64.b64decode(data.encode()).decode()
        print(f"\033[92mРозшифровано:\033[0m {decoded}")
    except Exception:
        print("\033[91mПомилка: Невірний формат шифру.\033[0m")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[94mOveliq Security Toolkit v1.0\033[0m")
    
    while True:
        print("\n1. Зашифрувати текст\n2. Розшифрувати текст\n3. Вихід")
        choice = input("\033[93mОберіть дію:\033[0m ")
        
        if choice == '1':
            encrypt_data()
        elif choice == '2':
            decrypt_data()
        elif choice == '3':
            print("Закриття інструментів...")
            break
        else:
            print("\033[91mНевірний вибір.\033[0m")

if __name__ == "__main__":
    main()
