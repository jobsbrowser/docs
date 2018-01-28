# Podsumowanie

Głównym celem pracy było stworzenie narzędzia oferującego możliwość opisanej we wstępnych wymaganiach
analizy zmian zachodzących na rynku pracy w branży IT.
Za kluczowe elementy przyjąć można:
 
+ automatyzację samego systemu - tak, aby bez ingerencji użytkownika obsługiwał
pojawiające się w czasie jego działania oferty pracy
+ poprawną analizę - polegającą na ekstrakcji nazw odpowiednich technologii z ich treści
+ implementację przyjaznego interfejsu użytkownika w postaci aplikacji WWW dającej
dostęp do opracowanych przez system statystyk

Założenia te można uznać za spełnione, a ponadto zauważono możliwości rozwoju
systemu niosące ze sobą potencjalne korzyści.


**Serwisy dostarczające dane**

Aplikacja, zgodnie ze wstępnymi założeniami korzysta z tylko jednego serwisu
(Pracuj.pl) jako źródła ofert. Jest to jeden z największych tego typu serwisów
na polskim rynku, jednak niewątpliwie jakość danych nie ucierpiałaby gdyby
system analizował również oferty pochodzące z innych źródeł. Modularna struktura
systemu nie wymagałaby procesu jego przerabiania, a jedynie dopisania nowych
robotów w przypadku chęci dodania nowego serwisu. Nie byłaby to więc funkcjonalność
trudna do wdrożenia


**Bardziej zaawansowana analiza tekstu**

Zbiór technologii które system wykrywa w treści analizowanych ofert, choć
łatwy do powiększenia, jest ograniczony. Być może dzięki odpowiednim zasobom
czasu i wiedzy dałoby się dopracować sposób wykorzystania opisanych w rozdz. \ref{proby_analizy}
algorytmów, co pozwoliłoby na samodzielne rozpoznawanie przez system pewnych
słów jako technologie. Jest to temat bez wątpienia ciekawy, i z pewnością wart
rozważenia np. jako kontynuacja w ramach pracy magisterskiej.



