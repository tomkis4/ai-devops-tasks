Bash                         PowerShell

mkdir -p                     New-Item -ItemType Directory
date                         Get-Date
echo                         Write-Host
$?                           $LASTEXITCODE
[ ! -d "$DIR" ]              !(Test-Path $DIR)