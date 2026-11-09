Aby uruchomić Jenkinsa z przygotowanym wcześniej plikiem konfiguracyjnym w formacie JCasC (Jenkins Configuration as Code), najwygodniej i najszybciej jest skorzystać z kontenera Docker. Pozwala to na automatyczne załadowanie konfiguracji przy starcie serwera bez konieczności ręcznego przelękania się przez instalator graficzny.

Poniżej znajdziesz kompletny przewodnik krok po kroku.

Krok 1: Przygotowanie pliku konfiguracyjnego
Utwórz folder na swoim komputerze, np. jenkins-jcasc.

Zapisz przygotowany wcześniej szablon YAML w tym folderze pod nazwą jenkins.yaml.

Krok 2: Konfiguracja autoryzacji JCasC w pliku YAML
Domyślnie Jenkins wymaga początkowego hasła administratora i przeklikania kreatora instalacji. Aby JCasC w pełni zautomatyzował start i pozwolił na logowanie, dopisz na samym końcu pliku jenkins.yaml sekcję bezpieczeństwa, która tworzy domyślnego użytkownika (np. admin / admin):

YAML
jenkins:
  securityRealm:
    local:
      allowsSignup: false
      users:
        - id: "admin"
          password: "${ADMIN_PASSWORD:-admin}"

authorizationStrategy:
  globalMatrix:
    permissions:
      - "Overall/Administer:admin"
Krok 3: Uruchomienie Jenkinsa za pomocą Dockera
Aby Jenkins wiedział, gdzie szukać pliku konfiguracyjnego, musimy wskazać zmienną środowiskową CASC_JENKINS_CONFIG oraz zamontować nasz plik z dysku do wnętrza kontenera.

Uruchom poniższe polecenie w terminalu (w folderze, gdzie znajduje się plik jenkins.yaml):

Bash
docker run \
  --name jenkins-master \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v $(pwd)/jenkins.yaml:/var/jenkins_home/jenkins.yaml \
  -e CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins.yaml \
  jenkins/jenkins:lts
-p 8080:8080 – Udostępnia panel webowy Jenkinsa na porcie 8080.

-v $(pwd)/jenkins.yaml:/var/jenkins_home/jenkins.yaml – Wstrzykuje Twój plik konfiguracyjny do katalogu domowego Jenkinsa.

-e CASC_JENKINS_CONFIG=... – Wskazuje Jenkinsowi ścieżkę do pliku konfiguracyjnego JCasC przy starcie.

Krok 4: Weryfikacja i uruchomienie
Otwórz przeglądarkę internetową i wejdź pod adres: http://localhost:8080

Zaloguj się danymi skonfiguracyjnymi w pliku YAML (login: admin, hasło: admin).

Sprawdź poprawność konfiguracji:

Zarządzanie Jenkinsem (Manage Jenkins) -> Configuration as Code – powinieneś zobaczyć informację, że konfiguracja została pomyślnie załadowana.

Na stronie głównej powinien pojawić się automatycznie utworzony pipeline o nazwie przykladowy-pipeline.

W sekcji Manage Jenkins -> Tools powinny być widoczne predefiniowane instalacje Mavena oraz Node.js.

Verification: Jeśli panel Jenkinsa uruchomił się bez przechodzenia przez ekran kreatora początkowego (tzw. "Unlock Jenkins") i od razu poprosił o logowanie, oznacza to, że plik JCasC został poprawnie wczytany.