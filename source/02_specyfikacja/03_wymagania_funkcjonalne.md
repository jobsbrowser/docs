# Wymagania funkcjonalne

Podstawą interakcji użytkownika z systemem jest strona WWW - użytkownik powinien
być w stanie otworzyć ją na dowolnym komputerze z dostępem do internetu, 
wyposażonym w przeglądarkę:

+ Google Chrome w wersji 49 lub wyższej
+ Mozilla Firefox w wersji 52 lub wyższej
+ Safari w wersji 10.1 lub wyższej

Posiadanie przeglądarki innej niż wymienione lub w starszej wersji nie oznacza
że strona nie będzie działać, jednak nie da się zagwarantować
że będzie to działanie w pełni poprawne.

Na stronie nie przewidziano kont użytkowników, nawet administracyjnego. Każdy
z odwiedzających ma dostęp do tych samych danych oraz takie same
możliwości.

Funkcjonalność aplikacji WWW rozbita jest na trzy podstrony:

+ statystyki technologii
+ wyszukiwanie ofert 
+ informacje o systemie

Możliwości użytkownika w obrębie każdej z sekcji prezentuje załączony diagram 
przypadków użycia (Rys. \ref{use_case_diagram}).


## Wyświetlenie statystyk technologii

Jest to pierwsza podstawowa funkcjonalność strony. Pozwala
ona użytkownikowi na wybór jednej bądź kilku (przy pomocy auto-uzupełniania)
technologii oraz wyświetlenie:

+ w przypadku wybrania więcej niż jednej technologii, wykresu porównującego z osobna
  ich popularność (pod względem ilości ofert)
+ wykresu ilości ofert zawierających każdą z wybranych technologii
+ wykresu procentowej ilości ofert z systemu zawierających te technologie
+ wykresu kołowego przedstawiającego najczęściej poszukujących wybranych technologii
  pracodawców
+ listy dziesięciu najbardziej zbliżonych technologii


## Wyszukiwanie ofert wg technologii

Kolejną oferowaną użytkownikom możliwością jest wyszukiwanie ofert zebranych
i umieszczonych w bazie. Rolę kryterium wyszukiwania, podobnie jak podczas
przeglądania statystyk, pełni jedna lub więcej wybranych technologii. Rezultatem
jest lista ogłoszeń oraz przycisk oferujący możliwość ich eksportu w formacie JSON.

Każdą z ofert widocznych na liście można rozwinąć, uzyskując dostęp do następujących informacji:

+ tytuł oferty
+ data dodania i wygaśnięcia oferty w macierzystym serwisie
+ nazwa pracodawcy i miejsce pracy
+ wszystkie wykryte w treści oferty technologie
+ odnośnik do oryginalnego ogłoszenia w macierzystym serwisie


## Wyświetlenie informacji o systemie

W osobnej sekcji użytkownik ma dostęp do wyświetlenia zbiorczych statystyk
dotyczących serwisu i dostępnych w nim danych. Zbiór dostępnych statystyk
sprowadza się do:

+ liczby wszystkich ofert w bazie systemu
+ wykresu powyższej wartości względem czasu
+ daty ostatniego zebrania danych z serwisu macierzystego


![Przypadki użycia. \label{use_case_diagram}](source/figures/usecase_diagram.png){ width=100% }

\clearpage