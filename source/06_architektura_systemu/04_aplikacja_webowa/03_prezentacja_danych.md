# Interakcja z użytkownikiem i prezentacja danych

Interakcję użytkownika ze stroną można sprowadzić do możliwości
wybrania jednej bądź wielu z sugerowanych technologii na pasku wyszukiwania
oraz obserwacji zmian zachodzących w treści strony. Pasek ten widoczny jest po otworzeniu
zakładki ze statystykami (otwarta domyślnie) lub z wyszukiwarką ofert.
Podczas wybierania technologii aktywny jest system auto-uzupełniania, który
chroni użytkownika przed wprowadzeniem niewłaściwych danych - np. nazwy technologii
która nie istnieje, czy zawierającej literówkę. Auto-uzupełnianie daje również
swego rodzaju podgląd na to, jakie technologie możliwe są do zbadania przy użyciu
systemu.


**Statystyki**

Na tej zakładce prezentowane są przewidziane w aplikacji wykresy, dotyczące wybranego
zbioru technologii. Zawartość zakładki podmienia się automatycznie po zaobserwowanej
zmianie na pasku wyszukiwania, a także w tle, np. gdy zmiana taka zostanie wykonana
z poziomu innej zakładki. Zakładki statystyk oraz wyszukiwania dzielą bowiem
ze sobą pasek wyszukiwania.

Prezentowane użytkownikowi informacje to:

1. Wykres porównujący dwie lub więcej technologii ze sobą. Porównanie wykonane jest
pod względem ilości ofert je zawierających i aktywnych danego dnia.
Widoczny jest on na samej górze zawartości zakładki, ale dopiero po wybraniu więcej
niż jednej technologii. Informacją płynąca z tego wykresu może być np. jak
konkurujące ze sobą technologie mają się do siebie na rynku pracy i jak wyglądało
to na przestrzeni czasu.

2. Wykresy ilości ofert zawierających każdą z wybranych technologii. Widoczne są dwa - 
jeden na którym przedstawiona jest całkowita liczba aktywnych ofert w czasie, oraz drugi
mówiący ile procent wszystkich ogłoszeń z branży IT one stanowią. Informacją płynąca z tego wykresu
może być np. czy popularność danej technologii rośnie lub maleje na przestrzeni czasu.

3. Wykres kołowy pracodawców. Wyszczególnionych jest na nim 10 najczęściej zamieszczających
ogłoszenia wymagające danej technologii pracodawców. Informacją płynącą z tego wykresu może być np.
jak wygląda zapotrzebowanie na daną technologię wśród największych firm z branży IT.

4. Lista dziesięciu najbardziej zbliżonych w modelu Word2Vec technologii. Informacją z niej płynącą
może być np. jakie technologie występują często wraz z tymi wybranymi przez użytkownika
w jednym ogłoszeniu.


**Wyszukiwanie**

Zakładka wyszukiwarki pozwala na przeglądanie zarówno aktywnych jak i archiwalnych
ofert zawierających każdą z wybranych technologii. Dostępne są podstawowe informacje
o każdej ofercie oraz odnośnik do oryginalnego ogłoszenia w serwisie Pracuj.pl.
Prezentowane są w postaci listy, na której każdy element jest rozwijalny, pokazując
więcej szczegółów.

Z poziomu tej zakładki użytkownik może też przeprowadzić operację eksportu danych.
Nad listą znalezionych ofert, a pod paskiem wyszukiwania znajduje się przycisk
pozwalający na pobranie ofert spełniających dane kryterium wyszukiwania w formacie JSON.


**Informacje**

Rolą ostatniej zakładki jest prezentacja użytkownikowi informacji dotyczących
serwisu jako całości. Zawiera kilka zdań o projekcie oraz dane takie jak

+ datę ostatniego przetwarzania ofert
+ liczbę wszystkich przetworzonych pod względem technologii ofert w bazie
+ wykres powyższej wartości względem czasu