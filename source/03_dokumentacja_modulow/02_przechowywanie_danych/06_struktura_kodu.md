# Struktura kodu

Poniżej prezentujemy drzewo katalogów oraz plików modułu wraz z krótkim
omówieniem.

```bash
├── jobsbrowser
│   ├── api	                       # katalog modułu API
│   │   ├── __init__.py
│   │   ├── resources.py           # definicja endpointów API
│   │   ├── settings.py            # ustawienia API
│   │   └── spec.yml               # specyfikacja API w standardzie OpenAPI(swagger)
│   ├── pipeline                   # moduł pipeline
│   └── __init__.py
├── manage.py                      # skrypt z pożytecznymi komendami dotyczącymi API
├── requirements.txt               # wymagane biblioteki modułu
├── setup.py
├── tests
│   ├── api                        # katalog z testami modułu API
│   │   ├── __init__.py
│   │   └── test_api_resources.py  # testy endpointów API
│   └── pipeline                   # katalog z testami modułu Pipeline
└── tox.ini                        # konfiguracja narzędzia używanego do testowania
```
