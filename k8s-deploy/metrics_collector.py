from prometheus_client import start_http_server, Gauge
import psutil
import time

#Создаем нужные метрики 
CPU_USAGE = Gauge('cpu_usage_percent', 'Current CPU usage in percent')
MEMORY_USAGE = Gauge('memory_usage_percent', 'Current RAM usage in percent')

def collect_metrics():
    while True:
        # Получаем метрики
        CPU_USAGE.set(psutil.cpu_percent())
        MEMORY_USAGE.set(psutil.virtual_memory().percent)
        time.sleep(5)

if __name__ == "__main__":
     #HTTP-сервер для Prometheus на 8000 порту
    start_http_server(8000)
    collect_metrics()