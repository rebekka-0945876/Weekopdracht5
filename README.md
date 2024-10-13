
# Symmetrische Encryptie en Decryptie App

Deze Python-applicatie stelt gebruikers in staat om zowel tekst als bestanden te versleutelen en te ontsleutelen met behulp van symmetrische encryptie via de `cryptography`-bibliotheek. De app biedt de volgende functies:
- **Tekstversleuteling**: Voer een tekst in om deze te versleutelen en ontvang de versleutelde tekst.
- **Tekstontsleuteling**: Voer een versleutelde tekst in om de originele tekst te ontsleutelen.
- **Bestandsversleuteling**: Versleutel bestanden en sla ze op met een `.enc` extensie.
- **Bestandsontsleuteling**: Ontsleutel versleutelde bestanden en sla ze op met de toevoeging `_decrypted` aan de bestandsnaam.

## Installatie
1. Zorg ervoor dat Python is geïnstalleerd op je systeem.
2. Installeer de vereiste library door het volgende commando uit te voeren in de terminal:
   ```bash
   pip install cryptography
   ```

## Gebruik
1. Clone deze repository.
2. Start de applicatie door het volgende commando uit te voeren:
   ```bash
   python encryption.py
   ```
3. Volg de instructies op het scherm om tekst of bestanden te versleutelen of te ontsleutelen.

### Voorbeeldbestanden
Om de encryptie en decryptie van bestanden te testen, kun je gebruik maken van het meegeleverde `testfile.txt` bestand. Volg deze stappen:
1. Kies optie 3 om `testfile.txt` te versleutelen:
   - Voer de bestandsnaam `testfile.txt` in wanneer hierom gevraagd wordt.
   - Het versleutelde bestand wordt opgeslagen als `testfile.txt.enc`.
2. Kies optie 4 om het versleutelde bestand `testfile.txt.enc` te ontsleutelen:
   - Voer de bestandsnaam `testfile.txt.enc` in wanneer hierom gevraagd wordt.
   - Het ontsleutelde bestand wordt opgeslagen als `testfile_decrypted.txt`.

## Structuur van het project
- **encryption.py**: Hoofdbestand met de implementatie van de encryptie- en decryptielogica.
- **testfile.txt**: Een voorbeeldbestand om de bestandsencryptie en -decryptie te testen.

## Vereisten
- Python 3.x
- `cryptography` bibliotheek
