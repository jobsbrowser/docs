# Wykonanie (SPA)

Aplikacja wykonana została w technologii *SPA* z użyciem frameworka **Vue.js**[@vuejs]

SPA to skrót od *Single Page Application*. Nazywamy tak stronę internetową,
która do zmiany prezentowanej użytkownikowi treści, np. podczas przejścia do innej
zakładki w menu, nie wymaga przeładowania - czyli pobierania raz jeszcze pełnego dokumentu
HTML przez przeglądarkę użytkownika. Znaczącą rolę pełni na takiej stronie język JavaScript,
To napisany w nim kod odpowiada za obsługę wydarzeń na stronie (np. kliknięcie przycisku w menu),
wykonywanie zapytań do serwera w tle (przy użyciu techniki AJAX) oraz podmianę
widocznej przez użytkownika struktury HTML tak aby pasowała do nowych danych.

Aplikacje takie często uważane są za przyjemniejsze w obsłudze, ponieważ sprawiają
wrażenie bardziej "natywnych" - znacząco skracają czas oczekiwania użytkownika
podczas interakcji czy urozmaicają go płynnymi przejściami (paskami postępu, kręcącymi
się spinnerami, itp.). Są one bardziej zoptymalizowane, ponieważ podczas interakcji
z użytkownikiem nie wymagają od serwera wielokrotnego generowania tych samych danych, np.
powtarzającego się kodu HTML.

Do wyboru tej technologii przyczyniły się trzy zasadnicze powody:

1. Aplikacja WWW pełniąca rolę interfejsu użytkownika powinna zapewniać
dynamiczną interakcję z użytkownikiem. Zastosowanie odpowiedniego frameworku
znacznie usprawnia proces implementacji funkcjonalności takich jak auto-uzupełnianie
podczas wprowadzania nazwy technologii czy rozwijanie kafelka zawierającego informacje
o ofercie.

2. Frameworki napisane w języku JavaScript, poza samą możliwością stworzenia SPA
oferują często rozbudowany system do tworzenia samego interfejsu. Skupiają w sobie
takie rzeczy jak obsługa kontrolek, data binding czy gotowe style CSS. Wykorzystanie
ich znacznie usprawnia prace nad aplikacją WWW.
 
3. Czasy generowania statystyk dla nowego zbioru technologii są nieco dłuższe niż
przeciętny czas ładowania się nowej strony, do którego przyzwyczajony jest użytkownik.
Wiąże się to z obliczeniami które odbywają się w tle po stronie modułu analitycznego.
Zastosowanie estetycznej animacji widocznej w trakcie ładowania się danych zwiększy
komfort użytkownika, a możliwość pobrania z serwera samych danych, bez zbędnego narzutu
w postaci kodu HTML, skróci potrzebny na odpowiedź czas.
