# Baza danych

Wykorzystanym silnikiem bazy danych jest SQLite3[@sqlite]. Zdecydowaliśmy się na
bazę relacyjną ze względu na to, że wykonujemy skomplikowane zapytania,
które silnikom nierelacyjnych baz danych zajmują dużo więcej czasu oraz zasobów
serwera, o czym przekonaliśmy się, testując te same zapytania na bazie danych
MongoDB[@mongodb].
Struktura dokumentów przechowywanych w bazie jest relacyjnym odzwierciedleniem
struktury zebranego ogłoszenia oraz dokumentu przechowywanego przez moduł
zbierający dane. Wyróżniliśmy trzy tabele:

+ Oferty
    + Adres URL
    + Czas w którym pobrano ofertę
    + Kod HTML strony z ofertą
    + ID oferty w systemie pracuj.pl
    + Data dodania
    + Data ważności
    + Podmiot dodający
    + Tytuł oferty
    + Miejsce pracy
    + Kategorie oferty
    + Kod HTML treści oferty (rozbity na opis, kwalifikacje oraz benefity - wg
      struktury Pracuj.pl)
+ Tagi
    + nazwa tagu
+ Dodatkowa tabela reprezentująca relację ofert z tagami - jest to bowiem
relacja `many-to-many` - czyli wiele do wielu.


## Indeksy

W celu optymalizacji często wykonywanych zapytań skorzystaliśmy z indeksów.
W bazie kluczy indeksowaną kolumną jest nazwa tagu, zaś w bazie ofert
data dodania oferty oraz data wygaśnięcia oferty.
