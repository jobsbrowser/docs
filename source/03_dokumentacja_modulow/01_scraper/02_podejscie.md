# Podejście

Zadaniem stojącym przed scraperem jest automatyczne przejście po wszystkich
dostępnych stronach listy, wyłuskanie zeń adresów poszczególnych ofert, a
stamtąd wszystkich potrzebnych informacji. Pobrane ogłoszenie z wydzielonymi
fragmentami powinno trafić do innego komponentu systemu, który zajmie się jego
zapisem czy dalszym przetwarzaniem.

Ofert w serwisie wraz z upływem czasu będzie przybywać - i dla naszego systemu
jest to bardzo istotne. Aby zapewnić stały przypływ ogłoszeń z serwisu Pracuj.pl
scraper został tak przygotowany, aby mógł być uruchamiany cyklicznie.
Przewidzianym interwałem jest 12 godzin, choć nie jest to wartość zdefiniowana
w programie. To od uruchamiającego program na komputerze zależy jak ją ustawi.

Uruchomienie cykliczne wraz z brakiem stanu (bo przecież wszystkie przetworzone
ogłoszenia trafiają do osobnego modułu) wiąże się z możliwością niechcianego
przetwarzania jednej oferty wielokrotnie - przy każdym kolejnym uruchomieniu
programu. Zdecydowaliśmy się na rozwiązanie tego programu przez zaimplementowanie
w scraperze możliwości pobrania z modułu do którego trafią dane kluczy (adresów URL)
tych danych które już tam są. Oznacza to, że scraper przy każdym uruchomieniu
przetworzy wszystkie dostępne strony, ale nie będzie pobierał ani przetwarzał podstron ofert które
już ma na liście. Próba pobrania listy wykonywana jest po uruchomieniu programu,
przed rozpoczęciem skanowania. Jeżeli nie uda się jej otrzymać (serwer nie odpowie,
lub odpowie z błędem), program wypisze w konsoli stosowny komunikat ostrzegający
i przejdzie do przetwarzania wszystkich ofert.
