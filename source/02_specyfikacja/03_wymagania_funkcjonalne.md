# Wymagania funkcjonalne

Podstawą interakcji użytkownika jest strona WWW - użytkownik powinien
być w stanie otworzyć ją na dowolnym komputerze z dostępem do internetu
i wyposażonym w aktualną wersję jednej z wiodących na rynku przeglądarek.

+ Google Chrome w wersji 49 lub wyższej
+ Mozilla Firefox w wersji 52 lub wyższej
+ Safari w wersji 10.1 lub wyższej

Posiadanie przeglądarki innej niż wymienione, lub w starszej wersji nie oznacza
że strona nie będzie działać, jednak jako twórcy nie możemy zagwarantować
że będzie to działanie w pełni poprawne.

Na stronie nie przewidujemy kont użytkowników, nawet administracyjnego. Każdy
wchodzący na stronę będzie miał dostęp do tych samych danych oraz takie same
możliwości.

Funkcjonalność strony rozbita jest na dwa moduły. Moduł wyszukiwarki
oraz moduł statystyk. Możliwości użytkownika prezentuje diagram przypadków
użycia. 

![Przypadki użycia. \label{ref_a_figure}](source/figures/usecase_diagram.png){ width=100% }

\clearpage

## Wyszukiwanie ofert wg klucza

Jednym z podstawowych zastosowań strony jest wyszukiwanie ofert zebranych
i umieszczonych w bazie przez nasz system. Jako kryterium wyszukiwania
(przez mechanizm filtrowania) może zostać użyty tzw. *klucz*, czyli wyłuskana
z opisu ogłoszenia jego cecha. Klucze dzielimy na trzy kategorie:

+ **Obszary** (np. Mobile development, Helpdesk)
+ **Stanowiska** (np. Software Developer, Data Scientist)
+ **Technologie i umiejętności** (np. Java, Docker, AWS)

Pozwoli to na kompleksowe wyszukiwanie ofert ze względu na branżę
czy pozycję którą interesuje się użytkownik oraz posiadane przez niego
umiejętności. Możliwe jest podanie wielu kluczy jako kryterium.


## Wyświetlenie oferty

Wynikiem wyszukiwania jest lista ofert. Każdą z nich użytkownik może
wyświetlić uzyskując dostęp do takich informacji jak:

+ Tytuł oferty
+ Data dodania i wygaśnięcia oferty w macierzystym serwisie
+ Nazwa pracodawcy i miejsce pracy
+ Wszystkie wyłuskane przez system klucze
+ Odnośnik do oryginalnego ogłoszenia w macierzystym serwisie


## Wyświetlenie statystyk serwisu

W osobnej sekcji użytkownik ma dostęp do wyświetlenia zbiorczych statystyk
dotyczących serwisu i dostępnych w nim danych. Zbiór dostępnych statystyk
planowo zostanie rozwinięty podczas pracy nad ostatnimi dwoma modułami systemu.
Bazowe, przewidziane już teraz to:

+ Liczba wszystkich ofert w bazie systemu
+ Wykres powyższej wartości względem czasu
+ Datę ostatniego zebrania danych z serwisu macierzystego
+ Listę wszystkich istniejących w systemie kluczy


## Wyświetlenie statystyk klucza

Jest to druga obok wyszukiwania podstawowa funkcjonalność strony. Pozwala
ona użytkownikowi na wybór klucza oraz wyświetlenie:

+ Wykresu ilości ofert zawierających ten klucz względem czasu
+ Wykresu procentowej ilości ofert z systemu zawierających ten klucz
+ Pogrupowanych w kategorie kluczy które występują z tym kluczem
najczęściej w jednym ogłoszeniu

Możliwe jest podanie wielu kluczy. Wtedy pod uwagę przy generowaniu powyższych
statystyk będą brane tylko ogłoszenia które zawierają każdy z nich.