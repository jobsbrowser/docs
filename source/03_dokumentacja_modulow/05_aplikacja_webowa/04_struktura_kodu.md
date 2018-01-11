# Struktura kodu

Poniżej prezentujemy drzewo katalogów oraz plików modułu wraz z krótkim
omówieniem.

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
│   │   └── TagInput.vue  # komponent obsługujący pobieranie kluczy od użytkownika
│   ├── main.js           # plik wejściowy dla aplikacji
│   ├── pages             # katalog z komponentami reprezentującymi podstrony aplikacji
│   │   ├── Info.vue      # komponent prezentujący informacje o projekcie
│   │   ├── Search.vue    # komponent umożliwiający interaktywne wyszukiwanie ofert
│   │   └── Stats.vue     # komponent pokazujący statystyki
│   ├── router
│   │   └── index.js      # konfiguracje routowania aplikacji
│   └── store
│       └── index.js      # konfiguracja oraz inicjalizacja vuex-store
└── webpack.config.js     # ustawienia babela
```
