# Zadanie 4
Grok 4.7

## Prompt 1

Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

## Odpowiedź 1

Najpierw zmierz, co zjada pamięć, a potem ustaw limit kontenera i ogranicz pamięć samej aplikacji.

**1. Zobacz zużycie**

```bash
docker stats
```

Kolumna `MEM USAGE / LIMIT` pokazuje, ile RAM-u bierze kontener i jaki ma limit. Jeśli limit to kilka gigabajtów, a aplikacja jest mała, proces w środku trzyma za dużo danych albo nie ma własnego limitu sterty.

**2. Ustaw limit kontenera**

```bash
docker run -m 512m --memory-swap 512m twoj-obraz
```

W Compose:

```yaml
services:
  app:
    image: twoj-obraz
    mem_limit: 512m
```

`--memory-swap` równe `-m` wyłącza swap. Po przekroczeniu limitu jądro zabija proces (OOM). To chroni hosta, ale nie naprawia wycieku w aplikacji.

**3. Ogranicz pamięć procesu**

- **Node.js:** `NODE_OPTIONS=--max-old-space-size=384` (wartość w MB, nieco poniżej limitu kontenera).
- **Java:** `-Xmx384m`.
- **Bazy i cache:** zmniejsz `shared_buffers`, pule połączeń i rozmiar cache.

**4. Jeśli zużycie rośnie bez końca**

To zwykle wyciek albo nieograniczony cache. Zrestartowanie kontenera tylko na chwilę zwalnia RAM. Trzeba sprawdzić logi i profil aplikacji, a nie tylko podnosić limit.

## Prompt 2

Jesteś doświadczonym DevOps Engineerem z 10-letnim doświadczeniem. Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

## Odpowiedź 2

Najpierw ustal, czy pamięć rośnie bez końca, czy kontener po prostu startuje z za dużym zapasem. Limit bez pomiaru tylko zamienia problem w restarty po OOM.

**Zmierz, zanim cokolwiek zmienisz**

```bash
docker stats --no-stream
docker inspect <kontener> --format '{{.HostConfig.Memory}} {{.State.OOMKilled}}'
```

`docker stats` pokazuje bieżące zużycie i limit cgroup. `OOMKilled=true` oznacza, że jądro zabiło proces po przekroczeniu limitu, a nie że aplikacja sama się wyłożyła. W logu szukaj `Killed` oraz kodu wyjścia 137.

Wejdź do kontenera i sprawdź, który proces trzyma RAM: `ps aux --sort=-rss`. Przy Node i Javie sam limit kontenera nic nie daje, dopóki sterta procesu jest większa niż ten limit.

**Ustaw limit hosta**

```bash
docker run -m 512m --memory-swap 512m twoj-obraz
```

W Compose: `mem_limit: 512m`. `--memory-swap` równe `-m` wyłącza swap, więc kontener nie zamula dysku, gdy brakuje RAM-u. Limit dobierz z pomiaru: szczyt ze `stats` plus około 20% zapasu. Za niski limit daje pętlę restartów, za wysoki zostawia aplikację bez hamulca.

**Zejdź do procesu**

- Node: `NODE_OPTIONS=--max-old-space-size=384` (MB, poniżej limitu kontenera).
- Java: `-XX:MaxRAMPercentage=75.0`, żeby sterta widziała limit cgroup, a nie RAM całego hosta.
- Postgres, Redis, cache: zmniejsz bufory i pule połączeń. Jeden kontener z domyślnym `shared_buffers` potrafi zająć więcej niż mała aplikacja.

**Gdy zużycie rośnie w czasie**

To wyciek albo cache bez górnej granicy. Restart kontenera zwalnia pamięć tylko do następnego wzrostu. Zostaw limit jako zabezpieczenie hosta, zbierz heap dump albo profil i popraw kod. Obraz wielostopniowy zmniejsza dysk, nie RAM w czasie działania.

## Obserwacje

- Pytanie było to samo. Drugi prompt dodał rolę doświadczonego inżyniera DevOps i odpowiedź zeszła głębiej w diagnostykę.
- Pierwsza odpowiedź to krótka lista kroków: `docker stats`, limit 512 MB, limit sterty Node i Javy, uwaga o wycieku.
- Druga odpowiedź zaczyna od rozróżnienia skoku na starcie i wzrostu w czasie. Dochodzą `OOMKilled`, kod wyjścia 137, `ps` po RSS, dobór limitu ze szczytu plus zapas oraz `-XX:MaxRAMPercentage` zamiast stałego `-Xmx`.
- Wspólny rdzeń obu odpowiedzi: najpierw pomiar, potem limit cgroup, potem limit procesu. Sam restart kontenera nie usuwa wycieku.
- Rola w prompcie zmieniła szczegółowość i język operacyjny. Nie zmieniła kierunku rozwiązania.
