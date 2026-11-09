bazowa wersja:
def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates
    Bardziej wydajna wersja:


python
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()

    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)
   
    Co poprawiono?
Użyto set, który pozwala szybko sprawdzać, czy element już istnieje.

Usunięto dwie zagnieżdżone pętle.

Każdy element jest sprawdzany tylko raz.