# Dodatek B: Zawartość załączonej płyty DVD {.unnumbered}

1. `thesis.pdf` - plik PDF zawierający całą treść pracy
2. `title.pdf` - strona tytułowa
3. `abstract_pl.pdf` - streszczenie w języku polskim
4. `abstract_en.pdf` - streszczenie w języku angielskim
5. `src/` - katalog z kodem źródłowym systemu. Jego zawartość jest szerzej opisana w dokumentacji
powykonawczej (dod. A)
6. `vm/` - obraz maszyny wirtualnej z zainstalowaną i skonfigurowaną
instancją systemu. Instrukcja jej uruchomienia znajduje się poniżej.


**Uruchomienie maszyny wirtualnej**

Obraz maszyny wirtualnej zawiera system operacyjny
Debian 9 i przeznaczony jest
do użytku z narzędziem Virtualbox. Po uruchomieniu obrazu należy zalogować się
przy pomocy danych:

+ użytkownik: `vagrant`
+ hasło: `vagrant`

a następnie wykonać komendę:

`jobsbrowser_start`

Uruchomiona zostanie sesja programu *tmux* z trzema oknami. W nich uruchomione
są poszczególne moduły systemu. Aplikacja WWW jest teraz dostępna na porcie
`8080` uruchomionej maszyny.
