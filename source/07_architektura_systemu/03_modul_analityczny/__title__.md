\clearpage

# Moduł analityczny \label{modul_analityczny}

Kod źródłowy znajduje się w repozytoriach:

+ [\url{github.com/jobsbrowser/pipeline}](https://github.com/jobsbrowser/pipeline)
+ [\url{github.com/jobsbrowser/backend}](https://github.com/jobsbrowser/backend)


Modułem systemu do którego trafiają przetwarzane oferty w następnej kolejności jest
moduł analityczny. To tutaj odbywa się, kluczowy z punktu widzenia biznesowego
zastosowania projektu, proces ekstrakcji ze zbieranych ofert wartościowych informacji.
Wejściem modułu są pobierane z serwisu Pracuj.pl oferty, natomiast rolę wyjścia pełni
interfejs HTTP z którego korzysta aplikacja WWW.

Moduł ten rozdzielony jest na dwa komponenty - pierwszym z nich jest usługa
obsługująca robota zbierającego dane. Przyjmuje ona pobrane oferty, roboczo
zapisuje je w nierelacyjnej bazie danych, a następnie dla każdej z nowo
dodanych rozpoczyna sekwencyjny proces analizy. Przetworzone ogłoszenia
trafiają w ostatnim kroku tego procesu do drugiego komponentu, którym jest
usługa obsługująca aplikację WWW. W odrębnej, już relacyjnej, bazie danych
zapisuje ona najważniejsze informacje o przetworzonych ofertach oraz, co najważniejsze,
listę technologii które udało się w nich wykryć.