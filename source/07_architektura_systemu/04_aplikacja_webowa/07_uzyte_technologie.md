# Wykorzystane technologie

**VueJS**

Licencja: MIT

Aplikacja została napisana we frameworku VueJS[@vuejs].
Jest to framework napisany w języku JavaScript oparty na architekturze
MVVVM (Model-View--View-Model). VueJS umożliwia tworzenie lekkich
oraz szybkich aplikacji sieciowych. Budowanie aplikacji polega na
tworzeniu tzw. komponentów i składaniu z nich całej aplikacji.
VueJS wydaje się być dobrym wyborem przy tworzeniu aplikacji, które opierają
się na konsumowaniu danych z różnych API oraz prezentowaniu ich
użytkownikowi.

Do budowy aplikacji wykorzystano kilka otwartoźródłowych rozszerzeń:

-   `vuetify`[@vuetify] - framework dostarczający gotowe komponenty stworzone
    w stylu material design
-   `vuex`[@vuex] - system (wzorzec) zarządzania stanem aplikacji
    napisanej w VueJS. Zapewnia miejsce na przechowywanie danych,
    które będą dostępne przez każdy komponent oraz kontroluje ich
    nadpisanie czy zmianę
-   `chart.js`[@chartjs] - biblioteka używana do tworzenia estetycznych wykresów
-   `axios`[@axios] - klient HTTP wykorzystany do komunikacji z modułem analitycznym