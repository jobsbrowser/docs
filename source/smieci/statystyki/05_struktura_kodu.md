# Struktura kodu

Poniżej prezentujemy drzewo katalogów oraz plików modułu wraz z krótkim
omówieniem. Struktura ta odpowiada szablonowemu projektowi działającemu
z użyciem Django. Zdecydowaną większość funkcjonalności (filtrowanie, paginację,
serializowanie modeli, wyszukiwanie po atrybucie) rozwiązaliśmy korzystając
z gotowych, oferowanych przez framework narzędzi.
Główna część logiki stworzonej przez nas znajduje się w pliku `offers/views.py`
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
│       └── models.py              # modele oferty oraz klucza 
│       └── pagination.py          # paginacja (używana przy wyszukiwaniu ofert)   
│       └── serializers.py         # serializacja modeli
│       └── tests.py               # testy jednostkowe
│       └── views.py               # główna część logiki - implementacja interfejsu
├── manage.py                      # skrypt do zarządzania serwerem i jego uruchamiania
├── requirements.txt               # lista koniecznych do zainstalowania zależności
```
