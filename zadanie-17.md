Przykład użycia:


javascript
const tasks = [
  { id: 3, title: "Zadanie C", status: "completed" },
  { id: 1, title: "Zadanie A", status: "completed" },
  { id: 2, title: "Zadanie B", status: "pending" }
];

console.log(getCompletedTasks(tasks));
Wynik:


javascript
["Zadanie A", "Zadanie C"]
Działanie:

filter() – wybiera zadania zakończone.

sort() – sortuje je według ID rosnąco.

map() – zwraca wyłącznie tytuły.


