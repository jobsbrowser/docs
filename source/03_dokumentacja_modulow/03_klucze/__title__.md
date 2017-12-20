# Moduł ekstrakcji kluczy

Kod źródłowy znajduje się pod adresem:
[\url{github.com/jobsbrowser/pipeline}](https://github.com/jobsbrowser/pipeline).

Modułem systemu do którego trafiają przetwarzane oferty w następnej kolejności jest
moduł ekstrakcji kluczy - czyli wymaganych na stanowisko którego dotyczy ogłoszenie
umiejętności i technologii. To tutaj odbywa się, kluczowy z punktu widzenia biznesowego
zastosowania projektu, proces wyciągania z "surowych" ofert wartościowych informacji.
Wejściem modułu są zapisane w bazie oferty, natomiast wyjściem te same obiekty,
ale uzupełnione o listę kluczy wykrytych w ich treści.