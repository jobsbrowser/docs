# Moduł przechowujący dane

Jednym z podmodułów komponentu jest moduł odpowiedzialny za przechowywanie
danych. Przez dane rozumiemy w tym przypadku te w postaci "pół-surowej". Tzn.
będące już po wstępnym, prostym procesie przetwarzania w module zbierania danych,
ale jeszcze przed najbardziej znaczącym procesem ekstrakcji kluczy. Są to więc
dane które są bazą dla przyszłych działań systemu, ale w obecnej formie nie
dostarczają wielu informacji.


## Wymagania

Moduł z pozostałymi komponentami systemu łączy się dwiema drogami:

+ Przez interfejs HTTP wykorzystywany przez moduł zbierania danych (poprzedni
  komponent)
+ Poprzez dodawanie nowych zadań do kolejki, zbieranych i wykonywanych
  przez moduł ekstrakcji kluczy (następny komponent)
  
Wymagania funkcjonalne modułu sprowadzają się więc do obsłużenia
obydwu kierunków komunikacji. Interfejs HTTP powinien pozwalać na dwie operacje:

+ Dodanie oferty do bazy (nadpisując jeśli oferta z takim adresem URL już istnieje)
+ Pobranie listy adresów URL ofert zapisanych już w bazie

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
  


##  Interfejs

Interfejs HTTP zaimplementowany jest przy użyciu micro-frameworka Flask[@flask].
Flask jest wykorzystywany do tworzenia stron internetowych oraz REST API.
Zdecydowaliśmy się na niego ze względu na to, że jest to framework dojrzały,
idealny do małych lub średnich projektów, a w razie wzrostu skali projektu
umożliwia wygodne skalowanie. Flask zawiera również wiele świetnych rozszerzeń,
np. rozszerzenie integrujące go z bazą MongoDB z której korzystamy w projekcie.


## Baza danych

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
+ Kod HTML treści oferty


## Uruchomienie

Do uruchomienia API korzystamy z polecenia `python manage.py runserver`.
Aby uruchomić usługę z odpowiednimi ustawieniami trzeba ustawić zmienną
środowiskową `APP_CONFIG` na wartość *PRODUCTION*. Możemy to zrobić korzystając
z 1 z poniższych poleceń:

-   ```bash
    export APP_CONFIG="production" && python manage.py runserver
    ```
-   ```bash
    APP_CONFIG="PRODUCTION" python manage.py runserver
    ```


## Struktura kodu

Poniżej prezentujemy drzewo katalogów oraz plików modułu wraz z krótkim
omówieniem.

```bash
├── jobsbrowser
│   ├── api                         # katalog modułu API
│   │   ├── __init__.py
│   │   ├── resources.py            # definicja endpointów API
│   │   ├── settings.py             # ustawienia API
│   │   └── spec.yml                # specyfikacja w standardzie OpenAPI(swagger)
│   ├── manage.py                   # skrypt z pożytecznymi komendami dotyczącymi API
│   └── tests                       # katalog z testami modułu
│       ├── __init__.py
│       └── test_api_resources.py   # testy endpointów API
└── requirements.txt                # wymagania modułu
```


## Główne klasy modułu

-   `add_offer` - funkcja implementująca dodawanie otrzymanej oferty do bazy
    danych.
-   `get_offers` - funkcja implementująca pobieranie aktualnych ofert (takich
    których data w polu *valid_through* jest większa od daty dzisiejszej)
    znajdujących się w bazie danych.
-   `init_app` - funkcja tworząca aplikację z podaną konfiguracją (jako
    parametr *config_name* lub zmienna środowiskowa `APP_CONFIG`).
-   **BaseConfig** - klasa z bazową, fundamentalną konfiguracją.
-   **DevConfig** - klasa przechowująca konfigurację developerską.
-   **ProductionConfig** - klasa przechowująca konfigurację produkcyjną.
-   **TestingConfig** - klasa przechowująca konfigurację testową.


## Testy

### Testy jednostkowe \newline \newline

Aby uruchomić testy jednostkowe, w konsoli należy wpisać polecenie `pytest`.
Poniżej przedstawiamy opis testów znajdujących się w pliku
`jobsbrowser/tests/test_api_resources.py`:

-   `test_ping_resource_returns_pong` - test sprawdza czy endpoint */pong*
    (który jest wykorzystywany do sprawdzania czy usługa API jest aktywna)
    zwraca odpowiedź ze statusem 200 oraz wartością "pong".
-   `test_add_offer_resource_try_add_offer_to_mongo_db` - test sprawdza czy
    wysłana poprzez zapytanie POST oferta próbuje być zapisana do bazy danych.
-   `test_get_offers_resource_query_mongo_db` - test sprawdza czy
    po wykonaniu zapytania HTTP GET na endpoint */offers* wykonywana jest próba
    pobrania danych z bazy danych.
