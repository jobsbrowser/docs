# Serwis zewnętrzny

Pracuj.pl dzieli zamieszczone w nim oferty na kategorie. My, z racji tematyki
pracy skupiamy się wyłącznie na trzech z nich:

+ Internet / e-Commerce / Nowe media
+ IT - Administracja
+ IT - Rozwój oprogramowania

Widok listy ogłoszeń w serwisie umożliwia wybór kategorii, z których ogłoszenia
chcemy zobaczyć. Skorzystaliśmy z tej możliwości, aby uzyskać bazowy link od
którego zaczniemy pobieranie ofert.

![Widok paginacji ogłoszeń w witrynie pracuj.pl. \label{ref_a_figure}](source/figures/pracuj_pagination_view.png){ width=100% }

\clearpage


Pracuj.pl przy zbiorczym  wyświetlaniu ofert używa paginacji. Oznacza to, że
scraper musi poradzić sobie nie tylko z pobieraniem podstron poszczególnych ofert,
ale też z poruszaniem się pomiędzy ponumerowanymi stronami listy.

Do każdej z ofert na stronie (których znajduje się ok. 50) prowadzi bezpośredni
link, który można wyłuskać z kodu HTML listy. Podstrona pojedynczej oferty
zawiera wszystkie interesujące nas informacje również możliwe do wyłuskania
z kodu HTML przy użyciu odpowiednich selektorów CSS. Dostępne w przystępny
sposób informacje to:

+ Data dodania oferty
+ Data wygaśnięcia
+ Nazwa dodającego (pracodawca)
+ Lokalizacja (miasto i województwo)
+ Tytuł oferty
+ Treść oferty

Ponadto, w łatwy sposób można uzyskać również dwie wartości jednoznacznie
identyfikujące ofertę:

+ Adres URL oferty
+ ID (będące częścią adresu URL)

Te dwie wartości z powodzeniem mogą służyć za klucz pozwalający np.
szybko sprawdzać czy oferta jest już w bazie systemu - czyli czy została już
kiedyś przetworzona.

![Widok oferty w witrynie pracuj.pl. \label{ref_a_figure}](source/figures/pracuj_offer_view.png){ width=100% }

\clearpage
