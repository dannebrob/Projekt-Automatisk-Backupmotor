import os
import shutil
from datetime import datetime

# 1. Hämta aktuell arbetsmapp
Current_Working_Directory = os.getcwd()


# 2. Ange källmapp och backupmapp
Source_Folder = Current_Working_Directory
Backup_Root = os.path.join(Current_Working_Directory, "backups")
Exclude_Files = ["script.py", "backups"]

# Hämta alla filer i källmappen
source_files = os.listdir(Source_Folder)

# 3. Skapa backupmapp med tidsstämpel
Timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
Backup_Folder = os.path.join(Backup_Root, f"backup_{Timestamp}")

# 4. Skapa loggfil
Log_File = os.path.join(Backup_Folder, "backup_log.txt")
os.makedirs(Backup_Folder, exist_ok=True)

# 5. Loopa igenom alla filer i källmappen
for file in source_files:
  
  # 6. Kontrollera att det är en fil eller mapp och inte i exkluderingslistan
  if os.path.isfile(file) or os.path.isdir(file) == True and file not in Exclude_Files:
    print(f"Backing up file: {file}")
    # 7. Kopiera filen eller mappen till backupmappen
    shutil.copytree(file, os.path.join(Backup_Folder, file)) if os.path.isdir(file) else shutil.copy2(file, Backup_Folder)
    # 8. Skriv till loggfilen
    with open(Log_File, "a") as log:
      log.write(f"Backed up: {file} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Backed up: {file}")
  else:
    print(f"Skipping non-file/non-directory: {file}")
    # 9. Skriv till loggfilen för hoppade filer
    with open(Log_File, "a") as log:
      log.write(f"Skipped: {file} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    continue
print("Backup completed.")
# 10. Avsluta scriptet
exit(0)

# KLART
