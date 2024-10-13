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
    # put encryption code here
    text = input("Voer nu de tekst in die u wilt versleutelen: ")
    print(f'De tekst die u heeft ingevoerd is: {text}')
    print("Deze tekst is nu versleuteld.")


def decrypt():
    print("U heeft gekozen voor decryptie.")
    # put decryption code here
    text = input("Voer nu de versleutelde tekst in die u wilt ontsleutelenn: ")
    print(f'De versleutelde tekst die u heeft ingevoerd is: {text}')
    print("Deze tekst is nu ontsleuteld.")
