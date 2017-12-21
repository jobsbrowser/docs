# Baza danych

Wykorzystanym silnikiem bazy danych jest MongoDB[@mongodb]. Zdecydowaliśmy się na bazę
relacyjną z kilku powodów. Po pierwsze tak naprawdę jedynym typem trzymanych
w niej danych są same oferty. Oznacza to że w bazie relacyjnej mielibyśmy
tylko jedną tabelę - bez żadnych relacji czy potrzeby zachowania spójności.
Nie ma potrzeby również stosowania mechanizmu transakcji, czy skomplikowanych
zapytań. Tym czego faktycznie oczekujemy od bazy jest wydajność, dostępność
oraz ewentualna skalowalność. Wybór był więc prosty.
Struktura dokumentów przechowywanych w bazie jest identyczna jak struktura
zebranego ogłoszenia. Dla przypomnienia, pola jakie wyróżniamy w dokumencie
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
