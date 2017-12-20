# Integracja z kolejnym modułem

Początkowe plany zakładały użycie w tym miejscu (po dodaniu oferty do bazy)
frameworka *Luigi*. Jest to stworzone przez twórców aplikacji *Spotify* narzędzie
do łączenia ze sobą kolejnych funkcji / etapów tworząc łańcuch przetwarzania (
wspomniany w kilku miejscach tzw. *Pipeline*). Okazało się jednak, że przewidziane
zastosowania narzędzia obsługują etapy nieco innego typu niż te do zaimplementowania
w module ekstrakcji kluczy. Luigi przeznaczony jest bowiem do łączenia bardzo
wymagających zadań, angażujących wiele zewnętrznych usług czy języków programowania
i wykonujących się nawet kilka dni. W efekcie nie udostępnia chociażby tak podstawowej
w mniejszych zastosowaniach możliwości, jak uruchamianie zadania z poziomu kodu
źródłowego. W grę wchodzi jedynie linia poleceń. Zdecydowaliśmy się więc na
porzucenie go, na rzecz frameworka *Celery* którego obsługa zadań jest tym
czego potrzebujemy. Stracimy co prawda na odporności na awarie (Luigi zapisuje
stan po każdym zadaniu, i wraca do niego po awarii), lecz zdecydowanie
zyskamy na łatwości implementacji.

Użycie frameworka Celery jest częścią kolejnego modułu, tj. modułu ekstrakcji
kluczy, więc to tam znajdzie się dotycząca tej kwestii dokumentacja.