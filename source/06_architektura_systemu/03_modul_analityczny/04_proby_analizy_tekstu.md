# Próby analizy tekstu i uzasadnienie wyboru algorytmu \label{proby_analizy}

Dużo czasu poświęciliśmy na testowanie wielu algorytmów do wyznaczania
słów kluczowych z tekstu. Wiele z nich dawało niezadowalające wyniki
na zbiorach ogłoszeń napisanych w języku polskim.
Poniżej opisujemy krótko algorytmy które przetestowaliśmy wraz z przykładowymi
wynikami jakie dawały. Wszystkie przedstawione poniżej wyniki zostały uzyskane
z przykładowej oferty (Rys. \ref{example_offer}).

![Oferta wykorzystywana do uzyskania przykładowego wyniku \label{example_offer}](source/figures/sample_offer.png){ width=100% }

\clearpage


**RAKE(Rapid Automatic Keyword Extraction)[@rakenltk]**

Popularny, stosunkowo prosty algorytm do automatycznej ekstrakcji słów kluczowych. Niestety
nie przyniósł zadowalających efektów. Poniżej lista zawiera 10
najważniejszych według algorytmu RAKE fraz/kluczy wykrytych w przykładowej ofercie:

- umiejętność samoorganizacji potrafisz pisać wysokiej jakości kod posiadasz umiejętność dekompozycji zadań
- potrafisz pisać testy jednostkowe znasz dowolny
- dostarczania działających rozwiązań jesteś skrupulatny
- poziomie przynajmniej dobrym język python
- język programowania możesz wykazać
- dużym prawdopodobieństwem jesteś osobą
- temat relacyjnych baz danych
- mile widziana znajomość postgresql
- znajomością protokołów sieciowych to
- posiadasz dobrą wiedzę

Jak widać na powyższej liście algorytm RAKE zwrócił ciekawe rezultaty,
jednak ich dokładność i forma pozostawiały wiele do życzenia.


**TF-IDF(Term Frequency - Inverse Document Frequency)[@tfidf]**

Jeden z bardziej popularnych i szeroko wykorzystywanych algorytmów
w świecie przetwarzania języka naturalnego.

Przy opisie algorytmu korzystamy z poniższych oznaczeń:

+ $D$ - zbiór wszystkich dokumentów (ogłoszeń w bazie)
+ $d_i$ - i-ty dokument (ogłoszenie) z całego korpusu
+ $t_i$ - i-te słowo w ogłoszeniu

TF-IDF jest algorytmem przypisującym słowu wagę obliczaną na podstawie
istotności tego słowa w dokumencie.
Do wyznaczenie jej potrzebne są następujące miary:

+ Term Frequency - liczba wystąpień słowa $t_i$ w dokumencie $d_j$, oznaczamy ją przez
    $tf(t_i, d_j)$
+ Document Frequency - liczba dokumentów w których wystąpiło słowo $t_i$, oznaczenie: $df(t_i)$
+ Inverse Document Frequency - odwrotna częstość dokumentów, obliczana za pomocą
    wzoru: $idf(t_i) = \log_2 \frac{ \left | D \right |}{ df(t_i)}$

Korzystając z powyżej zdefiniowanych miar, waga słowa wyznaczana przez algorytm
TF-IDF jest postaci:

$tfidf(t_i, d_j) = tf(t_i, d_j) \cdot idf(t_i)$

Z powyższego wzoru widać, że waga jest tym większa im częściej w
danym dokumencie występuje badane słowo (mnożenie przez $tf(t_i, d_j)$), ale
wartość wagi zmniejsza się wraz z wzrostem częstości występowania badanego
słowa we wszystkich dokumentach z korpusu ($idf(t_i)$),
co przyczynia się do ignorowania słów z tzw. listy stopwords, czyli listy
słów nieistotnych, ale często występujących w zdaniach.


Niestety algorytm ten nie dawał zadowalających wyników.
Wykryte słowa kluczowe dla przykładowej oferty (Rys. \ref{example_offer}):

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
ogłoszeń oraz relatywnie niewielkiej ich ilości, powyższe algorytmy dawały
niezadowalające wyniki, dlatego też
zdecydowaliśmy się na korzystanie z algorytmu opartego na tagach pobranych
z serwisu *Stack Overflow*.
