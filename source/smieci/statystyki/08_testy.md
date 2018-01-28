# Testy

## Testy jednostkowe

Aby uruchomić testy jednostkowe w konsoli należy wpisać polecenie
`python manage.py test`.

Testy jednostkowe znajdują się w pliku `offers/offers.py` i objemują klasy oraz metody
implementujące logikę widoków znajdujących się w pliku `offers/views.py`.

## Testy akceptacyjne
Moduł oferuje funkcjonalność serwera backendowego, brak jest w nim jakiejkolwiek
warstwy wizualnej. Możliwość sprawdzenia poprawności działania sprowadza się więc
do wykonania zapytań HTTP z odpowiednimi parametrami oraz sprawdzenia odpowiedzi.


![Wyszukiwanie ofert. \label{ref_a_figure}](source/figures/search_screen.png){ width=100% }


![Generowanie statystyk. \label{ref_a_figure}](source/figures/stats_screen.png){ width=100% }

\clearpage

![Statystyki zbiorcze. \label{ref_a_figure}](source/figures/info_screen.png){ width=100% }

\clearpage