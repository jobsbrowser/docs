# Testy

W kodzie źródłowym modułu znajdują się testy jednostkowe pozwalające na
przetestowanie poprawności zaimplementowanych metod oraz funkcji.
W tej sekcji znajduje się również opis przykładowego scenariusza testów
akceptacyjnych.


## Testy jednostkowe

Aby uruchomić testy jednostkowe w konsoli należy wpisać polecenie `tox`.

Poniżej przedstawiamy listę plików z testami jednostkowymi oraz opis
poszczególnych funkcji lub metod:

-   `pipeline.tasks.test_preprocess.py` - plik z testami etapów
    przygotowujących oferty do ekstrakcji tagów.
    -   `TestDetectLanguage` - klasa zawierająca metody testujące etap
        detekcji języka w którym napisane jest ogłoszenie.
    -   `test_prepare_extract_proper_fields_from_offer` - test sprawdzający
        czy etap przygotowujący ofertę, tworzy oraz wybiera odpowiednie
        pola z całej oferty.
    -   `test_remove_stopwords_return_tokens_without_stopwords` - test
        weryfikujący poprawne usunięcie tokenów będących słowami nieistotnymi.
    -   `test_strip_html_tags_return_tokens_without_html_tags` - test
        sprawdzający czy etap poprawnie usuwa tagi HTML.
    -   `test_tokenize_return_list_of_lowercase_tokens` - test sprawdzający
        czy etap zwraca odpowiednią listę tokenów składających się
        z małych liter.
-   `pipeline.tasks.test_process.py` - plik z testami etapów wykonujących
    ekstrakcje tagów z technologiami z oferty.
-   `pipeline.tasks.test_postprocess.py` - plik z testami etapów wykonujących
    zadania po wykonaniu ekstrakcji kluczy.


## Testy akceptacyjne

Funkcje modułu podczas normalnej pracy systemu działają w tle, uzupełniając przychodzące z modułu
zbierania danych oferty o listę wykrytych kluczy. Poprawne jego działanie, można więc przetestować
wywołując łańcuch przetwarzania ręcznie, dla wybranej z bazy oferty. Proces wygląda następująco:

+ W linii poleceń pobieramy jedną z ofert z bazy
+ Wywołujemy na niej łańcuch przetwarzania
+ Podglądamy listę wykrytych kluczy


