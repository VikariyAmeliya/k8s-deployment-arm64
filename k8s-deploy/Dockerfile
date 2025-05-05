FROM python:3.9-slim #готовый легковесный образ с пайтоном без лишних пакетов
WORKDIR /app #устанавливаем рабочую директорию
COPY requirements.txt . #копируем зависимости для работы нашего скрипта 
RUN pip install -r requirements.txt #устанавливаем зависимости для скрипта
COPY metrics_collector.py . #копируем сам скрипт
EXPOSE 8000 # говорим о том, что сервис будет работать на 8000 порту
CMD ["python", "metrics_collector.py"] #запускаем скрипт
