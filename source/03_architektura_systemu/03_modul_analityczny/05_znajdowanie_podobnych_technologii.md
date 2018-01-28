# Znajdowanie podobnych technologii za pomocą modelu Word2Vec

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