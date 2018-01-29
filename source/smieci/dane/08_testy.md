# Testy

## Testy jednostkowe


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


