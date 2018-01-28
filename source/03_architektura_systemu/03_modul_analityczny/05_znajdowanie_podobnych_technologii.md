# Znajdowanie podobnych technologii za pomocą modelu Word2Vec

Jedną z funkcjonalności systemu jest generowanie technologii zbliżonych do tych wybranych przez
użytkownika.
W celu znalezienia takiego zbioru postanowiliśmy skorzystać z modelu Word2Vec [@word2vec].
Word2vec to grupa modeli reprezentujących słowa jako tzw. zanurzenia słów [@wordemb],
czyli słowa reprezentowane jako wektory w wielowymiarowej przestrzeni.

W naszym przypadku zdecydowaliśmy się wytrenować model word2vec nie na całych
korpusach (wszystkich ogłoszeniach), ale na wykorzystywanej przez nas liście technologii.
Dzięki takiemu podejściu wynikowy zbiór zawierać będzie tylko pozostałe elementy z tej listy.
Do wytrenowania modelu skorzystaliśmy z biblioteki gensim[@gensim].

Rysunek \ref{w2vtsne} przedstawia wizualizacje wektorów technologii
uzyskaną przy pomocy algorytmu TSNE[@tsne], który transformuje zbiór
wielowymiarowych wektorów (w przypadku naszego modelu 100-wymiarowych),
kompresując je do 2-wymiarowej przestrzeni, zachowując proporcje, tj.
wektory które znajdowały się blisko siebie w wielowymiarowej przestrzeni
powinny znajdować się również blisko siebie w 2 wymiarowej przestrzeni oraz
analogicznie dla wektorów znajdujących się daleko od siebie.

Na rysunku możemy zaobserwować, że technologie podobne do siebie, bądź często
łączone ze sobą, występują blisko siebie, tak jak np. `html5`, `css3`, `jquery`
i `bootstrap`, czyli technologie front endowe, bardzo często wykorzystywane
razem w wielu projektach.

![Wizualizacja wektorów technologii \label{w2vtsne}](source/figures/w2v_tsne_visualization.png){ width=100% }

\clearpage

Aby określić poprawność znajdowanych przez algorytm technologii, wybraliśmy
kilka technologii dla których wskazaliśmy dziesięć ich idealnych najbliższych
sąsiadów (technologie najbardziej podobne do nich). Przykładowo dla technologii
`JAVA` jako jej najbliższych sąsiadów wskazaliśmy:

- maven
- hibernate
- junit
- spring
- groovy
- vaadin
- tomcat
- jsp
- jsf
- jenkins

a dla `Vue.js`:

- javascript
- node.js
- mvvm
- frontend
- reactjs
- angular
- api
- webpack
- firebase
- user-interface


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

Zatem wyżej opisany algorytm poprawnie wskazał 7 z 10 wybranych przez nas
technologii oraz jak widać wyniki są zadowalające, wszystkie pozostałe technologie
(eclipse, java-ee oraz soa) mają wiele wspólnego z językiem programowania JAVA.

Niestety z powodu stosunkowo małego zbioru treningowego rezultaty nie są 
tak dobre dla mniej popularnych technologii, mających mało wystąpień.
Dla przykładu - `Vue.js`:

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

Wynik ten zawiera 4 z 10 wybranych przez nas technologii.
