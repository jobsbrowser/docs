# Uruchomienie i użytkowanie

W katalogu `jobsbrowser` repozytorium znajduje się wykonywalny skrypt `run.sh`.
Nie przyjmuje on żadnych parametrów, a jego uruchomienie powoduje uruchomienie
procesu scraper'a. W celu cyklicznego uruchamiania, zalecamy skorzystanie
z menadżera *cron*.

Za pomocą parametru `--log-level=LOG_LEVEL`, gdzie LOG_LEVEL może przyjąć jedną
z poniższych wartości(wartości wymienione są od najmniej restrykcyjnej do najbardziej):

-   DEBUG
-   INFO
-   WARNING
-   ERROR
-   CRITICAL

Innym użytecznym parametrem podczas weryfikowania działania scraper'a jest
`-o/--output filename.EXTENSION`, gdzie EXTENSION może przyjąć jedną z niżej
wymienionych wartości:

-   json
-   jl (json lines) każda linia jest oddzielnym obiektem JSON
-   csv

Po podaniu tego parametru wszystkie dane zebrane przez scraper zostaną zapisane
do podanego pliku w wybranym na podstawie rozszerzenia formacie.

W pliku `jobsbrowser/jobsbrowser/settings.py` znajdują się ustawienia programu.
Większość z nich to ustawienia framework'a Scrapy. Ich opis znaleźć można
w jego dokumentacji[@scrapy]. Ustawieniami dotyczącymi
konkretnie tego projektu są `STORAGE_SERVICE_ADD_URL` oraz `STORAGE_SERVICE_RETRIEVE_URL`,
które oznaczają adresy URL pod który program może wykonać żądania w celu odpowiednio,
dodania nowo przetworzonej strony oraz uzyskania listy adresów URL ofert których
nie powinien przetwarzać.
