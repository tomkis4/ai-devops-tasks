Analiza złożoności i optymalizacja algorytmu findPairs
1. Opis algorytmu

Funkcja findPairs() wyszukuje pary liczb z tablicy, których suma jest równa podanej wartości targetSum.

2. Złożoność obecnego algorytmu
Czasowa: O(n²) – algorytm wykorzystuje dwie zagnieżdżone pętle.
Pamięciowa: O(n²) – w najgorszym przypadku zapisuje wiele znalezionych par.
3. Optymalizacja

Można użyć struktury Set, która pozwala szybko sprawdzać, czy dana liczba już wystąpiła.

Zoptymalizowany kod
javascript
function findPairs(arr, targetSum) {
  const pairs = [];
  const seen = new Set();

  for (const num of arr) {
    const complement = targetSum - num;

    if (seen.has(complement)) {
      pairs.push([complement, num]);
    }

    seen.add(num);
  }

  return pairs;
}

4. Przykład działania
javascript
console.log(findPairs([1, 2, 3, 4, 5], 6));


Wynik:

javascript
[[2, 4], [1, 5]]

5. Porównanie złożoności
Rodzaj	Stary algorytm	Nowy algorytm
Czasowa	O(n²)	O(n) średnio
Pamięciowa	O(n²)	O(n + k)

Gdzie:

n – liczba elementów tablicy.
k – liczba znalezionych par.
6. Podsumowanie

Zastosowanie Set pozwala uniknąć dwóch zagnieżdżonych pętli i znacznie przyspiesza działanie algorytmu.

Nowa wersja ma średnią złożoność czasową O(n), zamiast O(n²). Nadal jednak wymaga pamięci na przechowywanie znalezionych par i odwiedzonych elementów.