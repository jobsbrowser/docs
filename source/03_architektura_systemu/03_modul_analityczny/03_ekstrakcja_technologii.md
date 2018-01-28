# Ekstrakcja technologii

**Rozpoznawanie technologii**

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
czy języków programowania. Jako źródło takich danych, postanowiliśmy wykorzystać popularny
wśród ludzi zainteresowanych IT portal **Stack Overflow**. API tego serwisu pozwala na pobranie
używanych przez jego użytkowników tagów, posortowanych według popularności. Wszystkich jest blisko 40 tys.
W zdecydowanej większości odpowiadają one nazwom technologii.

Na potrzeby naszego projektu, korzystamy ze zbioru dwóch tysięcy najpopularniejszych tagów. Znajdują się
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


**Architektura**

Z technicznego punktu widzenia proces ten jest ciągiem funkcji, wykonywanych
w ustalonej kolejności, gdzie wyjście każdej z nich przekazywane jest jako argument
do następnej. Stąd powtarzający się często termin *pipeline*. Argumentem pierwszej funkcji
jest zapisana do bazy danych chwilę po otrzymaniu od robota oferta, natomiast wynikiem
ostatniej uproszczony obiekt oferty zawierający listę znalezionych technologii. Na koniec oferta jest
wyszukiwana w bazie, dodawana jest do niej wspomniana lista (dzięki zastosowaniu nierelacyjnej bazy
danych nie wiąże się to z potrzebą jej przebudowy), a następnie wysyłana jest do usługi
generującej statystyki.

Do obsługi łańcucha, czyli utrzymania poprawnej kolejności wykonywania funkcji, oraz asynchronicznego
przetwarzania wielu ofert jednocześnie korzystamy z frameworka **Celery**[@celery], którego opis znajduje
się w dalszej części tej sekcji.


**Znajdowanie podobnych technologii za pomocą modelu Word2Vec**

Jedną z funkcjonalności systemu jest generowanie technologii zbliżonych do tych wybranych przez
użytkownika.
W celu znalezienia takiego zbioru postanowiliśmy skorzystać z modelu Word2Vec [@word2vec].
Word2vec to grupa modeli reprezentujących słowa jako tzw. zanurzenia słów [@wordemb],
czyli słowa reprezentowane jako wektory w wielowymiarowej przestrzeni.
W naszym przypadku zdecydowaliśmy się wytrenować model word2vec nie na całych
korpusach (wszystkich ogłoszeniach), ale na wykorzystywanej przez nas liście technologii.
Dzięki takiemu podejściu wynikowy zbiór zawierać będzie tylko pozostałe elementy z tej listy.
Do wytrenowania modelu skorzystaliśmy z biblioteki gensim [@gensim].
Poniżej znajdują się wyniki otrzymane dla technologii `JAVA`:

- java-ee
- maven
- junit
- hibernate
- groovy
- soa
- tomcat
- jsp
- jenkins
- eclipse

Jak widać wyniki są zadowalające, wszystkie klucze znajdujące się na 
powyższej liście mają wiele wspólnego z językiem programowania JAVA.
Jednak z powodu stosunkowo małego zbioru treningowego rezultaty nie są 
tak dobre dla mniej popularnych technologii, mających mało wystąpień.
Dla przykładu - `Vue.JS`:

- node.js
- elasticsearch
- jasmine
- testy jednostkowe
- bitbucket
- api
- nosql
- webpack
- mongodb
- user-interface
