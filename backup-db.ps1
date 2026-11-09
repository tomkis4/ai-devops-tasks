
# Prosty skrypt do backupu bazy danych

$DB_NAME = "app_database"
$BACKUP_DIR = "C:\Backups\db"
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
$FILENAME = "$BACKUP_DIR\$($DB_NAME)_$DATE.sql.gz"

# Sprawdź czy katalog istnieje
if (!(Test-Path $BACKUP_DIR)) {
    New-Item -ItemType Directory -Path $BACKUP_DIR -Force
    Write-Host "Utworzono katalog $BACKUP_DIR"
}

# Wykonaj backup
Write-Host "Rozpoczynam backup bazy $DB_NAME..."

mysqldump -u root -p $DB_NAME | gzip.exe > $FILENAME

if ($LASTEXITCODE -eq 0) {
    Write-Host "Backup zakończony sukcesem: $FILENAME"
} else {
    Write-Host "Błąd podczas wykonywania backupu!"
    exit 1
}
