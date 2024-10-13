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
    print("1. Encryptie van tekst")
    print("2. Decryptie van tekst")
    print("3. Encryptie van bestand")
    print("4. Decryptie van bestand")
    print("5. App verlaten")
    print()
    choice = int(input("Kies een optie 1-5: "))
    return choice


def encrypt_text():
    print("\nU heeft gekozen voor encryptie.")
    text = input("Voer nu de tekst in die u wilt versleutelen: ")
    print(f'De tekst die u heeft ingevoerd is: {text}')
    encrypted_message = cipher.encrypt(text.encode()).decode()
    print("Deze tekst is nu versleuteld.")
    print(f'De versleutelde tekst is: {encrypted_message}')


def decrypt_text():
    print("\nU heeft gekozen voor decryptie.")
    text = input("Voer nu de versleutelde tekst in die u wilt ontsleutelen: ")
    print(f'De versleutelde tekst die u heeft ingevoerd is: {text}')
    try:
        decrypted_message = cipher.decrypt(text.encode()).decode()
        print(f"De ontsleutelde tekst is: {decrypted_message}")
    except Exception as e:
        print(f"Er is een fout opgetreden tijdens het ontsleutelen: {e}")


def encrypt_file():
    print("\nU heeft gekozen voor encryptie van een bestand.")
    file_path = input("Voer het pad van het bestand in dat u wilt versleutelen: ")
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = cipher.encrypt(file_data)
        with open(file_path + ".enc", "wb") as file:
            file.write(encrypted_data)
        print(f"Het bestand is versleuteld en opgeslagen als: {file_path}.enc")
    except Exception as e:
        print(f"Er is een fout opgetreden tijdens het versleutelen van het bestand: {e}")


def decrypt_file():
    print("\nU heeft gekozen voor decryptie van een bestand.")
    file_path = input("Voer het pad van het versleutelde bestand in dat u wilt ontsleutelen: ")
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
        new_file_path = file_path.replace(".enc", "_decrypted")
        with open(new_file_path, "wb") as file:
            file.write(decrypted_data)
        print(f"Het bestand is ontsleuteld en opgeslagen als: {new_file_path}")
    except Exception as e:
        print(f"Er is een fout opgetreden tijdens het ontsleutelen van het bestand: {e}")


if __name__ == "__main__":
    print("Welkom bij de Symetrische Encryptie en Decryptie App!")
    while True:
        choice = main_menu()
        if choice == 1:
            encrypt_text()
        elif choice == 2:
            decrypt_text()
        elif choice == 3:
            encrypt_file()
        elif choice == 4:
            decrypt_file()
        elif choice == 5:
            print("De app wordt nu afgesloten.")
            break
        else:
            print("Ongeldige keuze.")
