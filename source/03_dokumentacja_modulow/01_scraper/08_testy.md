# Testy

W kodzie źródłowym modułu znajdują się testy jednostkowe pozwalające na
przetestowanie poprawności zaimplementowanych metod i funkcji. W tej sekcji
znajduje się również opis przykładowego scenariusza testów akceptacyjnych.
Testów integracyjne na tym etapie nie są jeszcze przewidziane. Moduł zbierania
danych jest pierwszym modułem i bez implementacji pozostałych ich wykonanie
jest niemożliwe.


## Testy jednostkowe

Aby uruchomić testy jednostkowe w konsoli należy wpisać polecenie
`pytest`.

Poniżej przedstawiamy listę plików z testami jednostkowymi oraz opis
poszczególnych funkcji lub metod:

-   `test_pracuj_item_loader.py` - plik z testami klasy PracujItemLoader.
    -   `test_taking_first_from_each_field` - test sprawdza czy żaden z
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


## Testy akceptacyjne

Moduł zbierania danych zajmuje się, jak mówi sama nazwa, jedynie ich zbieraniem.
Domyślnie nie są one nigdzie przechowywane, ani zapisywane. Podejście takie
utrudnia nieco przygotowanie testów akceptacyjnych obejmujących wyłącznie
ten komponent, ale nie uniemożliwia, co zaraz wykażemy.
