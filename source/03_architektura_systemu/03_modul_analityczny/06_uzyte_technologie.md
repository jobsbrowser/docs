# Wykorzystane technologie


**Flask**

Licencja: BSD3

Flask jest napisanym w języku Python mikro-frameworkiem. Głównym jego zastosowaniem
jest tworzenie niewielkich aplikacji sieciowych czy REST API. Posiada wbudowany
serwer deweloperski i debugger. Stawia duży nacisk na zwięzłość kodu, co pozwala
na szybkie prototypowanie ale i późniejsze rozwijanie aplikacji.


**Django**

Licencja: BSD3

Jest to jeden z największych i najszybciej rozwijanych projektów Open Source.
Zdecydowaliśmy się na niego ze względu na to, że w tym module kluczowa jest
wydajność generowania odpowiednich statystyk, ale też duża elastyczność
w pisaniu kodu. Ważną zaletą Django jest wbudowany ORM który znacząco ułatwia
współpracę z bazą danych.


**Celery (i Luigi)**

Licencja: BSD3

Celery[@celery] jest asynchroniczną kolejką zadań.
Zadania są dystrybuowane do kolejki z różnych źródeł, np. z aplikacji sieciowej.
Celery jest przeznaczone głównie do operacji zlecanych oraz wykonywanych w
czasie rzeczywistym. Jako kolejkę lub bazę na zlecone zadania możliwe jest
wykorzystanie wielu backendów np. redis czy rabbitmq.

Początkowe plany zakładały użycie w tym miejscu
frameworka **Luigi**[@luigi]. Jest to stworzone przez twórców aplikacji *Spotify* narzędzie
do łączenia ze sobą kolejnych funkcji / etapów, tworząc łańcuch przetwarzania (*Pipeline*).
Okazało się jednak, że przewidziane
zastosowania narzędzia obsługują etapy innego typu niż te wymagane przez proces
ekstrakcji technologii. Luigi przeznaczony jest do łączenia
wymagających zadań, angażujących wiele zewnętrznych usług czy języków programowania
i wykonujących się nawet kilka dni. W efekcie nie udostępnia chociażby tak podstawowej
w mniejszych zastosowaniach możliwości jak uruchamianie zadania z poziomu kodu
źródłowego. Możliwe jest uruchamianie ich jedynie za pomocą linii poleceń.

Zdecydowaliśmy się na porzucenie Luigiego na rzecz frameworka *Celery*, którego obsługa zadań jest tym
czego potrzebujemy. Minusem takiego wyboru jest utrata odporności na awarie (Luigi zapisuje
stan po każdym zadaniu i wraca do niego po awarii), lecz dużym zyskiem jest zwiększona
łatwość implementacji.

