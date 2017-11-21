# Główne klasy modułu

-   **JobBrowserItem** - klasa bazowa definiująca pola które powinny być
    dostarczane przez wszystkie spider'y wykorzystywane w projekcie.
-   **PracujItem** - klasa przechowująca pola które muszą zostać wypełnione przez
    scrapery zbierające dane ze strony pracuj.pl.
-   **JobsBrowserPipeline** - klasa która po zebraniu danych ze stron wysyła
    dane do modułu zapisy do bazy danych.
-   **JobsBrowserSpiderMiddleware** - klasa wygenerowana automatycznie podczas
    tworzenia projektu za pomocą Scrapy'ego.
-   **PracujItemLoader** - klasa przetwarzająca w prosty sposób zebrane dane.
-   **PracujSpider** - klasa wykonująca zapytania do serwisu pracuj.pl oraz
    zbierająca dane.