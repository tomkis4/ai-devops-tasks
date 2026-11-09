Konwersja JSON do CSV
1. Opis procesu konwersji

Konwersja JSON do CSV polega na przekształceniu danych zapisanych w formacie JSON na tabelę, w której:

Każdy obiekt JSON stanowi jeden wiersz.
Każde pole obiektu stanowi osobną kolumnę.
Wartości są oddzielone przecinkami.

W tym przykładzie wykorzystujemy kolumny: id, name, email, roles.

2. Przykładowy wynik CSV
csv
id,name,email,roles
1,Jan Kowalski,jan@example.com,"admin; user"
2,Anna Nowak,anna@example.com,user

3. Potencjalne wyzwania
Tablice (roles)

CSV nie obsługuje bezpośrednio tablic. Można je reprezentować na kilka sposobów:

Łączyć wartości średnikiem, np. "admin; user".
Łączyć wartości przecinkiem, pamiętając o umieszczeniu całej wartości w cudzysłowie.
Tworzyć osobne kolumny dla każdej roli.
Znaki specjalne

Przecinki, cudzysłowy i znaki nowej linii mogą powodować problemy. Wartości zawierające takie znaki należy odpowiednio ujmować w cudzysłowy i uciekać cudzysłowy.

Brakujące wartości

Puste pola w JSON można zapisać jako puste komórki w CSV.

Typy danych

CSV przechowuje dane jako tekst, dlatego liczby i wartości logiczne mogą wymagać ponownej konwersji podczas odczytu.

4. Podsumowanie

Konwersja JSON do CSV ułatwia analizowanie danych w arkuszach kalkulacyjnych. Największym wyzwaniem jest prawidłowe przedstawienie złożonych struktur, takich jak tablice i obiekty. W tym przykładzie tablicę roles reprezentujemy jako tekst, a poszczególne role oddzielamy średnikiem.