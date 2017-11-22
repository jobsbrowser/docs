# Schemat architektury

Przewidziana architektura ma strukturę modułową. Schemat komponentów
oraz ich połączenie przedstawia załączony na końcu sekcji diagram.

W systemie wyróżnić możemy cztery główne, niezależne od siebie (na tyle że
mogą, a nawet powinny, być uruchamiane na różnych maszynach) moduły.
Ta sekcja zawiera ich ogólny, wysokopoziomowy opis. Szczegóły dotyczące
architektury i implementacji znajdują się w następnym rozdziale.


## Moduł zbierający dane
Komponent ten odpowiada za automatyczne pobieranie ogłoszeń z serwisu
zewnętrznego. Jest to program, który cyklicznie łączy się z udostępniającym
ogłoszenia serwisem i automatycznie pobiera ich treść. Z pobranych ogłoszeń
w najprostszy sposób (poprzez analizę kodu HTML) wyłuskuje podstawowe elementy,
takie jak:

+ Tytuł ogłoszenia
+ Treść
+ Data dodania
+ Pracodawca
+ Miejsce pracy

W kolejnym kroku tak "rozbite" ogłoszenie przesyła do kolejnego komponentu
systemu.

Opisany proces nie obejmuje zapisu do żadnej bazy danych.
W tej kwestii moduł zbierający dane polega całkowicie na komponencie,
do którego przekazuje pobrane ogłoszenia. To samo dotyczy kwestii
rozpoznawania duplikatów - program przed każdym rozpoczęciem skanowania
prosi swojego "odbiorcę" o listę już zeskanowanych ogłoszeń aby uniknąć
przetwarzania ich ponownie.


## Pipeline
Zebrane ogłoszenia trafiają do komponentu *Pipeline* (Łańcucha przetwarzania).
Nazwa komponentu odnosi się do zasady jego działania.
Odbierane ogłoszenia przekazywane są przez kolejne podmoduły, które wykonują na
nich stosowne operacje.

Pierwszym elementem jest moduł przechowujący dane. Odbiera on nowe ogłoszenia
od modułu zbierającego i zapisuje je w bazie danych. Jednocześnie oferuje
usługę odczytania listy kluczy (adresów URL) dodanych już ogłoszeń, z czego
moduł zbierający korzysta przed rozpoczęciem skanowania serwisu zewnętrznego.

Następnie ogłoszenia trafiają do modułu ekstrakcji kluczy. Tutaj zgodnie
z wymaganiami funkcjonalnymi systemu z ogłoszenia wyłuskane są elementy z trzech
kategorii:

+ Obszar branży IT którego dotyczy ogłoszenie
+ Stanowisko
+ Technologie i umiejętności

Po ukończeniu procesu model obiekt ogłoszenia powiększa się o zestaw kluczy,
a następnie zostaje wysłany do kolejnego komponentu.


## Backend
Moduł ten zajmuje się dostarczaniem użytkownikowi (a konkretnie aplikacji WWW)
informacji na podstawie przeanalizowanych ofert. Do bazy danych zapisywane
są ogłoszenia wraz z kluczami, a podmoduły pozwalają na jej odpytywanie.

Moduł wyszukiwarki wystawia interfejs pozwalający przeglądarce na wykonanie
zapytania o ogłoszenia zawierające jednej lub więcej kluczy.

Interfejs modułu statystyk pozwala na dostęp do statystyk systemu jako
całości oraz statystyk poszczególnych kluczy. Bardziej szczegółowe wymagania
tego interfejsu znajdują się w sekcji wymagań funkcjonalnych.


## Aplikacja WWW
Ostatnim elementem systemu, jedynym dostępnym bezpośrednio dla użytkownika
jest aplikacja WWW. Nie posiada ona własnej bazy, a co za idzie kont
użytkowników. Korzysta wyłącznie z interfejsu wyszukiwania oraz statystyk
pozwalając użytkownikowi na przejrzysty i wygodny dostęp do informacji.

![Diagram komponentów. \label{ref_a_figure}](source/figures/components_diagram.png){ width=100% }

\clearpage
