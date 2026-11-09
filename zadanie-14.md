May 19 10:15:32 server dockerd[1234]: time="2025-05-19T10:15:32.123456789Z" level=info msg="Container 78a2b3c4 health status changed from starting to healthy"
May 19 10:16:45 server dockerd[1234]: time="2025-05-19T10:16:45.987654321Z" level=info msg="Container 78a2b3c4 failed to connect to 172.17.0.3:5432: connection refused"
May 19 10:16:47 server dockerd[1234]: time="2025-05-19T10:16:47.246813579Z" level=warning msg="Container 78a2b3c4 health status changed from healthy to unhealthy"

W logach widać, że kontener Docker początkowo działał poprawnie, ale później stracił połączenie z bazą danych PostgreSQL.

Analiza logów
10:15:32 – Kontener działa poprawnie


text
health status changed from starting to healthy
Kontener zakończył uruchamianie i otrzymał status healthy.

10:16:45 – Problem z połączeniem


text
failed to connect to 172.17.0.3:5432: connection refused
Kontener nie może połączyć się z bazą PostgreSQL pod adresem 172.17.0.3 na porcie 5432.

10:16:47 – Kontener przestał być zdrowy


text
health status changed from healthy to unhealthy
Docker wykrył problem i zmienił status kontenera na unhealthy.

Możliwe przyczyny
PostgreSQL został zatrzymany.

Baza danych nie zdążyła się uruchomić.

PostgreSQL nie nasłuchuje na porcie 5432.

Wystąpił problem z konfiguracją sieci Docker.

Baza danych uległa awarii.

Jak sprawdzić problem?
1. Sprawdź kontenery:


bash
docker ps -a
2. Sprawdź logi bazy danych:


bash
docker logs NAZWA_KONTENERA
3. Sprawdź status PostgreSQL:


bash
docker exec NAZWA_KONTENERA pg_isready
4. Sprawdź sieć Docker:


bash
docker network ls
Podsumowanie
Główny problem to brak połączenia z PostgreSQL na porcie 5432. Należy sprawdzić, czy baza danych działa i czy kontenery mogą się ze sobą komunikować.


