#  Interfejs

Moduł z pozostałymi komponentami systemu łączy się przez interfejs HTTP.
Dane do statystyk są dostarczane przez moduł ekstrakcji kluczy.
Natomiast konsumentem danych generowanych przez moduł statystyk jest aplikacja
WWW z której korzysta końcowy użytkownik.

Interfejs HTTP zaimplementowany jest przy użyciu frameworka Django[@django].
Django jest to jeden z największych oraz najprężniej rozwijanych narzędzi
Open Source.
Zdecydowaliśmy się na niego ze względu na to, że w tym module kluczowa jest
wydajność generowania odpowiednich statystyk, ale też duża elastyczność
w pisaniu kodu.
Django jako projekt niezwykle dojrzały, rozwijany przez bardzo doświadczonych
developerów z całego świata jest świetnie zoptymalizowany do tego typu zadań.


![Schemat modułu. \label{ref_a_figure}](source/figures/backend_diagram.png){ width=100% }

\clearpage
