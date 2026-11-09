# Zadanie 3
Grok 4.7

## Prompt 1

dockerfile node

## Odpowiedź 1

Zacząłem od sprawdzenia katalogu projektu, żeby Dockerfile pasował do rzeczywistej aplikacji. W katalogu nie było `package.json` ani istniejącego `Dockerfile` — jest tylko folder `ai-devops-tasks` z opisami zadań. Zanim powstała gotowa odpowiedź, przyszedł drugi, dokładniejszy prompt.

## Prompt 2

Napisz prosty Dockerfile dla aplikacji Node.js, który:
- używa Node 18 jako obrazu bazowego
- kopiuje pliki package.json i package-lock.json
- instaluje zależności
- kopiuje resztę plików aplikacji
- wystawia port 3000
- uruchamia aplikację poleceniem "npm start" tylko wypisz na czacie

## Odpowiedź 2

```dockerfile
FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

## Wnioski

- Pierwszy prompt był zbyt ogólny, żeby od razu podać Dockerfile. Najpierw sprawdziłem, czy w projekcie jest aplikacja Node.js. Nie było jej, więc sensowna była dopiero druga, konkretna instrukcja.
- Drugi prompt kazał tylko wypisać plik na czacie, więc nie zapisywałem go wtedy na dysk.
- `package.json` i `package-lock.json` są kopiowane przed resztą kodu, żeby warstwa z zależnościami przebudowywała się tylko wtedy, gdy zmienią się te pliki.
- `npm ci` instaluje zależności dokładnie według lockfile, co jest powtarzalne w obrazie.
- `CMD ["npm", "start"]` uruchamia aplikację jako proces główny kontenera. `EXPOSE 3000` tylko dokumentuje port — nie publikuje go na hoście.
