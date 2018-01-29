# Aplikacja WWW

Kod źródłowy aplikacji WWW znaleźć można w katalogu `src/www`.

## Struktura plików kodu źródłowego

```bash
├── index.html            # główny plik HTML
├── package.json          # plik z zależnościami projektu
├── package-lock.json
├── public                # katalog na zasoby niezmieniające się np. zdjęcia, ikony
├── README.md
├── src                   # katalog z kodem źródłowym aplikacji
│   ├── App.vue           # główny komponent aplikacji
│   ├── components        # katalog z komponentami UI
│   │   ├── LineChart.js  # komponent obsługujący rysowanie wykresów liniowych
│   │   ├── Menu.vue      # komponent reprezentujący menu aplikacji
│   │   ├── Offer.vue     # komponent reprezentujący widok oferty
│   │   └── TagInput.vue  # komponent obsługujący wybieranie technologii przez użytkownika
│   ├── main.js           # plik wejściowy dla aplikacji
│   ├── pages             # katalog z komponentami reprezentującymi podstrony aplikacji
│   │   ├── Info.vue      # komponent prezentujący informacje o projekcie
│   │   ├── Search.vue    # komponent umożliwiający interaktywne wyszukiwanie ofert
│   │   └── Stats.vue     # komponent pokazujący statystyki
│   ├── router
│   │   └── index.js      # konfiguracje routingu (ścieżek URL) aplikacji
│   └── store
│       └── index.js      # konfiguracja oraz inicjalizacja vuex-store
└── webpack.config.js     
```

## Opis klas i metod

-   komponenty UI
    -   `Menu` - komponent generujący widok górnego menu.
    -   `TagInput` - komponent obsługujący pobieranie technologii (tagów) od użytkownika
        w interaktywny sposób.
    -   `Offer` - komponent generujący widok listy ofert z odpowiednimi tagami pobranymi
        od użytkownika poprzez komponent `TagInput`.
    -   `LineChart` - komponent renderujący wykresy liniowe dla technologii pobranych
        dzięki komponentowi `TagInput`.

-   komponenty stron
    -   `Search` - komponent korzystający z komponentów: `Menu`, `TagInput` oraz
        `Offer`. Pobiera informacje o ofertach z pobranymi tagami i prezentuje
        je w formie listy.
    -   `Info` - komponent korzystający z komponentów: `Menu`. Pobiera
        informacje na temat projektu **JobsBrowser** oraz je prezentuje.
    -   `Stats` - komponent korzystający z komponentów: `Menu`, `TagInput` oraz
        `LineChart`. Pobiera statystyki dotyczące wybranych technologii oraz prezentuje
        je użytkownikowi w formie wykresów.