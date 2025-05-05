FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY metrics_collector.py .
EXPOSE 8000
CMD ["python", "metrics_collector.py"]
