#готовый легковесный образ с пайтоном без лишних пакетов
FROM python:3.9-slim 
#устанавливаем рабочую директорию
WORKDIR /app
#копируем зависимости для работы нашего скрипта
COPY requirements.txt . 
#устанавливаем зависимости для скрипта
RUN pip install -r requirements.txt 
#копируем сам скрипт
COPY metrics_collector.py .
#говорим о том, что сервис будет работать на 8000 порту
EXPOSE 8000 
#запускаем скрипт
CMD ["python", "metrics_collector.py"] 
