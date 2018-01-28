# Próby analizy tekstu i uzasadnienie wyboru algorytmu

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


**TF-IDF(Term Frequency - Inverse Document Frequency)[@tfidf]**

Jeden z bardziej popularnych i szeroko wykorzystywanych algorytmów
w świecie przetwarzania języka naturalnego. Niestety również nie dawał
zadowalających wyników. Wykryte słowa kluczowe dla tej samej oferty:

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