# VueJS

Do stworzenia aplikacji zdecydowaliśmy się użyć stosunkowo nowego
frameworka VueJS[@vuejs].
Jest to framework napisany w języku JavaScript oparty na architekturze
MVVVM (Model-View--View-Model). VueJS umożliwia tworzenie lekkich
oraz szybkich aplikacji webowych. Budowanie aplikacji polega na
tworzeniu coraz to nowych komponentów i składaniu z nich całej aplikacji.
VueJS jest świetnym wyborem przy tworzeniu aplikacji, które opierają
się na konsumowaniu danych z różnych API oraz prezentowaniu ich
użytkownikowi, a więc wydaje się być rozwiązaniem dopasowanym do naszych
potrzeb. Jest wydawany na licencji MIT.

## Dodatkowe biblioteki

Do budowy aplikacji skorzystaliśmy z kilku rozszerzeń usprawniających pracę
z Vue. Przedstawiamy je poniżej:

-   `vuetify`[@vuetify] - framework dostarczający wiele pożytecznych
    komponentów stworzonych w stylu material design.
-   `vuex`[@vuex] - system(wzorzec) zarządzania stanem aplikacji
    napisanej w VueJS. Zapewnia miejsce na przechowywanie danych,
    które będą dostępne w każdym komponencie oraz kontroluje ich
    nadpisanie, zmianę. Jest także przydatny przy debugowaniu aplikacji.
-   `chart.js`[@chartjs] - biblioteka używana przez nas do tworzenia 
    wykresów, prezentowania statystyk.
-   `axios`[@axios] - klient HTTP, za pomocą którego w wygodny sposób
    komunikujemy się z modułem statystyk.
