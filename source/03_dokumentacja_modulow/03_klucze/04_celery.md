# Celery

Celery[@celery] jest asynchroniczną kolejką zadań.
Zadania są dystrybuowane do kolejki z różnych źródeł, np. z aplikacji webowej.
Celery jest przeznaczone głównie do operacji zlecanych oraz wykonywanych w
czasie rzeczywistym. Jako kolejkę lub bazę na zlecone zadania możliwe jest
wykorzystanie wielu backend'ów np. redis czy rabbitmq.
W aplikacji korzystamy z Celery do wykonywania przetwarzania pobranych z
zewnętrznych serwisów (pracuj.pl) ofert.
