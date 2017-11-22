# Struktura kodu źródłowego

Poniżej prezentujemy drzewo katalogów oraz plików projektu wraz z krótkim
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
│   ├── tests/               # katalog z testami projektu
│   ├── run.sh               # plik wykonywalny uruchamiający proces zbierania danych
│   └── scrapy.cfg           # konfiguracja całego projektu
└── requirements.txt         # plik z wymaganiami projektu
```
