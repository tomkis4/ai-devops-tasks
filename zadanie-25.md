1. Wyjaśnienie etapów Jenkinsfile
1. Checkout


groovy
stage('Checkout') {
    steps {
        checkout scm
    }
}
Pobiera kod projektu z repozytorium Git.

2. Install Dependencies


groovy
stage('Install Dependencies') {
    steps {
        sh 'npm install'
    }
}
Instaluje wszystkie biblioteki potrzebne do działania aplikacji Node.js.

3. Run Tests


groovy
stage('Run Tests') {
    steps {
        sh 'npm test'
    }
}
Uruchamia testy automatyczne. Jeśli testy nie przejdą, pipeline zostanie zatrzymany.

4. Build Application


groovy
stage('Build Application') {
    steps {
        sh 'npm run build'
    }
}
Buduje aplikację, przygotowując ją do uruchomienia lub wdrożenia.

5. Build Docker Image


groovy
stage('Build Docker Image') {
    steps {
        sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
    }
}
Tworzy obraz Docker na podstawie pliku Dockerfile.

6. Push Docker Image


groovy
stage('Push Docker Image') {
    steps {
        // logowanie i publikowanie obrazu
    }
}
Loguje się do Docker Hub i wysyła obraz do rejestru.

7. Post


groovy
post {
    success {
        echo 'Pipeline zakończony sukcesem!'
    }
    failure {
        echo 'Pipeline zakończony błędem!'
    }
}
Wyświetla komunikat zależnie od wyniku całego pipeline'u.

2. Najlepsze praktyki Jenkins
Automatyczne testowanie – uruchamiaj testy przy każdej zmianie kodu.

Bezpieczne przechowywanie haseł – używaj Jenkins Credentials zamiast wpisywania haseł w kodzie.

Oddzielne etapy – podziel pipeline na małe, czytelne etapy.

Kontrola błędów – zatrzymuj pipeline, jeśli testy lub budowanie zakończą się niepowodzeniem.

Wersjonowanie obrazów Docker – używaj tagów, np. numeru wersji lub identyfikatora commita, zamiast samego latest.

Czyszczenie zasobów – usuwaj niepotrzebne pliki i obrazy po zakończeniu pracy.

Ograniczanie uprawnień – Jenkins powinien mieć tylko niezbędne uprawnienia.

3. Co można poprawić w naszym Jenkinsfile?
Najważniejsze zmiany:

Zamiast npm install użyj npm ci, jeśli projekt ma plik package-lock.json.

Zamiast tagu latest używaj identyfikatora commita.

Dodaj etap sprawdzania jakości kodu (np. ESLint).

Dodaj obsługę czyszczenia zasobów w sekcji post.

Nie przechowuj haseł bezpośrednio w Jenkinsfile.

Podsumowanie: Dobry pipeline Jenkins powinien automatycznie pobierać kod, instalować zależności, testować aplikację, budować obraz i bezpiecznie publikować go w rejestrze Docker.