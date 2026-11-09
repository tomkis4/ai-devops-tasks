Jakie są 5 kluczowych praktyk bezpieczeństwa dla aplikacji Dockerowych w środowisku produkcyjnym?

1. Uruchamianie jako non-root – nie uruchamiaj kontenerów jako administrator (root). Ogranicza to skutki ewentualnego włamania.

2. Aktualizowanie obrazów – regularnie aktualizuj obrazy Docker i usuwaj znane podatności.

3. Ochrona haseł i danych – używaj Docker Secrets lub zmiennych środowiskowych zamiast zapisywania haseł bezpośrednio w kodzie.

4. Ograniczanie uprawnień – przyznawaj kontenerom tylko niezbędne uprawnienia i unikaj --privileged.

5. Monitorowanie i logowanie – kontroluj logi kontenerów, monitoruj ich działanie i reaguj na podejrzane zdarzenia.

Podsumowanie: Najważniejsze jest ograniczanie uprawnień, aktualizowanie obrazów i ochrona danych dostępowych.

Najprościej: utwórz użytkownika w Dockerfile i ustaw go w docker-compose.yml.

1. Dockerfile

dockerfile
FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Utworzenie użytkownika bez uprawnień root
RUN useradd -m appuser

USER appuser

CMD ["npm", "start"]
2. docker-compose.yml

yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    user: "appuser"
3. Uruchomienie

bash
docker compose up --build -d
4. Sprawdzenie

bash
docker compose exec app whoami
Oczekiwany wynik:


text
appuser
Ważne: Jeśli aplikacja potrzebuje zapisywać pliki, nadaj użytkownikowi appuser odpowiednie uprawnienia do katalogów.

Dzięki temu aplikacja nie będzie działać jako root, co zwiększa bezpieczeństwo kontenera.