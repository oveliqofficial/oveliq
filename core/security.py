import base64

def encrypt_data(data):
    # Просте шифрування для демонстрації
    encoded = base64.b64encode(data.encode())
    return encoded

print("Oveliq Security Module Loaded...")
text = input("Enter secret message: ")
print(f"Encrypted: {encrypt_data(text)}")
