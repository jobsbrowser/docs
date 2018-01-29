# Napotkane problemy

Zadaniem stojącym przed scraperem jest automatyczne przejście po wszystkich
dostępnych stronach listy, wydobycie z nich adresów poszczególnych ofert, a
stamtąd wszystkich potrzebnych informacji. Pobrane ogłoszenie z wydzielonymi
fragmentami powinno trafić do innego komponentu systemu, który zajmie się jego
zapisem czy dalszym przetwarzaniem. Podczas prac nad modułem wynikło kilka
kwestii które wymagały opracowania konkretnego rozwiązania.


**Aktualizacja ofert w serwisie**

Ofert na stronie wraz z upływem czasu będzie przybywać - dla działającego systemu
jest to bardzo istotne. Aby zapewnić stały przypływ ogłoszeń z serwisu Pracuj.pl
scraper został tak przygotowany, aby mógł być uruchamiany cyklicznie.
Przewidzianym interwałem są 24 godziny, choć nie jest to wartość na stałe zdefiniowana
w programie. To od uruchamiającego system zależy jak ją ustawi.


**Utrzymywanie stanu scrapera**

Uruchomienie cykliczne wraz z brakiem stanu (bo przecież wszystkie przetworzone
ogłoszenia trafiają do osobnego modułu) wiąże się z możliwością niechcianego
przetwarzania jednej oferty wielokrotnie - przy każdym kolejnym uruchomieniu
programu. Rozwiązaniem okazało się zaimplementowanie
w scraperze możliwości pobrania z modułu do którego trafią dane kluczy (adresów URL)
tych danych które już tam są. Oznacza to, że scraper przy każdym uruchomieniu
przetworzy wszystkie dostępne strony, ale nie będzie pobierał ani przetwarzał
podstron ofert które już ma na liście. Próba pobrania listy wykonywana jest po
uruchomieniu programu, przed rozpoczęciem skanowania. Jeżeli nie uda się jej
otrzymać (serwer nie odpowie, lub odpowie z błędem), program wypisze w konsoli
stosowny komunikat ostrzegający i przejdzie do przetwarzania wszystkich ofert.


**Struktura danych**

Początkowo dane pobierane były z wersji portalu Pracuj.pl przeznaczonej dla
urządzeń o wyższej rozdzielczości ekranu (Laptopy, komputery PC). Problemem okazała
się jednak niejednolita struktura danych, utrudniająca automatyczne wydobywanie
informacji z treści ogłoszenia. Rozwiązaniem okazało się korzystanie z wersji
portalu przeznaczonej dla urządzeń mobilnych.