# Testy

W kodzie źródłowym modułu znajdują się testy jednostkowe pozwalające na
przetestowanie poprawności zaimplementowanych metod oraz funkcji.
W tej sekcji znajduje się również opis przykładowego scenariusza testów
akceptacyjnych.


## Testy jednostkowe

Aby uruchomić testy jednostkowe w konsoli należy wpisać polecenie `tox`.

Poniżej przedstawiamy listę plików z testami jednostkowymi oraz opis
poszczególnych funkcji lub metod:




## Testy akceptacyjne

Funkcje modułu podczas normalnej pracy systemu działają w tle, uzupełniając przychodzące z modułu
zbierania danych oferty o listę wykrytych kluczy. Poprawne jego działanie, można więc przetestować
wywołując łańcuch przetwarzania ręcznie, dla wybranej z bazy oferty. Proces wygląda następująco:

+ W linii poleceń pobieramy jedną z ofert z bazy
+ Wywołujemy na niej łańcuch przetwarzania
+ Podglądamy listę wykrytych kluczy


\clearpage

![Przykładowy skrypt testujący\label{ref_a_figure}](source/figures/test_pipeline_script.png){ width=100% }

![Tekst przykładowej oferty\label{ref_a_figure}](source/figures/test_offer_content.png){ width=100% }

\clearpage

![Rezultat \label{ref_a_figure}](source/figures/test_pipeline_result.png){ width=100% }

\clearpage

