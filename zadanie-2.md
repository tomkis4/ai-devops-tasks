# Zadanie 2
Grok 4.7
## Wymień 5 korzyści z używania kontenerów Docker w środowisku programistycznym.

1. **Takie samo środowisko u każdego** — aplikacja i jej zależności są spakowane w kontener, więc działa tak samo na komputerze programisty, w testach i na serwerze.
2. **Szybkie uruchomienie projektu** — nowa osoba w zespole odpala środowisko jedną komendą, bez ręcznej instalacji baz danych, bibliotek i wersji narzędzi.
3. **Izolacja zależności** — każdy projekt ma własne wersje bibliotek i usług, więc nie kolidują ze sobą na jednym komputerze.
4. **Łatwiejsze testowanie** — można szybko postawić i usunąć bazę, kolejkę albo inną usługę tylko na czas testu.
5. **Bliżej produkcji** — kontener, który działa lokalnie, można wdrożyć w podobnej formie na serwer, co zmniejsza różnice między środowiskiem deweloperskim a produkcyjnym.

Chat gpt
Oto 5 najważniejszych korzyści z używania kontenerów Docker w środowisku programistycznym:

1. Spójność środowiska – Docker zapewnia takie samo środowisko uruchomieniowe na komputerach programistów, serwerach testowych i produkcyjnych. Dzięki temu ogranicza problemy typu „u mnie działa, a u Ciebie nie”.

2. Izolacja aplikacji – każda aplikacja działa w osobnym kontenerze, z własnymi bibliotekami, zależnościami i konfiguracją. Pozwala to uniknąć konfliktów między różnymi projektami.

3. Łatwe wdrażanie i przenoszenie aplikacji – kontenery można uruchamiać na różnych systemach i serwerach obsługujących Docker bez konieczności ręcznego konfigurowania środowiska.

4. Szybsze uruchamianie i mniejsze zużycie zasobów – kontenery są lżejsze od tradycyjnych maszyn wirtualnych, ponieważ współdzielą jądro systemu operacyjnego.

5. Automatyzacja i łatwiejsze testowanie – Docker umożliwia szybkie tworzenie, usuwanie i odtwarzanie środowisk testowych, co ułatwia integrację z procesami CI/CD (Continuous Integration / Continuous Delivery).

Podsumowanie: Docker przyspiesza pracę programistów, zwiększa powtarzalność procesów i ułatwia współpracę zespołową oraz wdrażanie aplikacji.