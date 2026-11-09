
import os
import requests
from requests.auth import HTTPBasicAuth

# Konfiguracja Jenkins
JENKINS_URL = os.getenv("JENKINS_URL", "http://localhost:8080")
USERNAME = os.getenv("JENKINS_USER")
API_TOKEN = os.getenv("JENKINS_TOKEN")

session = requests.Session()
session.auth = HTTPBasicAuth(USERNAME, API_TOKEN)
session.headers.update({"Accept": "application/json"})


def jenkins_request(endpoint, method="GET"):
    """Wysyła zapytanie do Jenkins API."""
    url = f"{JENKINS_URL.rstrip('/')}/{endpoint.lstrip('/')}"

    try:
        response = session.request(method, url, timeout=15)
        response.raise_for_status()
        return response

    except requests.exceptions.HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except requests.exceptions.ConnectionError:
        print("Nie można połączyć się z Jenkins.")
    except requests.exceptions.Timeout:
        print("Przekroczono czas oczekiwania.")
    except requests.exceptions.RequestException as e:
        print(f"Błąd: {e}")

    return None


def list_jobs():
    """Wyświetla wszystkie zadania Jenkins."""
    response = jenkins_request(
        "api/json?tree=jobs[name,color,url]"
    )

    if response:
        jobs = response.json().get("jobs", [])

        print("\n--- Lista zadań ---")
        for job in jobs:
            print(
                f"Nazwa: {job['name']} | "
                f"Status: {job['color']} | "
                f"URL: {job['url']}"
            )


def check_build_status(job_name):
    """Sprawdza status ostatniego buildu."""
    endpoint = (
        f"job/{job_name}/lastBuild/api/json"
        "?tree=number,result,building,timestamp"
    )

    response = jenkins_request(endpoint)

    if response:
        build = response.json()

        print(f"\n--- Build: {job_name} ---")
        print(f"Numer: {build.get('number')}")
        print(f"Status: {build.get('result') or 'W trakcie'}")
        print(f"Czy trwa: {build.get('building')}")


def trigger_job(job_name):
    """Uruchamia wybrane zadanie."""
    response = jenkins_request(
        f"job/{job_name}/build",
        method="POST"
    )

    if response:
        print(f"Wysłano żądanie uruchomienia: {job_name}")


if __name__ == "__main__":

    if not USERNAME or not API_TOKEN:
        raise SystemExit(
            "Ustaw JENKINS_USER i JENKINS_TOKEN."
        )

    print("\n=== Jenkins Manager ===")
    print("1. Lista zadań")
    print("2. Status ostatniego buildu")
    print("3. Uruchom zadanie")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        list_jobs()

    elif choice == "2":
        name = input("Podaj nazwę zadania: ")
        check_build_status(name)

    elif choice == "3":
        name = input("Podaj nazwę zadania: ")
        trigger_job(name)

    else:
        print("Nieprawidłowy wybór.")
