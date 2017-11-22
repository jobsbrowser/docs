\clearpage

# Opis biznesowy

Głównym zadaniem aplikacji ma być automatyczna analiza rynku pracy. System
zajmuje się agregacją oraz przetwarzaniem (analizą) ofert zebranych z serwisu
zewnętrznego (Pracuj.pl) i przedstawianiem wyników użytkownikowi.

W szczególności proces działania systemu sprowadza się do:

1. Pobierania ofert pracy z serwisu zewnętrznego wyłuskując kluczowe elementy:
   tytuł ogłoszenia, opis, datę dodania, itp.
2. Zapisania tak zebranych ogłoszeń do własnej bazy danych
3. Przeprowadzenia analizy na treści ogłoszenia uzyskując zeń listę *kluczy*, tj:
    - obszaru branży IT którego dotyczy ogłoszenie
    - stanowiska którego dotyczy
    - wymaganych od pracownika opanowanych technologii / umiejętności
4. Udostępnienia użytkownikowi interfejsu do wyszukiwania zebranych w systemie
   ofert oraz wyświetlania statystyk przy użyciu wyżej wspomnianych kluczy.
   
Wymienione działania realizują odrębne komponenty systemu. Bardziej szczegółowy
podział i opis znajduje się w sekcji wymagań funkcjonalnych oraz rozdziale drugim
będącym dokumentacją każdego z modułów.

Użytkownik bezpośrednio będzie korzystał tylko z ostatniego modułu - aplikacji WWW
będącej interfejsem dla zebranych i przetworzonych przez system danych.

Aplikacja będzie niosła korzyść duzej grupie odbiorców takich jak:

-   studenci - dzięki aplikacji będą mogli znaleźć świetnie dopasowane
    stanowisko do ich umiejętności lub obserwując dane stanowisko
    określić jakie umięjętności są na nim elementarne, a także jakiej
    technologii powinni się nauczyć w najbliższym czasie.
-   osoby szukjące pracy - łatwo na podstawie swoich umiejętności znajdą
    stanowiska dla siebie.
-   pracodawcy - na podstawie trendów wśród używanych technologii będą mogli
    podjąć decyzje dotyczące przyszłych projektów.
-   pozostali użytkownicy zainteresowani analizą rynku pracy.
