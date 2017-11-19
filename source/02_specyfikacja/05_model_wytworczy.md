# Model wytwórczy

Do wytworzenia opisywanego systemu wybraliśmy metodykę zwinną - Agile.
Jest ona jedną z najszybszych metod wytwarzania oprogramowania i idealnie
wpasowuje się w modułową strukturę architektury systemu.
Wybór tej metodyki oznacza prowadzenie prac w modelu iteracyjnym - komponent
po komponencie. W naszym przypadku oznacza to, że z każdą kolejną iteracją
gotowy projekt będzie powiększał się o nowy w pełni działający fragment.
Po pierwszym etapie będzie to moduł zbierający dane z zewnętrznych serwisów,
następnie moduł przechowujący i udostępniający zebrane dane, i tak dalej.

Wymagania funkcjonalne projektu zostały opracowane w pierwszej kolejności.
Pozwoliło to na nakreślenie zarysu systemu i tego na co musi pozwalać, bez
wdawania się w szczegóły implementacyjne. Po wyodrębnieniu komponentów systemu,
uznaliśmy że podejście kaskadowe byłoby zbyt ryzykowne. Zaprojektowanie
dokładnej struktury i szczegółowych wymagań implementacji każdego z nich już
na wstępie niosłoby za sobą ryzyko niedopasowania się do przewidzianego
na implementację czasu. Zachodziłoby również niebezpieczeństwo przeoczenia
błędów w planowaniu, które wyszłyby na powierzchnię dopiero w momencie
implementacji bądź testów, kiedy metoda kaskadowa nie przewiduje już 
zmiany wymagań ani planu. Jakość końcowego produktu zdecydowanie bardzo by na
tym ucierpiała.

Komponenty systemu są na tyle niezależne i wyizolowane, że mając opracowane
ogólne ich założenia i przeznaczenie, podczas każdej z iteracji jesteśmy
w stanie skupić się na nich indywidualnie, bez ingerowania w resztę projektu.
Pozwoli to na dokładne ich dopracowanie, co jest szczególnie istotne
biorąc pod uwagę że część z nich opiera się w znacznym stopniu na zewnętrznych
projektach i technologiach które do udanej integracji będą wymagały głębszego
poznania.




