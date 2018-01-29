# Moduł analityczny - podmoduł obsługi robota i ekstrakcji technologii

Jak wspomniano w rozdz. \ref{modul_analityczny}, moduł podzielony jest
na dwa komponenty, korzystające z różnych technologii, a nawet różnych baz danych.
Praca nad nimi przebiegała z użyciem dwóch niezależnych od siebie repozytoriów,
tak więc i na załączonej płycie DVD komponenty znaleźć można w odrębnych katalogach.

Omawianym w tej sekcji podmodułem jest ten odpowiedzialny za obsługę robota
zbierającego dane oraz ekstrakcję technologii. Jego kod źródłowy
znaleźć można w katalogu `src/analytics/pipeline` na załączonej płycie, a jego struktura
przedstawia się następująco:


## Struktura plików kodu źródłowego

```bash
├── jobsbrowser
│   ├── api                          # część odpowiedzialna za obsługę scrapera
│   │   ├── __init__.py
│   │   ├── resources.py             # definicja endpointów API
│   │   ├── settings.py              # ustawienia API
│   │   └── spec.yml                 # specyfikacja API w standardzie OpenAPI(swagger)
│   ├── pipeline                     # łańcuch przetwarzania danych - ekstrakcja technologii
│   │   ├── _app.py
│   │   ├── chains.py                # konstrukcja łańcucha
│   │   ├── __init__.py
│   │   ├── settings.py              # ustawienia Celery oraz MongoDB
│   │   └── tasks                    # moduł poszczególnych zadań pipeline
│   │       ├── bases.py             # bazowe klasy zadań
│   │       ├── exceptions.py        # wyjątki modułu zadań pipeline
│   │       ├── __init__.py
│   │       ├── postprocess.py       # zadania wykonywane na koniec przetwarzania
│   │       ├── preprocess.py        # zadania przygotowujące ofertę to ekstrakcji cech
│   │       ├── process.py           # zadania ekstrakcji technologii
│   │       └── utils.py             # pożyteczne, mniejsze funkcje
│   └── __init__.py
├── tests                            # katalog z testami podmodułu
│   ├── api                          # katalog z testami części obsługującej robota
│   │   ├── __init__.py
│   │   └── test_api_resources.py    # testy endpointów API
│   └── pipeline                     # katalog z testami modułu łańcucha
│       ├── __init__.py
│       └── tasks                    
│           ├── __init__.py
│           ├── test_process.py      # testy zadań ekstrakcji pipeline
│           ├── test_postprocess.py  # testy zadań końcowych pipeline
│           └── test_preprocess.py   # testy zadań początkowych pipeline
```


## Opis klas i metod

Obsługa scrapera

-   `add_offer` - funkcjas implementująca dodawanie otrzymanej oferty do bazy
    danych.
-   `get_offers` - funkcja implementująca pobieranie aktualnych ofert (takich
    których data w polu *valid_through* jest większa od daty dzisiejszej)
    znajdujących się w bazie danych.
-   `update_offer` - funkcja implementująca uaktualnianie oferty z bazy.
-   `init_app` - funkcja tworząca aplikację z podaną konfiguracją (jako
    parametr *config_name* lub zmienna środowiskowa `APP_CONFIG`).
-   *BaseConfig* - klasa z bazową, fundamentalną konfiguracją.
-   *DevConfig* - klasa przechowująca konfigurację developerską.
-   *ProductionConfig* - klasa przechowująca konfigurację produkcyjną.
-   *TestingConfig* - klasa przechowująca konfigurację testową.


Łańcuch przetwarzania

-   `MongoDBTask` - klasa bazowa dla etapów łańcucha przetwarzania danych
    korzystających z danych znajdujących się w bazie MongoDB.
-   `TagsFindingTask` - klasa bazowa dla etapu pipeline'a, który znajduje
    technologie(tagi) w ofercie.
-   `LanguageNotSupported` - klasa błędu, rzucanego w przypadku próby
    przetwarzania oferty napisanej w języku innym niż polski.
-   `prepare` - etap przygotowujący dane do dalszego przetwarzania.
-   `strip_html_tags` - etap usuwający tagi HTML z ofert.
-   `tokenize` - etap rozbijający opis oferty na tokeny.
-   `detect_language` - etap przeprowadzający detekcję języka
    oraz kończący przetwarzanie w przypadku detekcji języka innego niż polski.
-   `remove_stopwords` - etap usuwający tokeny składające się ze słów
    nieistotnych.
-   `find_tags` - etap znajdujący tagi z technologiami spośród tokenów oferty.
-   `save_to_mongodb` - etap zapisujący ofertę do bazy MongoDB.
-   `pracuj_pipeline` - pipeline wykorzystywany do ekstrakcji z oferty
    niezbędnych cech, takich jak tagi z technologiami wymienionymi w opisie
    oferty.


## Testy jednostkowe

Aby uruchomić testy jednostkowe, w konsoli należy wpisać polecenie `tox`.
Poniżej znajduje się opis testów z pliku
`jobsbrowser/tests/api/test_api_resources.py`:

-   `test_ping_resource_returns_pong` - test sprawdza czy endpoint */pong*
    (który jest wykorzystywany do sprawdzania czy usługa API jest aktywna)
    zwraca odpowiedź ze statusem 200 oraz wartością "pong".
-   `test_add_offer_resource_try_add_offer_to_mongo_db` - test sprawdza czy
    wysłana poprzez zapytanie POST oferta próbuje być zapisana do bazy danych.
-   `test_get_offers_resource_query_mongo_db` - test sprawdza czy
    po wykonaniu zapytania HTTP GET na endpoint */offers* wykonywana jest próba
    pobrania danych z bazy danych.
-   `test_update_offer_resource_query_mongo_db` - test sprawdza czy
    po wykonaniu zapytania HTTP PUT na endpoint /offer wykonywana
    jest próba pobrania oferty oraz uaktualnienia jej w bazie.
    
    
Oraz tych dotyczących łańcucha przetwarzania:

-   `pipeline.tasks.test_preprocess.py` - plik z testami etapów
    przygotowujących oferty do ekstrakcji technologii.
    -   `TestDetectLanguage` - klasa zawierająca metody testujące etap
        detekcji języka w którym napisane jest ogłoszenie.
    -   `test_prepare_extract_proper_fields_from_offer` - test sprawdzający
        czy etap przygotowujący ofertę, tworzy oraz wybiera odpowiednie
        pola z całej oferty.
    -   `test_remove_stopwords_return_tokens_without_stopwords` - test
        weryfikujący poprawne usunięcie tokenów będących słowami nieistotnymi.
    -   `test_strip_html_tags_return_tokens_without_html_tags` - test
        sprawdzający czy etap poprawnie usuwa tagi HTML.
    -   `test_tokenize_return_list_of_lowercase_tokens` - test sprawdzający
        czy etap zwraca odpowiednią listę tokenów składających się
        z małych liter.
-   `pipeline.tasks.test_process.py` - plik z testami etapów wykonujących
    ekstrakcje technologii z oferty.
-   `pipeline.tasks.test_postprocess.py` - plik z testami etapów wykonujących
    zadania po wykonaniu ekstrakcji technologii.