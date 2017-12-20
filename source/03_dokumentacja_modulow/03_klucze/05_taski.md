# Etapy pipeline'a

Łańcuch przetwarzania ofert pobranych z serwisu `pracuj.pl` składa się
z następujących etapów:

-   wybranie odpowiednich pól z oferty
-   usunięcie tagów HTML z opisu oferty
-   podzielenie opisu oferty na tokeny
-   detekcja języka w jakim napisana jest oferta, w przypadku detekcji języka
    innego niż polski, w tym miejscu kończy się przetwarzanie oferty
-   usunięcie nieistotnych słów np. "tak", "więc"
-   znalezienie technologii(tagów) jakich dotyczy oferta
-   zapisanie przetworzonej oferty ze znalezionymi technologiami(tagami) do
    bazy danych MongoDB

# Struktura kodu

Poniżej prezentujemy drzewo katalogów oraz plików modułu wraz z krótkim
omówieniem.


```bash
├── jobsbrowser
│   ├── api                          # moduł przechowywania danych
│   ├── pipeline                     # moduł łańcucha przetwarzania danych
│   │   ├── _app.py
│   │   ├── chains.py                # konstrukcja łańcucha przetwarzania danych
│   │   ├── __init__.py
│   │   ├── settings.py              # ustawienia Celery oraz MongoDB
│   │   └── tasks                    # moduł poszczegołnych etapów pipeline
│   │       ├── bases.py             # bazowe klasy etapów
│   │       ├── exceptions.py        # wyjątki modułu etapów pipeline
│   │       ├── __init__.py
│   │       ├── postprocess.py       # etapy wykonywane na koniec pipeline
│   │       ├── preprocess.py        # etapy przygotowujące oferte to ekstrakcji cech
│   │       ├── process.py           # etapy ekstraktujące cechy, klucze z oferty
│   │       └── utils.py             # pożyteczne, mniejsze funkcje
│   └── __init__.py
├── requirements.txt
├── setup.py
├── tests                            # katalog z testami modułu
│   ├── api                          # katalog z testami modułu przechowywania danych
│   └── pipeline                     # katalog z testami modułu pipeline
│       ├── __init__.py
│       └── tasks                    # katalog z testami modułów etapów pipeline
│           ├── __init__.py
│           ├── test_process.py      # testy etapów ekstrakcji pipeline
│           ├── test_postprocess.py  # testy etapów końcowych pipeline
│           └── test_preprocess.py   # testy etapów początkowych pipeline
└── tox.ini                          # konfiguracja narzędzia używanego do testowania
```


# Główne klasy modułu

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
