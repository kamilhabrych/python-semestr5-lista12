# Lista 12 - Języki programowania wysokiego poziomu

**Python (12) - Macierze i układy równań**

(1) Stosując eliminację Gaussa i funkcje z operacjami elementarnymi z poprzednich zajęć, napisz funkcję Gauss(A) która sprowadza macierz A do
postaci schodkowej:
-znajdujemy pierwszy niezerowy element x kolumna po kolumnie
-zamieniamy wiersz zawierający x z pierwszym wierszem
-przemnażamy wiersz tak aby zamienić x na 1
-za pomocą 1 zerujemy elementy pod 1
-szukamy kolejnego niezerowego elementu y (pomijając pierwszy wiersz)
-zamieniamy wiersz zawierający y z drugim wierszem
-zamieniamy y na 1, zerujemy elementy pod 1 i kontynuujemy aż zostaną
same zera lub skończą się wiersze.
Przetestuj na konkretnej macierzy, np. rozmiaru 3 na 4 (testując można wyświetlać tymczasowo powstałe macierze, rozdzielając za pomocą input()).

(2) Rzędem macierzy A jest ilość niezerowych wierszy po sprowadzeniu do
postaci schodkowej. Napisz funkcję rz(A) korzystającą z Gauss i zwracającą
rząd A. W pętli generuj dużą ilość losowych macierzy 3 na 4 z wartościami
od 1 do 4 i sprawdź jakie wychodzą rzędy.
Zmodyfikuj program tak aby dla rzędów mniejszych od 3 wyświetlana była
macierz i jej postać schodkowa po czym należy wcisnąć enter aby generować
nowe macierze.

(3) Napisz Gauss2(A) która korzystając z Gauss sprowadza A do postaci
schodkowej i dodatkowo zeruje operacjami elementarnymi wszystkie elementy nad 1 schodkowymi (czyli pierwszymi niezerowymi elementami wierszy).
Przetestuj.

(4) Stosując (3) napisz funkcję odwr(A) zwracającą odwrotność A.
Dla losowej macierzy 3 na 3, przestuj za pomocą funkcji pomnoz.

(5) Stosując Gauss2(A) rozwiąż układy równań:
a)
x1 + x2 + x3 = 4
x1 − x2 + x3 = 2
x1 + x2 − x3 = 1
b)
−2x1 + x2 + x3 = 1
x1 − 2x2 + x3 = 1
x1 + x2 − 2x3 = 1
c)
x1 − 2x2 − x3 + 3x4 = 5
2x1 − 4x2 − 2x3 + 6x4 = 10
2x1 + x2 + x4 = 20
