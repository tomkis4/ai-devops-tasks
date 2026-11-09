Walidacja adresu IPv4 za pomocą Regex
1. Wyrażenie regularne
regex
^(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$

2. Wyjaśnienie
^ – początek tekstu.
25[0-5] – liczby od 250 do 255.
2[0-4][0-9] – liczby od 200 do 249.
1?[0-9]{1,2} – liczby od 0 do 199.
| – oznacza „lub”.
\. – kropka oddzielająca liczby.
{3} – powtarza poprzedni fragment 3 razy.
$ – koniec tekstu.

Regex sprawdza, czy adres składa się z czterech liczb oddzielonych kropkami, każda w zakresie od 0 do 255.

3. Przykłady testów
Adres IP	Wynik
192.168.1.1	Poprawny
255.255.255.255	Poprawny
0.0.0.0	Poprawny
127.0.0.1	Poprawny
256.1.1.1	Niepoprawny
192.168.1	Niepoprawny
192.168.1.999	Niepoprawny
abc.def.ghi.jkl	Niepoprawny
4. Testowanie w JavaScript
javascript
const regex = /^(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$/;

const addresses = [
  "192.168.1.1",
  "255.255.255.255",
  "0.0.0.0",
  "256.1.1.1",
  "192.168.1",
  "192.168.1.999"
];

addresses.forEach(ip => {
  console.log(ip, regex.test(ip));
});

5. Podsumowanie

Wyrażenie regularne pozwala sprawdzić poprawność formatu adresu IPv4. Każdy z czterech segmentów musi zawierać liczbę od 0 do 255.