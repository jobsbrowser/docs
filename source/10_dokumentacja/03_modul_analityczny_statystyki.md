# Moduł analityczny - podmoduł statystyk i wyszukiwarki

Kod źródłowy podmodułu znaleźć można w katalogu `src/analytics/backend`.

## Struktura plików kodu źródłowego

Zaprezentowana poniżej struktura plikóœ i katalogów odpowiada szablonowemu projektowi działającemu
z użyciem Django. Zdecydowaną większość funkcjonalności (filtrowanie, paginację,
serializowanie modeli, wyszukiwanie po atrybucie) zapewniły gotowe,
oferowane przez framework narzędzia.
Główna część logiki znajduje się w pliku `offers/views.py`
i jest to zoptymalizowane generowanie statystyk.

```bash
├── backend
│   ├── config                     # moduł ustawień (Django)
│   │   ├── __init__.py
│   │   ├── settings.py            # plik z ustawieniami
│   │   ├── urls.py                # konfiguracja adresów URL serwera
│   │   └── wsgi.py                # aplikacja WSGI (np. do integracji z Apache)
│   └── offers                     # moduł aplikacji
│       ├── migrations             # migracje (kod generujący schemat bazy danych na podstawie modeli)
│       └── __init__.py               
│       └── apps.py                
│       └── filters.py             # filtrowanie po tagach  
│       └── models.py              # modele oferty oraz technologii 
│       └── pagination.py          # paginacja (używana przy wyszukiwaniu ofert)   
│       └── serializers.py         # serializacja modeli
│       └── tests.py               # testy jednostkowe
│       └── views.py               # główna część logiki - implementacja interfejsu
├── manage.py                      # skrypt do zarządzania serwerem i jego uruchamiania
├── requirements.txt               # lista koniecznych do zainstalowania zależności
```


## Opis klas i metod

Najbardziej istotnymi klasami są:

- **Offer** - Model oferty. Tutaj zadeklarowane są pola stanowiące strukturę
tabeli w bazie danych.
- **Tag** - Model pojedynczej technologii. Zawiera jedynie pole na nazwę.
- **OffersListView** - klasa widoku obsługującego wyszukiwanie ofert.
- **OffersStatsView** - klasa widoku obsługującego generowanie statystyk
- **SystemInfoView** - klasa widoku obsługującego statystyki całościowe

każda z tych klas jest rozszerzeniem funkcjonalności oferowanych przez framework,
dziedzicząc po odpowiedniej klasie bazowej. Niezależnie zaimplementowana logika
znajduje się tylko w klasach **OffersStatsView** oraz **SystemInfoView**
w postaci odpowiednich metod. W pozostałych dostosowanie klasy oferowanej przez
framework sprowadza się do ustawienia odpowiednich atrybutów.


## Testy jednostkowe

Aby uruchomić testy jednostkowe w konsoli należy wpisać polecenie
`python manage.py test`.

Testy jednostkowe znajdują się w pliku `offers/offers.py` i obejemują klasy oraz metody
implementujące logikę widoków znajdujących się w pliku `offers/views.py`.