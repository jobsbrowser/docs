\clearpage

# Opis biznesowy

Głównym zadaniem aplikacji jest automatyczna analiza rynku pracy. System
zajmuje się agregacją oraz przetwarzaniem ofert zebranych z serwisu
zewnętrznego (Pracuj.pl) i przedstawianiem wyników użytkownikowi.

W szczególności proces działania systemu sprowadza się do:

1. Pobierania ofert pracy z serwisu zewnętrznego biorąc pod uwagę jedynie kluczowe elementy, takie jak:
   tytuł ogłoszenia, opis, datę dodania, itp.
2. Zapisania tak zebranych ogłoszeń do bazy danych
3. Przeprowadzenia analizy na treści ogłoszenia uzyskując listę technologii wymienionych w treści ogłoszenia,
   których znajomość jest oczekiwana od pracownika.
4. Udostępnienia użytkownikowi interfejsu do wyszukiwania zebranych w systemie
   ofert oraz wyświetlania statystyk dla wybranych technologii w postaci strony WWW.
   
Wymienione działania realizują odrębne komponenty systemu.

Użytkownik bezpośrednio korzystać powinien tylko z jednego modułu -
wspomnianej wyżej aplikacji WWW.

Przewidzianymi grupami docelowymi użytkowników aplikacji są:

-   studenci i osoby szukające pracy - dzięki oferowanym przez aplikację danym, będą mogli ocenić
    znajomość których technologii staje się pożądana na rynku pracy
-   pracodawcy - na podstawie trendów wśród używanych technologii będą mogli
    podjąć decyzje dotyczące przyszłych projektów
-   pozostali użytkownicy zainteresowani zmianami na rynku pracy - 
    możliwość eksportu zgromadzonych przez system danych pozwala na przeprowadzenie
    samodzielnej analizy
