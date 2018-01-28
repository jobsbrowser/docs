# Główne klasy modułu

Najbardziej istotnymi klasami są:

- **Offer** - Model oferty. Tutaj zadeklarowane są pola stanowiące strukturę
tabeli w bazie danych.
- **Tag** - Model pojedynczego klucza. Zawiera jedynie pole na nazwę.
- **OffersListView** - klasa widoku obsługującego wyszukiwanie ofert.
- **OffersStatsView** - klasa widoku obsługującego generowanie statystyk
- **SystemInfoView** - klasa widoku obsługującego statystyki całościowe

każda z tych klas jest rozszerzeniem funkcjonalności oferowanych przez framework,
dziedzicząc po odpowiedniej klasie bazowej. Logika implementowana przez nas
znajduje się tylko w klasach **OffersStatsView** oraz **SystemInfoView**
w postaci własnych metod. W pozostałych dostosowanie klasy oferowanej przez
framework do naszych potrzeb sprowadza się do ustawienia odpowiednich atrybutów.