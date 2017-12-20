# Główne klasy modułu

-   `add_offer` - funkcja implementująca dodawanie otrzymanej oferty do bazy
    danych.
-   `get_offers` - funkcja implementująca pobieranie aktualnych ofert (takich
    których data w polu *valid_through* jest większa od daty dzisiejszej)
    znajdujących się w bazie danych.
-   `init_app` - funkcja tworząca aplikację z podaną konfiguracją (jako
    parametr *config_name* lub zmienna środowiskowa `APP_CONFIG`).
-   **BaseConfig** - klasa z bazową, fundamentalną konfiguracją.
-   **DevConfig** - klasa przechowująca konfigurację developerską.
-   **ProductionConfig** - klasa przechowująca konfigurację produkcyjną.
-   **TestingConfig** - klasa przechowująca konfigurację testową.

