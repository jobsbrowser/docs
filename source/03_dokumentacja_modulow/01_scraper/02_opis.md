# Opis

Poniżej przentujemy drzewo katalogów oraz plików projektu wraz z krótkim
omówieniem:

```bash
├── jobsbrowser
│   ├── jobsbrowser
│   │   ├── __init__.py
│   │   ├── items.py         # definicje klas przechowujących zebrane dane
│   │   ├── loaders.py       # definicje klas ładujących zebrane dane
│   │   ├── middlewares.py
│   │   ├── pipelines.py     # definicje kolejnych etapów przetwarzania danych
│   │   ├── settings.py      # ustawienia pająków
│   │   └── spiders          # katalog z definicjami pająków zbierających dane
│   │       ├── __init__.py
│   │       └── pracuj.py    # definicja pająka zbierającego dane ze strony pracuj.pl
│   ├── run.sh               # plik wykonywalny uruchamiający proces zbierania danych
│   └── scrapy.cfg           # konfiguracja całego projektu
└── requirements.txt         # plik z wymaganiami projektu
```


Poniżej znajduje się opis użytych w projekcie klas:

-   **JobBrowserItem** - klasa bazowa definiująca pola które powinny być
    dostaraczane przez wszyskie spider'y wykorzystywane w projekcie.
-   **PracujItem** - klasa przechowująca pola które muszą zostać wypełnione przez
    scrapery zbierające dane ze strony pracuj.pl.
-   **JobsBrowserPipeline** - klasa która po zebraniu danych ze stron wysyła
    dane do modułu zapisy do bazy danych.
-   **JobsBrowserSpiderMiddleware** - klasa wygenerowana automatycznie podczas
    tworzenia projektu za pomocą Scrapy'ego.
-   **PracujItemLoader** - klasa przetwarzająca w prosty sposób zebrane dane.
-   **PracujSpider** - klasa wykonująca requesty do serwisu pracuj.pl oraz
    zbierająca dane.

Moduł Scraper'a komunikuje się bezpośrednio jedynie z modułem zapisu do
bazy danych. Po pobraniu oferty pracy ze strony oraz wyciągnieciu z niej
potrzebnych danych moduł Scraper'ów wysyła request HTTP do modułu zapisu
do bazy danych w celu zapisania właśnie zebranych danych.
Komunikacja w drugą stronę ma na celu pobranie od modułu bazy danych
informacji o URL'ach ogłoszeń z ostatniego okresu czasu aby nie wykonywać
niepotrzebnych zapytań HTTP o już wcześniej przetwarzane oferty pracy
tym samym nie obciążając niepotrzebnie serwerów serwisów z ogłoszeniami
o pracę.
