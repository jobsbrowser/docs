# Uruchomienie

Do uruchomienia API korzystamy z polecenia `python manage.py runserver`.
Aby uruchomić usługę z odpowiednimi ustawieniami trzeba ustawić zmienną
środowiskową `APP_CONFIG` na wartość *PRODUCTION*. Możemy to zrobić korzystając
z 1 z poniższych poleceń:

-   ```bash
    export APP_CONFIG="production" && python manage.py runserver
    ```
-   ```bash
    APP_CONFIG="PRODUCTION" python manage.py runserver
    ```