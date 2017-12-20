# Struktura kodu

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
