# Wyjaśnienie zależności między etapami pipeline’u CI/CD

W potoku (pipeline) CI/CD dla aplikacji webowej poszczególne etapy są ze sobą ściśle powiązane. Zależności te decydują o tym, czy dany krok może się rozpocząć, czy musi czekać na zakończenie lub pomyślny wynik poprzedniego.

## 1. Sekwencyjność początkowa
* **Checkout kodu $\rightarrow$ Budowanie aplikacji:** 
  To absolutna zależność liniowa. Żaden proces budowania (kompilacja, pobieranie zależności przez np. npm czy Maven) nie może się odbyć, dopóki kod źródłowy nie zostanie poprawnie pobrany z repozytorium (np. Git).

## 2. Równoległość fazy testów i jakości
Po poprawnym zbudowaniu aplikacji pipeline często rozgałęzia się, aby przyspieszyć proces. Etapy te są od siebie niezależne, ale wszystkie zależą od sukcesu etapu **Budowania**:
* **Budowanie $\rightarrow$ Testy jednostkowe**
* **Budowanie $\rightarrow$ Analiza statyczna kodu (np. SonarQube)**
* **Budowanie $\rightarrow$ Skanowanie bezpieczeństwa (SAST/DAST)**

Wszystkie te trzy etapy mogą działać równolegle, ponieważ badają ten sam artefakty lub kod źródłowy wygenerowany w kroku budowania.

## 3. Zależność od bram jakości (Quality Gates)
* **Testy jednostkowe, Analiza statyczna, Bezpieczeństwo $\rightarrow$ Budowanie obrazu Docker:**
  To kluczowa zależność typu "bramka jakości". Obraz Docker **nie powinien** zostać zbudowany, jeśli w kodzie wykryto krytyczne błędy bezpieczeństwa, nie przeszły testy jednostkowe lub naruszono standardy jakości kodu. Zapewnia to, że do kolejnych etapów trafiają wyłącznie przetestowane i bezpieczne komponenty.

## 4. Testowanie środowiskowe i kontenerowe
* **Budowanie obrazu Docker $\rightarrow$ Testy integracyjne:**
  Testy integracyjne wymagają gotowego, spakowanego środowiska (obrazu Docker), aby sprawdzić, jak aplikacja współpracuje z zewnętrznymi usługami (np. bazą danych, cache). Dlatego ten etap musi nastąpić bezpośrednio po utworzeniu obrazu.

## 5. Automatyzacja wdrożeń i kontrola biznesowa
* **Testy integracyjne $\rightarrow$ Wdrożenie na Staging:**
  Środowisko staging odzwierciedla produkcję. Wdrożenie na nie następuje automatycznie pod warunkiem, że testy integracyjne zakończyły się sukcesem.
* **Wdrożenie na Staging $\rightarrow$ Akceptacja ręczna (Manual Approval):**
  Zanim kod trafi do użytkowników końcowych, wymagane jest przejście przez środowisko staging w celu weryfikacji manualnej lub biznesowej.
* **Akceptacja ręczna $\rightarrow$ Wdrożenie na Produkcję:**
  Jest to tzw. *deployment gate* o charakterze decyzyjnym (ludzkim). Dopóki osoba odpowiedzialna (np. Tech Lead, Product Owner) nie zatwierdzi wdrożenia w Jenkinsie, proces zatrzymuje się na środowisku staging, chroniąc system produkcyjny przed nieautoryzowanym lub przedwczesnym wypuszczeniem zmian.