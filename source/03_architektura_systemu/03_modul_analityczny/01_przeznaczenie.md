# Przeznaczenie modułu

Dzięki robotowi zbierającemu dane do systemu trafiają pojawiające się 
w serwisie Pracuj.pl oferty. Dla przypomnienia, informacje jakie
uzyskiwane są bezpośrednio w trakcie ich pozyskiwania to:

+ tytuł
+ ID
+ treść (w postaci kodu HTML)

oraz kilka mniej znaczących z punktu widzenia tego komponentu, a szerzej opisanych w części dotyczącej
robota zbierającego dane.
Informacje te same w sobie nie są szczególnie istotne dla użytkownika końcowego aplikacji.
Są to bowiem te same dane które zobaczyć możemy korzystając bezpośrednio z serwisu pracuj.pl. Nie niosą
więc za sobą póki co żadnych dodatkowych wartości.\newline
Sednem aplikacji i systemu samego w sobie, jest przekształcenie dużego zbioru ofert w statystyki dotyczące ich wspólnych
elementów - czyli technologii które są w nich wymieniane. Moduł ten pozwala właśnie na to -
uzyskanie z pojedynczej oferty listy nazw technologii, które są zawarte w jej treści.
