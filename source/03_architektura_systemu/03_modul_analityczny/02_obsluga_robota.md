# Obsługa robota zbierającego dane

Komunikacja między modułem analitycznym a robotem zbierającym dane odbywa
się za pośrednictwem protokołu HTTP. Interfejs udostępniany robotowi pozwala
na następujące operacje:

+ Dodanie oferty do bazy (nadpisując jeśli oferta z takim adresem URL już istnieje)
+ Pobranie listy adresów URL ofert zapisanych już w bazie, tak aby uniknąć przetwarzania ich ponownie
+ Uaktualnienie wybranej oferty z bazy danych
  
  
Wymagania niefunkcjonalne stawiane tej części systemu sprowadzają się zatem do:

+ **niezawodności** - usługa powinna być dostępna możliwie cały czas. Nie jest to
  jednak kwestia kluczowa, ponieważ stosunkowo krótkie braki w dostępności (
  rzędu maksymalnie kilku dni) nie ciągną za sobą konsekwencji.
  Jeżeli robot zbierający dane nie uzyska odpowiedzi od modułu zajmującego się
  ich przechowywaniem i analizą, informacje o tej ofercie nie zostaną nigdzie zapisane.
  Kiedy usługa przechowywania będzie ponownie dostępna, na zapytanie robota
  o listę ofert będących już w bazie zwróci tę sprzed awarii, wszystkie pominięte
  oferty zostaną więc ostatecznie dodane.

+ **wydajności** - liczba nadchodzących ofert może być potencjalnie duża, proces
  zapisu do bazy powinien być więc jak najmniej skomplikowany i efektywny, aby
  uniknąć spadków na wydajności z powodu niewydajnych zapytań. Podobnie jak
  w kwestii niezawodności, nie jest to jednak wymaganie kluczowe. Spadki
  w wydajności nie będą bowiem objawiać się wolniejszym działaniem aplikacji
  przeznaczonej dla użytkownika końcowego, a jedynie późniejszym pojawianiem
  się w niej nowych ofert.
  


**Baza danych**

Wykorzystanym silnikiem bazy danych do roboczego zapisu ofert jest MongoDB[@mongodb].
Wybór padł na bazę nierelacyjną, ponieważ jedynym typem trzymanych
w niej danych są same oferty. Oznacza to że w bazie relacyjnej znajdowałaby się
tylko jedną tabela - bez żadnych relacji czy potrzeby zachowania spójności.
Nie ma potrzeby również stosowania mechanizmu transakcji, czy skomplikowanych
zapytań. Tym co faktycznie jest oczekiwane od bazy jest wydajność, dostępność
oraz ewentualna skalowalność.

Struktura dokumentów przechowywanych w bazie jest identyczna jak struktura
zebranego ogłoszenia. Dla przypomnienia, pola wyróżniane w dokumencie
oferty to:

+ Adres URL
+ Czas w którym pobrano ofertę
+ Kod HTML strony z ofertą
+ ID oferty w systemie pracuj.pl
+ Data dodania
+ Data ważności
+ Podmiot dodający
+ Tytuł oferty
+ Miejsce pracy
+ Kategorie oferty
+ Kod HTML treści oferty (rozbity na opis, kwalifikacje oraz benefity - wg
  struktury Pracuj.pl)
  

**Interfejs HTTP**

Interfejs HTTP zaimplementowany jest przy użyciu mikro-frameworka Flask[@flask].
Przydatne okazało się dostępne rozszerzenie integrujące go z bazą
MongoDB, użytą w module.


