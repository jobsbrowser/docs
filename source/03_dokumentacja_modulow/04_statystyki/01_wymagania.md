# Wymagania

Moduł z pozostałymi komponentami systemu łączy się przez interfejs HTTP.
Dane do statystyk są dostarczane przez moduł ekstrakcji kluczy.
Natomiast konsumentem danych generowanych przez moduł statystyk jest aplikacja
webowa z której korzysta końcowy użytkownik.

Wymagania funkcjonalne modułu sprowadzają się więc do dwóch głównych zadań

+ dodanie oferty wysłanej przez moduł ekstrakcji kluczy do bazy
+ wysłanie wszelakich statystyk w odpowiedzi na odpowiednie zapytanie HTTP

Wymagania niefunkcjonalne modułu sprowadzają się natomiast do:

+ **niezawodności** - usługa powinna być dostępna cały czas, ponieważ
  dostarcza ona danych niezbędnych do pokazania wszystkich statystyk w
  aplikacji z której korzysta użytkownik.
+ **wydajności** - liczba przychodzących do modułu danych może być momentami
  bardzo duża, dlatego zapisywanie do bazy nie może być zrobione niewydajnie.
  Większy wpływ na wydajność mają zapytania generujące odpowiednie statystyki.
  Niektóre z nich są skomplikowane, dlatego niezbędnym jest ich optymalizacja.
