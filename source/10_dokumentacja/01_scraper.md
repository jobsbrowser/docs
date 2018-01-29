# Robot zbierający dane

Kod źródłowy tego modułu znajduje się na załączonej do pracy płycie DVD, w katalogu
`src/scraper/`.


## Struktura plików kodu źródłowego

Poniżej przedstawione jest drzewo katalogów oraz plików modułu, wraz z krótkim omówieniem:

```bash
├── jobsbrowser
│   ├── jobsbrowser
│   │   ├── __init__.py
│   │   ├── extractors.py    # definicje klas ekstraktujących linki z ofertami
│   │   ├── items.py         # definicje klas przechowujących zebrane dane
│   │   ├── loaders.py       # definicje klas ładujących zebrane dane
│   │   ├── loaders.py       # definicje klas ładujących zebrane dane
│   │   ├── middlewares.py
│   │   ├── pipelines.py     # definicje kolejnych etapów przetwarzania danych
│   │   ├── settings.py      # ustawienia pająków
│   │   └── spiders          # katalog z definicjami pająków zbierających dane
│   │       ├── __init__.py
│   │       └── pracuj.py    # definicja pająka zbierającego dane ze strony pracuj.pl
│   ├── tests/               # katalog z testami projektu
│   ├── run.sh               # plik wykonywalny uruchamiający proces zbierania danych
│   └── scrapy.cfg           # konfiguracja całego projektu
└── requirements.txt         # plik z wymaganiami projektu
```

## Opis klas i metod

-   **JobBrowserItem** - klasa bazowa definiująca pola które powinny być
    dostarczane przez wszystkie spider'y wykorzystywane w projekcie.
-   **PracujItem** - klasa przechowująca pola które muszą zostać wypełnione przez
    scraper'y zbierające dane ze strony pracuj.pl.
-   **JobsBrowserPipeline** - klasa, która po zebraniu danych ze stron wysyła
    dane do modułu analitycznego.

    -   `process_item` - metoda w której za pomocą zapytania HTTP wysyłany jest
        aktualnie przetwarzany element (oferta).

-   **JobsBrowserSpiderMiddleware** - klasa wygenerowana automatycznie podczas
    tworzenia projektu za pomocą Scrapy'ego.
-   **PracujLinkExtractor** - klasa wyciągająca linki do ofert pracy
    w serwisie pracuj.pl.
-   **PracujItemLoader** - klasa przetwarzająca w prosty sposób zebrane dane.

    -   `load_item` - wykonuje wszystkie operacje zdefiniowane w deskryptorach
        na aktualnie przetwarzanym elemencie.

-   **PracujSpider** - klasa wykonująca zapytania do serwisu pracuj.pl oraz
    zbierająca dane.

    -   `start_urls` - adresy URL od których zaczynane jest zbieranie danych.
    -   `rules` - zasady definiujące jakie elementy są ofertami oraz jak
        przejść do następnej strony z ofertami.
    -   `already_parsed_links` - linki do ofert znajdujących się już w bazie.
    -   `filter_link` - metoda sprawdzająca czy dane ogłoszenie
        nie jest już w bazie.
    -   `parse_item` - zajmuje się wyciągnięciem potrzebnych danych z aktualnie
        przetwarzanej podstrony
    -   `start_requests` - generuje zapytania HTTP do każdej strony z daną
        kategorią.


## Testy jednostkowe

Aby uruchomić testy jednostkowe w konsoli należy wpisać polecenie
`pytest`.

Poniżej znajduje się lista plików zawierających testy jednostkowe oraz opis
poszczególnych funkcji lub metod:

-   `test_pracuj_item_loader.py` - plik z testami klasy PracujItemLoader.
    -   `test_taking_first_from_each_field` - test sprawdza czy żadne z
        przetworzonych pól nie jest listą (Scrapy domyślnie zwraca wszystkie
        elementy jako listy, nawet tylko gdy znajduje się w nich jeden element.
    -   `test_offer_id_properly_extracted` - test sprawdza czy pole *offer_id*
        jest odpowiednio wydobywane z adresu URL strony.
    -   `test_remove_html_tags_from_employer_and_job_title_fields` - test
        sprawdza czy znaczniki HTML zostały poprawnie usunięte z wartości pól
        *employer* oraz *job_title*.

-   `test_jobsbrowser_pipeline.py` - plik z testami klasy JobsBrowserPipeline.
    -   `test_jobsbrowser_pipeline_process_item_send_request_to_db_module` - test
        sprawdza czy w metodzie `process_item` wykonywane jest zapytanie HTTP
        POST do serwera z działającym modułem bazy danych.

-   `test_pracuj_spider.py` - plik z testami klasy PracujSpider.
    -   `test_parse_item` - test sprawdza czy metoda prawidłowo wyciąga dane
        z adresu URL oraz treści strony, a następnie zwraca je w atrybutach
        obiektu typu PracujItem.
    -   `test_parse_on_page_with_multiple_next_pages` - test sprawdza czy metoda
        `parse` prawidłowo znajduje link do następnej strony z
        ofertami. Testowany w tej metodzie jest przypadek gdy istnieją kolejne
        strony.
    -   `test_parse_on_last_page` - test sprawdza czy metoda `parse` prawidłowo
        zachowuje się na ostatniej stronie z listingami ofert, czyli nie
        znajduje żadnych nowych linków, tym samym kończąc zbieranie danych.
