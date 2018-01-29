# Generowanie statystyk

Przeznaczeniem tej części modułu jest odpowiadanie na żądania wyszukiwania oraz
generowania statystyk. Komunikacja taka powinna odbywać się z wykorzystaniem
protokołu HTTP, tak aby łatwo można było zintegrować moduł z aplikacją WWW
bądź w przypadku takiej potrzeby innym dowolnym konsumentem.

Z powodu złożoności zapytań (jak np. generowanie statystyk sumarycznych dla
wielu dni i wielu technologii jednocześnie) część ta potrzebuje własnej bazy danych
na której wykonywane będą zapytania. Wymusza to dodatkowe wymaganie w postaci
możliwości dodawania nowych ofert, z którego korzysta proces ekstrakcji technologii
(wysyłając na bieżąco w pełni przetworzone oferty).


**Wymagania**

Wymagania funkcjonalne sprowadzają się więc do obsługi następujących
żądań HTTP:

+ dodanie nowej oferty do bazy
+ wyszukiwanie ofert przy pomocy danego zbioru technologii
+ generowanie statystyk, tj. dla każdego dnia z zakresu od 02.12.2018 do
daty wykonania żądania obliczenie ilości aktywnych wówczas w serwisie pracuj.pl
ofert zawierających podane technologie
+ generowanie statystyk całościowych - tj. ilości wszystkich ofert w bazie
(również we wspomnianym wyżej zakresie) oraz daty dodania ostatniego ogłoszenia


Natomiast wymagania niefunkcjonalne postawione modułowi to:

+ **niezawodność** - usługa powinna być dostępna cały czas, ponieważ
  dostarcza ona danych niezbędnych do pokazania wszystkich statystyk w
  aplikacji z której korzysta użytkownik. Bez niej aplikacja WWW staje się
  bezużyteczna.
+ **wydajność** - liczba przychodzących do modułu danych może być momentami
  bardzo duża, dlatego zapisywanie do bazy nie może być przeprowadzane niewydajnie.
  Największy wpływ na wydajność mają zapytania generujące odpowiednie statystyki.
  Niektóre z nich są skomplikowane, dlatego niezbędna jest ich optymalizacja.
  Wydłużony czas generowania statystyk obniży znacznie komfort używania aplikacji
  WWW
  
  
**Interfejs**

Usługa z pozostałymi komponentami systemu łączy się przez interfejs HTTP.
Dane do statystyk są dostarczane przez proces ekstrakcji technologii.
Konsumentem generowanych przez usługę statystyk jest aplikacja
WWW z której korzysta końcowy użytkownik.

Interfejs zaimplementowany jest przy użyciu frameworka Django[@django].
Implementując ten interfejs wdrażaliśmy dobre praktyki programowania
opisane w książce
"Two Scoops of Django 1.11: Best Practices for the Django Web Framework"[@djangobook].


![Schemat modułu. \label{ref_a_figure}](source/figures/backend_diagram.png){ width=100% }

\clearpage


**Baza danych**

Wykorzystanym silnikiem bazy danych jest SQLite3[@sqlite]. Wybór padł na
bazę relacyjną ze względu na to, że wykonywane są do niej skomplikowane zapytania,
które silnikom nierelacyjnych baz danych zajmują więcej czasu oraz zasobów
serwera, o czym przekonaliśmy się, testując te same zapytania na bazie danych
MongoDB[@mongodb].
Struktura dokumentów przechowywanych w bazie jest relacyjnym odzwierciedleniem
struktury ogłoszenia zebranego przez robota zbierający dane. 
Baza zawiera trzy tabele:

+ Oferty
    + Adres URL
    + Czas w którym pobrano ofertę
    + Kod HTML strony z ofertą
    + ID oferty w systemie pracuj.pl
    + Data dodania
    + Data ważności
    + Podmiot dodający
    + Tytuł oferty
    + Miejsce pracy
    + Kategorie oferty
    + Kod HTML treści oferty (rozbity na opis, kwalifikacje oraz benefity - wg
      struktury Pracuj.pl)
+ Tagi
    + nazwa technologii
+ Dodatkowa tabela reprezentująca relację ofert z tagami - jest to bowiem
relacja `many-to-many` - czyli wiele do wielu.

W celu optymalizacji często wykonywanych zapytań baza posiada założone indeksy.
W tabeli tagów indeksowaną kolumną jest nazwa technologii, zaś w bazie ofert
data dodania oferty oraz data wygaśnięcia oferty.


**Algorytm generowania statystyk**

O ile wyszukiwanie ofert na podstawie listy podanych technologii realizowane
jest w wydajny i optymalny sposób przez użyty framework, o tyle
generowanie statystyk w określony przez wymagania modułu sposób jest
bardziej skomplikowane i wymagało implementacji własnego algorytmu.

Przypominając wymagania, interfejs statystyk ma działać w następujący sposób:

+ Przyjmij listę technologii
+ Dla każdego dnia z przedziału od 02.12.2018 (początek zbierania ofert) do
dzisiaj policz ile tego dnia było w serwisie pracuj.pl aktywnych ofert
zawierających te technologie oraz jaki procent wszystkich aktywnych ofert z branży IT
stanowiły.
+ Zwróć wynik

Ofertę uważa się za aktywną danego dnia, jeśli zachodzą dwa warunki:
`dzień dodania <= wybrany dzień` oraz `dzień wygaśnięcia >= wybrany dzień`.
Mając te dwie daty w bazie danych można więc konstruować zapytania
wybierające odpowiednie oferty.

Naiwna implementacja algorytmu, sprowadzałaby się do wykonania *n* zapytań
zliczających do bazy danych, gdzie *n* to ilość dni które upłynęły od daty początkowej.
Nie jest to rozwiązanie optymalne, ponieważ zapytania do bazy danych są kosztowne
a z każdym kolejnym dniem wygenerowanie statystyk wymagałoby ich więcej. 

Postanowiliśmy ograniczyć się do jednego zapytania, a algorytm wygląda następująco:
 
1. Wybierz oferty aktywne przez choć jeden dzień na zadanym przedziale. Wykorzystane warunki to:
`dzień dodania <= koniec przedziału`, `dzień wygaśnięcia >= początek przedziału`
oraz warunek zawierania się wszystkich podanych technologii wśród tych wykrytych w ofercie.
2. Utwórz *n* "kubełków", gdzie każdy kubełek odpowiada jednej dacie z przedziału
i na początku ma wartość 0
3. Przejdź po liście ofert i dla każdej z nich:
    - Zwiększ wartość kubełka odpowiadającego dacie dodania oferty o 1.
    Może się zdarzyć że data dodania oferty poprzedza początek zakresu, i nie
    ma takiego kubełka. Wtedy zwiększ wartość pierwszego kubełka.
    - Jeśli data wygaśnięcia oferty poprzedza koniec zakresu, to zmniejsz wartość
    w kubełku z dniem następnym po dniu wygaśnięcia.
4. Wykonaj operację sumy skumulowanej na kubełkach.

Dzięki temu w każdym kubełku odpowiadającym każdemu dniu z zakresu znajdzie się
ilość pasujących do zapytania, aktywnych tamtego dnia ofert. Do uzyskania wyniku
procentowego operacja jest powtarzana, ale w kroku 1 pomijany jest warunek dotyczący technologii.
Wtedy wynikiem jest iloraz rezultatów tych dwóch operacji.
