from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)


def main_menu():
    print("Welkom bij de Symetrische Encryptie en Decryptie App!")
    print("Welke functie wil je uitvoeren?")
    print("1. Encryptie")
    print("2. Decryptie")
    print("3. App verlaten")
    print()
    choice = int(input("Kies een optie 1-3: "))
    return choice


def encrypt():
    print("U heeft gekozen voor encryptie.")
    text = input("Voer nu de tekst in die u wilt versleutelen: ")
    print(f'De tekst die u heeft ingevoerd is: {text}')
    print("Deze tekst is nu versleuteld.")
    print(f'De versleutelde tekst is: {cipher.encrypt(text.encode())}')


def decrypt():
    print("U heeft gekozen voor decryptie.")
    text = input("Voer nu de versleutelde tekst in die u wilt ontsleutelenn: ")
    print(f'De versleutelde tekst die u heeft ingevoerd is: {text}')
    try:
        decrypted_message = cipher.decrypt(text.encode()).decode()
        print(f"De ontsleutelde tekst is: {decrypted_message}")
    except Exception as e:
        print(f"Er is een fout opgetreden tijdens het ontsleutelen: {e}")


if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            print("De app wordt nu afgsloten.")
            break
        else:
            print("Ongeldige keuze.")