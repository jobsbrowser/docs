# Uruchomienie i użytkowanie

W katalogu `jobsbrowser` repozytorium znajduje się wykonywalny skrypt `run.sh`.
Nie przyjmuje on żadnych parametrów, a jego uruchomienie powoduje uruchomienie
procesu scrapera. W celu cyklicznego uruchamiania, zalecamy skorzystanie
z menadżera *cron*.

W pliku `jobsbrowser/jobsbrowser/settings.py` znajdują się ustawienia programu.
Większość z nich to ustawienia framework'a Scrapy. Ich opis znaleźć można
w jego dokumentacji. (*Tutaj bibliografia*). Ustawieniami dotyczącymi
konkretnie tego projektu są `STORAGE_SERVICE_ADD_URL` oraz `STORAGE_SERVICE_RETRIEVE_URL`,
które oznaczają adresy URL pod który program może wykonać żądania w celu odpowiednio,
dodania nowo przetworzonej strony oraz uzyskania listy adresów URL ofert których
nie powinien przetwarzać.