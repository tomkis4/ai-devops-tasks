
#!/bin/bash

# Sprawdzenie, czy Docker działa
if systemctl is-active --quiet docker; then
    echo "Docker działa poprawnie."
else
    echo "Docker nie działa. Próba uruchomienia..."

    # Próba uruchomienia usługi Docker
    sudo systemctl start docker

    # Ponowne sprawdzenie statusu
    if systemctl is-active --quiet docker; then
        echo "Docker został pomyślnie uruchomiony."
    else
        echo "Błąd: Nie udało się uruchomić Dockera."
        exit 1
    fi
fi
