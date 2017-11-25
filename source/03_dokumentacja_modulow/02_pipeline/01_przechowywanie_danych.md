# Moduł przechowujący dane

Jednym z podmodułów komponentu jest moduł odpowiedzialny za przechowywanie
danych. Przez dane rozumiemy w tym przypadku te w postaci "pół-surowej". Tzn.
będące już po wstępnym, prostym procesie przetwarzania w module zbierania danych,
ale jeszcze przed najbardziej znaczącym procesem ekstrakcji kluczy. Są to więc
dane które są bazą dla przyszłych działań systemu, ale w obecnej formie nie
dostarczają wielu informacji.


##  Interfejs

Moduł z pozostałymi komponentami systemu łączy się dwiema drogami:

+ Przez interfejs HTTP wykorzystywany przez moduł zbierania danych (poprzedni
  komponent)
+ Poprzez dodawanie nowych zadań do frameworka *Luigi*, zbieranych i wykonywanych
  przez moduł ekstrakcji kluczy (następny komponent)
  
Interfejs HTTP sprowadza się do możliwości wykonania dwóch działań:

+ Dodanie oferty do bazy (nadpisując jeśli oferta z takim adresem URL już istnieje)
+ Pobranie listy adresów URL ofert zapisanych już w bazie

Interfejs zaimplementowany jest przy użyciu micro-frameworka Flask.


## Baza danych

Wykorzystanym silnikiem bazy danych jest MongoDB. Zdecydowaliśmy się na bazę
relacyjną z kilku powodów. Po pierwsze tak naprawdę jedynym typem trzymanych
w niej danych są same oferty. Oznacza to że w bazie relacyjnej mielibyśmy
tylko jedną tabelę - bez żadnych relacji czy potrzeby zachowania spójności.
Nie ma potrzeby również stosowania mechanizmu transakcji, czy skomplikowanych
zapytań. Tym czego faktycznie oczekujemy od bazy jest wydajność, dostępność
oraz ewentualna skalowalność. Wybór był więc prosty.


## Luigi

Podczas wykonywania prawidłowego żądania dodania oferty, poza samym faktem dodania
jej do kolekcji w bazie danych, dodawane jest nowe zadanie do kolejki frameworka
Luigi. Jest to moment wejścia oferty do trzeciego etapu, tj. ekstrakcji kluczy.
To głównie tam wykorzystywane są możliwości Luigiego, więc bardziej szczegółowy
opis tego środowiska znaleźć można w dokumentacji tego komponentu.


## Uruchomienie


## Struktura kodu


## Testy
