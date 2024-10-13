from cryptography.fernet import Fernet
import os


def load_or_generate_key():
    if os.path.exists("secret.key"):
        print("Sleutelbestand gevonden, laden...")
        try:
            with open("secret.key", "rb") as key_file:
                key = key_file.read()
                print("Sleutel succesvol geladen.")
                return key
        except Exception as e:
            print(f"Er is een fout opgetreden bij het laden van de sleutel: {e}")
    else:
        print("Geen sleutelbestand gevonden, nieuwe sleutel genereren...")
        key = Fernet.generate_key()
        try:
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
                print("Nieuwe sleutel succesvol opgeslagen.")
        except Exception as e:
            print(f"Er is een fout opgetreden bij het opslaan van de sleutel: {e}")
        return key


key = load_or_generate_key()
cipher = Fernet(key)


def main_menu():
    print("Welke functie wilt u  uitvoeren?")
    print("1. Encryptie")
    print("2. Decryptie")
    print("3. App verlaten")
    print()
    choice = int(input("Kies een optie 1-3: "))
    return choice


def encrypt():
    print("\nU heeft gekozen voor encryptie.")
    text = input("Voer nu de tekst in die u wilt versleutelen: ")
    print(f'De tekst die u heeft ingevoerd is: {text}')
    encrypted_message = cipher.encrypt(text.encode()).decode()
    print("Deze tekst is nu versleuteld.")
    print(f'De versleutelde tekst is: {encrypted_message}')


def decrypt():
    print("\nU heeft gekozen voor decryptie.")
    text = input("Voer nu de versleutelde tekst in die u wilt ontsleutelen: ")
    print(f'De versleutelde tekst die u heeft ingevoerd is: {text}')
    try:
        decrypted_message = cipher.decrypt(text.encode()).decode()
        print(f"De ontsleutelde tekst is: {decrypted_message}")
    except Exception as e:
        print(f"Er is een fout opgetreden tijdens het ontsleutelen: {e}")


if __name__ == "__main__":
    print("Welkom bij de Symetrische Encryptie en Decryptie App!")
    while True:
        choice = main_menu()
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            print("De app wordt nu afgesloten.")
            break
        else:
            print("Ongeldige keuze.")
