Wyjaśnienie skryptu linia po linii

bash
#!/bin/bash
Informuje system, że skrypt ma być uruchomiony za pomocą Bash.


bash
if systemctl is-active --quiet docker; then
Sprawdza, czy Docker działa. Jeśli tak, wykonuje kod poniżej.


bash
echo "Docker działa poprawnie."
Wyświetla komunikat, że Docker działa.


bash
else
Jeśli Docker nie działa, przechodzi do tej części skryptu.


bash
echo "Docker nie działa. Próba uruchomienia..."
Wyświetla informację o próbie uruchomienia Dockera.


bash
sudo systemctl start docker
Próbuje uruchomić usługę Docker z uprawnieniami administratora.


bash
if systemctl is-active --quiet docker; then
Ponownie sprawdza, czy Docker został uruchomiony.


bash
echo "Docker został pomyślnie uruchomiony."
Wyświetla komunikat o sukcesie.


bash
else
Jeśli uruchomienie się nie powiodło, wykonuje kolejne polecenia.


bash
echo "Błąd: Nie udało się uruchomić Dockera."
Wyświetla komunikat o błędzie.


bash
exit 1
Kończy działanie skryptu i zwraca kod błędu.


bash
fi
Kończy instrukcję warunkową if.

Najprościej: skrypt sprawdza Dockera → jeśli nie działa, próbuje go uruchomić → ponownie sprawdza, czy działa.