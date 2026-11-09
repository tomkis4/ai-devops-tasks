1. Czym jest Jest?
Jest to narzędzie do testowania kodu JavaScript. Pozwala sprawdzić, czy funkcje działają poprawnie.

2. Instalacja Jest
W terminalu, w folderze projektu, wpisz:


bash
npm install --save-dev jest
3. Funkcja do testowania
Plik sum.js:


javascript
function sum(a, b) {
  return a + b;
}

module.exports = sum;
4. Test jednostkowy
Plik sum.test.js:


javascript
const sum = require('./sum');

test('dodaje dwie liczby', () => {
  expect(sum(2, 3)).toBe(5);
});
Wyjaśnienie:

test() – tworzy test.

expect() – sprawdza wynik funkcji.

toBe(5) – oczekuje wyniku 5.

5. Konfiguracja
W pliku package.json dodaj:


json
"scripts": {
  "test": "jest"
}
6. Struktura projektu

text
projekt/
│
├── node_modules/
├── sum.js
├── sum.test.js
└── package.json
7. Uruchomienie testu
W terminalu wpisz:


bash
npm test
Oczekiwany wynik:


text
PASS  ./sum.test.js
✓ dodaje dwie liczby