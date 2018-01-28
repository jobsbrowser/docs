# Dostęp do strony

Funkcjonalność serwisu uzależniona jest od ilości przetworzonych
ofert znajdujących się w bazie danych (świeżo uruchomiona instancja systemu będzie pusta).
Zalecane jest zatem korzystanie z oficjalnej wersji serwisu, dostępnej pod adresem
`http://jobsbrowser.pl` (2018-01-29).


# Zakładka statystyk
Jest to pierwsza zakładka którą jako użytkownik widzimy po wprowadzeniu
w przeglądarce adresu aplikacji. W górnej części strony znajduje się pasek
menu pozwalający na zmianę zakładki, a w środkowej pole do wpisywania kluczy.

Po wprowadzeniu klucza i wciśnięciu klawisza Enter zakoloruje się on, a pod
spodem pojawią się dwa wykresy. Wpisany klucz można usunąć lub dodać do niego
kolejny pisząc w polu i ponownie wciskając Enter.

Na pierwszym wykresie przedstawiona będzie ilość aktywnych ofert zawierających
dany klucz konkretnego dnia, a na drugim jaką procentowo część wszystkich
aktywnych wówczas ofert z branży IT one stanowiły. Wykresy są w pewnym stopniu
interaktywne. Tzn. nie pozwalają na zmianę skali czy zakresu, ale pozwalają
na dokładne zbadanie wartości w określonym dniu najeżdżając na wykres kursorem
myszy.


# Zakładka wyszukiwania
Drugą dostępną z menu zakładką jest ta z widokiem wyszukiwania.
Tutaj ponownie zobaczymy identyczne pole do wpisywania kluczy, jednak tym razem
pod spodem pojawi nam się lista znalezionych ofert które ten klucz zawierają.
Każdą z nich możemy rozwinąć żeby zobaczyć więcej informacji, w tym link do 
oryginalnego ogłoszenia czy pozostałe wykryte w ofercie klucze.
Lista jest paginowana, co zwiększa komfort użytkownika i poprawia szybkość
ładowania wyników.

Ogłoszenia na liście posortowane są wg daty ich wygaśnięcia (znaleźć na niej można
również ogłoszenia archiwalne). O statusie danej oferty informuje etykieta w prawym górnym rogu.


# Zakładka informacji
Ostatnią zakładką jest ta poświęcona informacjom o serwisie oraz statystykom
zbiorczym. Zobaczymy tam krótki opis projektu oraz wykres ilości wszystkich
przetworzonych przez niego ofert względem czasu.


\clearpage

![Zakładka statystyk z wybranym jednym tagiem. \label{stats_view}](source/figures/www_stats1.png){ width=100% }

![Wykres pracodawców i lista podobnych technologii. \label{pie_chart}](source/figures/www_stats2.png){ width=100% }

![Wykres porównania tagów z osobna. \label{tags_chart}](source/figures/www_stats3.png){ width=100% }

![Zakładka wyszukiwania. \label{ref_a_figure}](source/figures/www_search1.png){ width=100% }

![Rozwinięte ogłoszenie. \label{ref_a_figure}](source/figures/www_search2.png){ width=100% }

![Zakładka informacji. \label{ref_a_figure}](source/figures/www_info.png){ width=100% }

\clearpage
