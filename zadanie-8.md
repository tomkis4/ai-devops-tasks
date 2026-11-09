Co oznacza błąd?
Port 3000 jest już zajęty przez inny proces lub kontener Docker. Docker nie może więc uruchomić kolejnej aplikacji na tym porcie.

Jak rozwiązać problem?
1. Sprawdź, kto używa portu 3000:


bash
sudo lsof -i :3000
2. Sprawdź uruchomione kontenery:


bash
docker ps
3. Jeśli port zajmuje inny kontener, zatrzymaj go:


bash
docker stop ID_KONTENERA
4. Uruchom ponownie aplikację:


bash
docker compose up -d
Alternatywne rozwiązanie
Możesz zmienić port w pliku docker-compose.yml:


yaml
ports:
  - "3001:3000"
Wtedy aplikacja będzie dostępna pod portem 3001.

Podsumowanie: Problem wynika z konfliktu portów. Zwolnij port 3000 albo zmień go na inny, np. 3001.


