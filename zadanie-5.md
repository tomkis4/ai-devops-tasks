# Zadanie 5
Grok 4.7

## Prompt 1

Stwórz prosty diagram ASCII Art przedstawiający połączenie klienta, serwera aplikacji i bazy danych.

## Diagram 1

```
+----------+         +--------------------+         +--------------+
|          |  HTTP   |                    |   SQL   |              |
|  Klient  | ------->| Serwer aplikacji   | ------->| Baza danych  |
|          | <-------|                    | <-------|              |
+----------+ odpowiedź +--------------------+  dane  +--------------+
```

## Prompt 2

Dodaj do diagramu opisy elementów i kierunki przepływu danych.

## Diagram 2

```
+------------------+          +------------------------+          +------------------+
| KLIENT           |          | SERWER APLIKACJI       |          | BAZA DANYCH      |
| przeglądarka     |  żądanie | logika, API            |  zapytanie | tabele, rekordy |
| lub aplikacja    | -------> |                        | -------> |                  |
|                  | <------- |                        | <------- |                  |
|                  | odpowiedź|                        | wynik    |                  |
+------------------+          +------------------------+          +------------------+

Kierunek przepływu:
  klient  --HTTP-->  serwer  --SQL-->  baza
  klient  <--JSON--  serwer  <--dane-- baza
```
