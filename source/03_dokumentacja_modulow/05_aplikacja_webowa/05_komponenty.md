# Główne komponenty aplikacji

Poniżej prezentujemy najważniejsze komponenty aplikacji wraz z krótkim opisem:
-   komponenty UI
    -   `Menu` - komponent generujący widok górnego menu.
    -   `TagInput` - komponent obsługujący pobieranie kluczy (tagów) od użytkownika
        w interaktywny sposób.
    -   `Offer` - komponent generujący widok listy ofert z odpowiednimi tagami pobranymi
        od użytkownika poprzez komponent `TagInput`.
    -   `LineChart` - komponent renderujący wykresy liniowe dla kluczy pobranych
        dzięki komponentowi `TagInput`.

-   komponenty stron
    -   `Search` - komponent korzystający z komponentów: `Menu`, `TagInput` oraz
        `Offer`. Pobiera informacje o ofertach z pobranymi tagami i prezentuje
        je w formie listy.
    -   `Info` - komponent korzystający z komponentów: `Menu`. Pobiera
        informacje na temat projektu **JobsBrowser** oraz je prezentuje.
    -   `Stats` - komponent korzystający z komponentów: `Menu`, `TagInput` oraz
        `LineChart`. Pobiera statystyki dotyczące wybranych kluczy oraz prezentuje
        je użytkownikowi w formie wykresów.
