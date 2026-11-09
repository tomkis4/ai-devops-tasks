1. Jak działa skrypt?
Skrypt komunikuje się z Jenkins przez REST API. Pozwala wykonać trzy operacje:

Listowanie zadań – pobiera wszystkie zadania z serwera Jenkins.

Sprawdzanie statusu buildów – sprawdza wynik ostatniego uruchomienia zadania.

Uruchamianie zadania – wysyła żądanie do Jenkins, aby rozpocząć nowy build.

2. Wykorzystane biblioteki
Biblioteka

Zastosowanie

requests

Wysyłanie zapytań HTTP do Jenkins API.

requests.auth.HTTPBasicAuth

Obsługa autoryzacji użytkownika i tokenu API.

os

Odczytywanie zmiennych środowiskowych.

Biblioteki os i requests.auth są częścią odpowiednio standardowej biblioteki Pythona i pakietu requests.

3. Jak działa komunikacja z Jenkins API?
Skrypt wykorzystuje trzy główne endpointy:

Endpoint

Działanie

/api/json

Pobiera listę zadań.

/job/NAZWA/lastBuild/api/json

Pobiera informacje o ostatnim buildzie.

/job/NAZWA/build

Uruchamia nowe zadanie.

Do komunikacji używane są metody HTTP:

GET – pobieranie danych.

POST – uruchamianie zadania.

4. Przykładowe polecenia
Krok 1. Instalacja biblioteki


bash
pip install requests
Krok 2. Konfiguracja Jenkins

Linux / macOS:


bash
export JENKINS_URL="http://localhost:8080"
export JENKINS_USER="admin"
export JENKINS_TOKEN="twoj_token"
Windows PowerShell:


powershell
$env:JENKINS_URL="http://localhost:8080"
$env:JENKINS_USER="admin"
$env:JENKINS_TOKEN="twoj_token"
Krok 3. Uruchomienie skryptu


bash
python jenkins_api.py
Krok 4. Wybór operacji

Przykładowy ekran:


text
1. Lista zadań
2. Status ostatniego buildu
3. Uruchom zadanie

Wybierz opcję: 1
Przykładowy wynik:


text
--- Lista zadań Jenkins ---
Nazwa: myapp
Status: blue
URL: http://localhost:8080/job/myapp/
Sprawdzenie statusu buildu:


text
Wybierz opcję: 2
Podaj nazwę zadania: myapp
Uruchomienie zadania:


text
Wybierz opcję: 3
Podaj nazwę zadania: myapp
5. Obsługa błędów
Skrypt wykorzystuje mechanizm try-except, który pozwala obsłużyć:

401 – brak poprawnej autoryzacji.

403 – brak odpowiednich uprawnień.

404 – nie znaleziono zasobu.

ConnectionError – problem z połączeniem.

Timeout – przekroczony czas oczekiwania.

Ważne: Warto dodatkowo rozbudować skrypt o obsługę CSRF crumb, jeśli Jenkins wymaga go przy żądaniach POST.

6. Podsumowanie
Skrypt automatyzuje podstawowe operacje administracyjne w Jenkinsie. Dzięki bibliotece requests można komunikować się z Jenkins API bezpośrednio z poziomu Pythona, bez konieczności korzystania z przeglądarki.