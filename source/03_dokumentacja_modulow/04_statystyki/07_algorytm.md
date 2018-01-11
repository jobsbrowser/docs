# Algorytm generowania statystyk

O ile wyszukiwanie ofert na podstawie listy podanych kluczy realizowane
jest w wydajny i optymalny sposób przez framework którego używamy, o tyle
generowanie statystyk w określony przez wymagania modułu sposób jest nieco
bardziej skomplikowane i wymagało implementacji własnego algorytmu.

Przypominając wymagania, interfejs statystyk ma działać w następujący sposób:

+ Przyjmij listę kluczy
+ Dla każdego dnia z przedziału od 02.12.2018 (początek zbierania ofert) do
dzisiaj policz ile tego dnia było w serwisie pracuj.pl aktywnych ofert
zawierających te klucze oraz jaki procent wszystkich aktywnych ofert z branży IT
stanowiły.
+ Zwróć wynik

Ofertę uważamy za aktywną danego dnia, jeśli zachodzą dwa warunki:
`dzień dodania <= wybrany dzień` oraz `dzień wygaśnięcia >= wybrany dzień`.
Mając te dwie daty w bazie danych możemy więc konstruować zapytania
wybierające odpowiednie oferty.

Naiwna implementacja algorytmy, sprowadzałaby się do wykonania *n* zapytań
zliczających do bazy danych, gdzie *n* to ilość dni które upłynęły od daty początkowej.
Nie jest to rozwiązanie optymalne, ponieważ zapytania do bazy danych są kosztowne
a z każdym kolejnym dniem wygenerowanie statystyk wymagałoby ich więcej. 

Postanowiliśmy ograniczyć się do jednego zapytania, a algorytm wygląda następująco:
 
1. Wybierz oferty aktywne przez choć jeden dzień na zadanym przedziale. Wykorzystane warunki to:
`dzień dodania <= koniec przedziału`, `dzień wygaśnięcia >= początek przedziału`
oraz warunek zawierania się wszystkich podanych kluczy wśród kluczy oferty.
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
procentowego operację powtarzamy, ale w kroku 1 pomijamy warunek dotyczący kluczy.
Wtedy dzielimy jeden wynik przez drugi.
