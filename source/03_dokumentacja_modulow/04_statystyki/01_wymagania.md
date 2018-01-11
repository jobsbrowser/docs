# Wymagania

Przeznaczeniem modułu jest odpowiadanie na żądania wyszukiwania oraz
generowania statystyk. Komunikacja taka powinna odbywać się z wykorzystaniem
protokołu HTTP, tak aby łatwo można było zintegrować moduł z aplikacją WWW
bądź w przypadku takiej potrzeby innym dowolnym konsumentem.

Z powodu złożoności zapytań (jak np. generowanie statystyk sumarycznych dla
wielu dni i wielu kluczy jednocześnie) moduł potrzebuje własnej bazy danych
na której wykonywane będą zapytania. Wymusza to dodatkowe wymaganie w postaci
możliwości dodawania nowych ofert, z którego korzysta moduł ekstrakcji
kluczy (wysyłając na bieżąco w pełni przetworzone oferty).


Wymagania funkcjonalne modułu sprowadzają się więc do obsługi następujących
żądań HTTP:

+ dodanie nowej oferty do bazy
+ wyszukiwanie ofert przy pomocy danego zbioru kluczy
+ generowanie statystyk, tj. dla każdego dnia z zakresu od 02.12.2018 do
daty wykonania żądania obliczenie ilości aktywnych wówczas w serwisie pracuj.pl
ofert zawierających podane klucze
+ generowanie statystyk całościowych - tj. ilości wszystkich ofert w bazie
(również we wspomnianym wyżej zakresie) oraz daty dodania ostatniego ogłoszenia


Natomiast wymagania niefunkcjonalne postawione modułowi to:

+ **niezawodność** - usługa powinna być dostępna cały czas, ponieważ
  dostarcza ona danych niezbędnych do pokazania wszystkich statystyk w
  aplikacji z której korzysta użytkownik. Bez niej aplikacja WWW staje się
  bezużyteczna.
+ **wydajność** - liczba przychodzących do modułu danych może być momentami
  bardzo duża, dlatego zapisywanie do bazy nie może być zrobione niewydajnie.
  Największy wpływ na wydajność mają zapytania generujące odpowiednie statystyki.
  Niektóre z nich są skomplikowane, dlatego niezbędna jest ich optymalizacja.
  Wydłużony czas generowania statystyk obniży znacznie komfort używania aplikacji
  WWW
