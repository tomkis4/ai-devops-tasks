GET /api/users
Opis

Endpoint zwraca listę użytkowników z możliwością filtrowania według roli oraz stronicowania wyników.

Parametry zapytania
Parametr	Typ	Domyślna wartość	Opis
page	Integer	1	Numer strony
limit	Integer	10	Liczba wyników na stronę (maks. 100)
role	String	Brak	Opcjonalny filtr według roli użytkownika
Przykładowe żądanie
http
GET /api/users?page=1&limit=10&role=admin

Przykładowa odpowiedź

Status: 200 OK

json
{
  "users": [
    {
      "id": 1,
      "name": "Jan Kowalski",
      "email": "jan@example.com",
      "role": "admin"
    },
    {
      "id": 2,
      "name": "Anna Nowak",
      "email": "anna@example.com",
      "role": "admin"
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 2
}

Kody odpowiedzi
Kod	Znaczenie
200 OK	Żądanie zakończone sukcesem
400 Bad Request	Nieprawidłowe parametry zapytania
401 Unauthorized	Brak uwierzytelnienia
500 Internal Server Error	Błąd serwera