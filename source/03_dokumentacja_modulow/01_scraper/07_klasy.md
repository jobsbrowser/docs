# Główne klasy modułu

-   **JobBrowserItem** - klasa bazowa definiująca pola które powinny być
    dostarczane przez wszystkie spider'y wykorzystywane w projekcie.
-   **PracujItem** - klasa przechowująca pola które muszą zostać wypełnione przez
    scraper'y zbierające dane ze strony pracuj.pl.
-   **JobsBrowserPipeline** - klasa która po zebraniu danych ze stron wysyła
    dane do modułu zapisy do bazy danych.

    -   `process_item` - metoda w której za pomocą zapytania HTTP wysyłany jest
        aktualnie przetwarzany element(Item) do modułu bazy danych.

-   **JobsBrowserSpiderMiddleware** - klasa wygenerowana automatycznie podczas
    tworzenia projektu za pomocą Scrapy'ego.
-   **PracujItemLoader** - klasa przetwarzająca w prosty sposób zebrane dane.

    -   `load_item` - wykonuje wszystkie operacje zdefiniowane w deskryptorach
        na aktualnie przetwarzanym elemencie

-   **PracujSpider** - klasa wykonująca zapytania do serwisu pracuj.pl oraz
    zbierająca dane.

    -   `start_urls` - adresy URL od których zaczynane jest zbieranie danych.
    -   `rules` - zasady definiujące jakie elementy są ofertami oraz jak
        przejść do następnej strony z ofertami.
    -   `already_parsed_links` - linki do ofert znajdujących się już w bazie.
    -   `filter_links` - metoda sprawdzająca czy ogłoszenia z danej strony
        nie są już w bazie. Zwraca nowe ogłoszenia.
    -   `parse_item` - zajmuje się wyciągnięciem potrzebnych danych z aktualnie
        przetwarzanej strony za pomocą PracujItemLoader'a.
