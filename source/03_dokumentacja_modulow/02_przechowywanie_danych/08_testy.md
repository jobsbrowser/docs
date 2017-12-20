# Testy

## Testy jednostkowe

Aby uruchomić testy jednostkowe, w konsoli należy wpisać polecenie `pytest`.
Poniżej przedstawiamy opis testów znajdujących się w pliku
`jobsbrowser/tests/test_api_resources.py`:

-   `test_ping_resource_returns_pong` - test sprawdza czy endpoint */pong*
    (który jest wykorzystywany do sprawdzania czy usługa API jest aktywna)
    zwraca odpowiedź ze statusem 200 oraz wartością "pong".
-   `test_add_offer_resource_try_add_offer_to_mongo_db` - test sprawdza czy
    wysłana poprzez zapytanie POST oferta próbuje być zapisana do bazy danych.
-   `test_get_offers_resource_query_mongo_db` - test sprawdza czy
    po wykonaniu zapytania HTTP GET na endpoint */offers* wykonywana jest próba
    pobrania danych z bazy danych.
    
  
## Testy akceptacyjne

Interfejs modułu zbierania danych jest dość ubogi. Zajmuje się on bowiem
jedynie dodawaniem ofert oraz zwracaniem informacji o adresach URL tych już
istniejących. Test jaki możemy przeprowadzić aby upewnić się moduł działa
poprawnie może więc polegać na:

+ Uruchomieniu usługi wg instrukcji z dokumentacji
+ Wykonaniu zapytania o listę ofert (powinna być pusta)
+ Wykonaniu żądania dodającego nową ofertę
+ Wykonaniu zapytania o listę ofert raz jeszcze. Powinniśmy otrzymać adres URL
  przesłany w poprzednim kroku.
  
  
\clearpage

![Uruchomienie serwera \label{ref_a_figure}](source/figures/db_test_1.png){ width=100% }

![Pierwsze zapytanie o listę \label{ref_a_figure}](source/figures/db_test_2.png){ width=100% }

\clearpage

![Dodanie nowej oferty \label{ref_a_figure}](source/figures/db_test_3.png){ width=100% }

![Ponowne zapytanie o listę \label{ref_a_figure}](source/figures/db_test_4.png){ width=100% }

\clearpage


