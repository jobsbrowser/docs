# Przeznaczenie modułu

Dzięki opisanym wcześniej modułom w bazie danych systemu znajdują się
zbierane z serwisu pracuj.pl oferty. Dla przypomnienia, informacje jakie
uzyskiwane są bezpośrednio w trakcie ich pozyskiwania to:

+ tytuł
+ ID
+ treść (w postaci kodu HTML)

oraz kilka mniej znaczących z punktu widzenia tego komponentu, a szerzej opisanych w części dotyczącej
modułu zbierania danych.
Informacje te same w sobie nie są szczególnie istotne dla użytkownika końcowego naszej aplikacji.
Są to bowiem te same dane które zobaczyć możemy korzystając bezpośrednio z serwisu pracuj.pl. Nie niosą
więc za sobą póki co żadnych dodatkowych wartości.\newline
Sednem naszej aplikacji jest przekształcenie dużego zbioru ofert w statystyki dotyczące ich wspólnych
elementów - czyli umiejętności i technologii które są w nich wymieniane. Moduł ten pozwala właśnie na to -
uzskanie z pojedynczej oferty listy takich kluczy, które są zawarte w jej treści.
