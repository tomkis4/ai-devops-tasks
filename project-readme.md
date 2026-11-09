Simple Task API
1. Opis

Simple Task API to REST API do zarządzania zadaniami, stworzone przy użyciu:

Node.js
Express.js
MongoDB
Główne funkcje
Tworzenie, odczytywanie, aktualizacja i usuwanie zadań (CRUD).
Filtrowanie zadań według statusu i priorytetu.
Prosta autoryzacja użytkowników.
2. Instalacja
Sklonuj repozytorium:
bash
git clone https://github.com/username/simple-task-api.git

Przejdź do folderu projektu:
bash
cd simple-task-api

Zainstaluj zależności:
bash
npm install

Utwórz plik .env:
env
PORT=3000
MONGO_URI=mongodb://localhost:27017/tasks
JWT_SECRET=your_secret_key

Uruchom aplikację:
bash
npm start

3. Użycie

API domyślnie działa pod adresem:

text
http://localhost:3000


Przykładowe żądanie pobierające zadania:

bash
curl http://localhost:3000/api/tasks

4. Endpointy API
Metoda	Endpoint	Opis
GET	/api/tasks	Pobieranie wszystkich zadań
GET	/api/tasks/:id	Pobieranie zadania po ID
POST	/api/tasks	Tworzenie zadania
PUT	/api/tasks/:id	Aktualizacja zadania
DELETE	/api/tasks/:id	Usuwanie zadania
POST	/api/auth/register	Rejestracja użytkownika
POST	/api/auth/login	Logowanie użytkownika
Filtrowanie zadań

Można filtrować zadania według statusu i priorytetu:

text
GET /api/tasks?status=completed&priority=high

Przykładowe dane zadania
json
{
  "title": "Nauka Node.js",
  "description": "Poznanie Express",
  "status": "pending",
  "priority": "high"
}

5. Technologie
Node.js – środowisko uruchomieniowe.
Express – obsługa API.
MongoDB – baza danych.
JWT – autoryzacja użytkowników.

Simple Task API – prosty system zarządzania zadaniami.