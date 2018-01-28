# Schemat

Przewidziana architektura ma strukturę modułową. Ogólny schemat komponentów
oraz ich połączenie przedstawia załączony diagram (Rys. \ref{components_diagram}),
natomiast bardziej szczegółowy opis każdego z nich znajduje się w dalszej części tego rozdziału.

W systemie wyróżnić możemy trzy główne, niezależne od siebie (na tyle że
mogą, a nawet powinny, być uruchamiane na różnych maszynach) moduły.

**Robot zbierający dane**

Komponent ten, nazywany też *scraperem*, odpowiada za automatyczne pobieranie
ogłoszeń. Jest to program, który cyklicznie łączy się z udostępniającym
ogłoszenia serwisem i automatycznie pobiera ich treść. Zebrane oferty
przesyła do kolejnego komponentu systemu.

**Moduł analityczny**

Stosowaną zamiennie nazwą jest *Pipeline* - czyli *łańcuch przetwarzania*.
Odbiera on zebrane ogłoszenia, a następnie wykonuje na nich
sekwencję operacji obejmujących zapis do bazy danych czy wykrycie zawartych w treści
technologii. Komponent ten jest również odpowiedzialny za komunikację z aplikacją WWW,
generując wyświetlane przez nią dane.

**Aplikacja WWW**

Ostatnim elementem systemu, jedynym dostępnym bezpośrednio dla użytkownika
jest aplikacja WWW. Nie posiada ona własnej bazy, a co za idzie kont
użytkowników. Komunikuje się z modułem analitycznym, 
pozwalając użytkownikowi na przejrzysty i wygodny dostęp do informacji.

![Diagram komponentów. \label{components_diagram}](source/figures/components_diagram.png){ width=100% }

\clearpage
