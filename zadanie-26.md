1. Znalezione błędy
stesp zamiast steps – literówka w nazwie sekcji. Poprawiono na steps.
npm build – niepoprawna komenda. Poprawiono na npm run build.
Brak jawnego tagu Docker – poprawiono budowanie obrazu na docker build -t myapp:latest ..
Nieprawidłowe położenie when – przeniesiono sekcję when przed steps.
2. Poprawiony Jenkinsfile
groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test'
            }
        }

        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                sh 'docker build -t myapp:latest .'
                sh 'docker push myapp:latest'
            }
        }
    }
}

3. Podsumowanie

Poprawiono literówkę, komendę budowania aplikacji, tag obrazu Docker oraz kolejność sekcji when i steps.

Dzięki temu Jenkinsfile ma poprawną strukturę Declarative Pipeline.