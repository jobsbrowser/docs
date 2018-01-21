# Architektura i algorytm

Z technicznego punktu widzenia moduł jest ciągiem funkcji, wykonywanych
w ustalonej kolejności, gdzie wyjście każdej z nich przekazywane jest jako argument
do następnej. Stąd powtarzający się w kodzie termin *pipeline*. Argumentem pierwszej funkcji
jest zapisana do bazy danych chwilę po pobraniu z serwisu zewnętrznego oferta, natomiast wynikiem
ostatniej uproszczony obiekt oferty zawierający listę znalezionych kluczy. Na koniec oferta jest
wyszukiwana w bazie, dodawana jest do niej wspomniana lista (dzięki zastosowaniu nierelacyjnej bazy
danych nie wiąże się to z potrzebą jej przebudowy).

Do obsługi łańcucha, czyli utrzymania poprawnej kolejności wykonywania funkcji, oraz asynchronicznego
przetwarzania wielu ofert jednocześnie korzystamy z frameworka **Celery**[@celery], którego opis znajduje
się w dalszej części tego rozdziału.


## Rozpoznawanie umiejętności i technologii

Uznaliśmy, że aby w miarę poprawnie rozpoznawać klucze, powinniśmy w pierwszym kroku
zaopatrzyć się w miarę obszerny i sprawdzony ich zbiór.\newline
Podejście takie, jak później się
okazało wydaje się być całkiem słuszne, ponieważ stosowane jest także w projektach
o znacznie szerszym zasięgu i złożoności niż nasz. Dla przykładu, powstająca w momencie
pisania tej pracy platforma **Google Cloud Job Discovery**, zajmująca się automatycznym dopasowywaniem
ofert pracy do CV potencjalnych pracowników, do działania wykorzystuje zbudowaną przez zespół Google
ontologię zawierającą, jak podają, ok. 50 tys. umiejętności z różnych pól zawodowych.

Z racji tego, że nasz projekt skupia się na ofertach pracy z branży IT, postanowiliśmy skorzystać z faktu
że istotne, oczekiwane przez pracodawców umiejętności, pokrywają się z nazwami technologii informatycznych,
czy języków programowania. Jako źródło takich danych, postanowiliśmy wykorzystać niesamowicie popularny
wśród ludzi zainteresowanych IT portal **Stack Overflow**. API tego serwisu pozwala na pobranie
używanych przez jego użytkowników kluczy, posortowanych według popularności. Wszystkich jest blisko 40 tys.

Na potrzeby naszego projektu, korzystamy ze zbioru dziesięciu tysięcy najpopularniejszych kluczy. Znajdują się
wśród nich wszelakie technologie, frameworki, wzorce projektowe i języki programowania. Mając taką listę,
możemy każdą przychodzącą ofertę przeszukać pod względem występowania niektórych z nich. Proces ten przeprowadzamy
w następując sposób:

1. Po zapisaniu całej oferty do bazy, upraszczamy obiekt przekazując dalej tylko istotne z punktu
widzenia komponentu dane, tj.

+ ID
+ tytuł
+ treść

2. Z treści oferty usuwamy tagi HTML

3. Treść oferty rozbijamy na *tokeny*, czyli wyrazy oraz znaki interpunkcyjne

4. Sprawdzamy czy oferta jest w języku polskim, bo tylko takie akceptujemy

5. Usuwamy zbędne z punktu widzenia analizy językowej tokeny, takie jak przyimki, spójniki czy zaimki.

6. Dla listy uzyskanych tokenów sprawdzamy które z nich znajdują się na liście znanych nam kluczy, i te zapisujemy.


W ten sposób każdej ofercie z osobna przypisujemy listę technologii które znaleźliśmy w jej treści.
Śledząc opis algorytmu, zauważyć można że wynikowo będą one posortowane jedynie ze względu na kolejność
występowania w treści oferty. Właściwością tą zajmie się kolejny moduł systemu, który znalezionym tutaj kluczom
nada odpowiednie priorytety, biorąc pod uwagę nie tylko kolejność ich występowania w tekście, ale także sąsiedztwo
wyrazów w jakim się znajdują, czy poprzedzające je frazy.


## Uzasadnienie wyboru powyżej opisanego algorytmu

Dużo czasu poświęciliśmy na testowanie wielu algorytmów do wyznaczania
słów kluczowych z tekstu. Wiele z nich dawało niezadowalające wyniki
na zbiorach ogłoszeń napisanych w języku polskim.
Poniżej opisujemy krótko algorytmy które przetestowaliśmy wraz z przykładowymi
wynikami jakie dawały. Wszystkie przedstawione poniżej wyniki zostały uzyskane
z poniższej oferty:

\clearpage

![Oferta wykorzystywana do testów algorytmów \label{ref_a_figure}](source/figures/sample_offer.png){ width=100% }

\clearpage

+ RAKE(Rapid Automatic Keyword Extraction)[@rakenltk]
Bardzo popularny na githubie stosunkowo prosty algorytm, niestety
nie przyniósł zadowalających efektów. Poniżej prezentujemy listę 10
najważniejszych według algorytmu RAKE fraz/kluczy:

    + umiejętność samoorganizacji potrafisz pisać wysokiej jakości kod posiadasz umiejętność dekompozycji zadań
    - potrafisz pisać testy jednostkowe znasz dowolny
    - dostarczania działających rozwiązań jesteś skrupulatny
    - poziomie przynajmniej dobrym język python
    - język programowania możesz wykazać
    - dużym prawdopodobieństwem jesteś osobą
    - temat relacyjnych baz danych
    - mile widziana znajomość postgresql
    - znajomością protokołów sieciowych to
    - posiadasz dobrą wiedzę


+ TF-IDF(Term Frequency - Inverse Document Frequency)[@tfidf]
Jeden z najbardziej popularnych i najszerzej wykorzystywanych algorytmów
w świecie przetwarzania języka naturalnego, również nie dawał
zadowalających wyników.

    + pisać
    + implementowanie
    + python
    + posiadasz
    + wyszukujących
    + znasz
    + uwierzytelnianie
    + dres
    + niecierpliwością
    + niespotykaną


Z racji bardzo szczególnego podzbioru języka polskiego używanego przy pisaniu
ogłoszeń powyższe algorytmy dawały bardzo dziwne wyniki, dlatego też
zdecydowaliśmy się na korzystanie z algorytmu opartego na tagach pobranych
z serwisu stackoverflow.
