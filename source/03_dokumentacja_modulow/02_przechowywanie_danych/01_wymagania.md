# Wymagania

Moduł z pozostałymi komponentami systemu łączy się dwiema drogami:

+ Przez interfejs HTTP wykorzystywany przez moduł zbierania danych (poprzedni
  komponent)
+ Poprzez dodawanie nowych zadań do kolejki, zbieranych i wykonywanych
  przez moduł ekstrakcji kluczy (następny komponent)
  
Wymagania funkcjonalne modułu sprowadzają się więc do obsłużenia
obydwu kierunków komunikacji. Interfejs HTTP powinien pozwalać na dwie operacje:

+ Dodanie oferty do bazy (nadpisując jeśli oferta z takim adresem URL już istnieje)
+ Pobranie listy adresów URL ofert zapisanych już w bazie
+ Uaktualnienie wybranej oferty z bazy danych


Natomiast na drodze komunikacji z kolejnym modułem:

+ Rozpoczęcie nowego zadania Celery z dokumentem oferty przekazanym jako
  argument, po zapisie oferty do bazy.
  
  
Wymagania niefunkcjonalne modułu sprowadzają się natomiast do:

+ **niezawodności** - usługa powinna być dostępna możliwie cały czas. Nie jest to
  jednak kwestia kluczowa, ponieważ stosunkowo krótkie braki w dostępności (
  rzędu maksymalnie kilku dni) nie ciągną za sobą konsekwencji.
  Jeżeli moduł zbierający dane nie uzyska odpowiedzi od modułu zajmującego się
  ich przechowywaniem, informacje o tej ofercie nie zostaną nigdzie zapisane.
  Kiedy usługa przechowywania będzie ponownie dostępna, na zapytanie scrapera
  o listę ofert będących już w bazie zwróci tę sprzed awarii, wszystkie pominięte
  oferty zostaną więc ostatecznie dodane.

+ **wydajności** - liczba nadchodzących ofert może być potencjalnie duża, proces
  zapisu do bazy powinien być więc jak najmniej skomplikowany i efektywny, aby
  uniknąć spadków na wydajności z powodu niewydajnych zapytań. Podobnie jak
  w kwestii niezawodności, nie jest to jednak wymaganie kluczowe. Spadki
  w wydajności nie będą bowiem objawiać się wolniejszym działaniem aplikacji
  przeznaczonej dla użytkownika końcowego, a jedynie późniejszym pojawianiem
  się w niej nowych ofert.
