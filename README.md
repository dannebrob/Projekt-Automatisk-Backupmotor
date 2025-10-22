# Projekt Automatisk Backupmotor

Detta projekt är en enkel Python-baserad backupmotor som automatiskt skapar säkerhetskopior av filer och mappar i en angiven källmapp till en backupmapp med tidsstämplar. Scriptet kan anpassas för att exkludera specifika filer eller mappar från backupen.

## Funktioner
- Skapar en backupmapp med en tidsstämpel för varje körning.
- Kopierar alla filer och mappar från källmappen till backupmappen.
- Möjlighet att exkludera specifika filer eller mappar från backupen.
- Enkel att använda och anpassa.
## Användning
1. Installera Python om det inte redan är installerat.
2. Klona eller ladda ner detta repository.
3. Anpassa `Source_Folder`, `Backup_Root` och `Exclude_Files` variablerna i `script.py` efter dina behov.
4. Kör scriptet med kommandot `python script.py`.
5. Backupen skapas i den angivna backupmappen med en tidsstämpel.
## Krav
- Python 3.x
- Standardbibliotek: os, shutil, datetime
## Licens
Detta projekt är licensierat under MIT-licensen. Se LICENSE-filen för mer information.

# Vad jag lärt mig
I detta projekt har jag lärt mig att:
- Använda Python för filhantering och kataloghantering.
- Skapa tidsstämplar med hjälp av datetime-biblioteket.
- Använda shutil-biblioteket för att kopiera filer och mappar.
- Implementera exkluderingslogik för att undvika att vissa filer eller mappar inkluderas i backupen.

# Tack för att du använder detta projekt! Om du har några frågor eller förslag, tveka inte att kontakta mig.