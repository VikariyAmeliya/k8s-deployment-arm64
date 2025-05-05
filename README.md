# k8s-deployment-arm64

## Развертывание single node кластера k8s с использованием Docker Desktop на arm64 архитектуре:

1. **Развернем single node кластер**
2. **Напишем плейбук для установки и добавления репозитория внутри пода:** `kubectl`, `helm`, `helm repo`
3. **Напишем Python скрипт**, который использует `prometheus_server` на 8000 порту, куда идут логи метрик CPU/RAM
4. **Напишем Dockerfile** и соберем образ под arm64 архитектуру
5. **Развернем Deployment kind** (1 под) и **Service kind** (для доступа к 8000 порту)
6. **С помощью `kubectl` настроим port-forwarding**

---

### 1) Необходимо включить k8s в настройках Docker Desktop (там есть галочка Enable Kubernetes)
- **Settings → Kubernetes → Enable → Apply & Restart**

### 2) Установим Ansible:
- **a)** `brew install ansible` (или `ansible-core`), после этого в директории Ansible наполняем файлы из данного репозитория
- **b)** Запустим плейбук: `ansible-playbook k8s-setup.yml` и смотрим `RECAP`, если все ок — идем дальше

### 3) Убедимся, что установлен Python:
- Проверим командой: `python --version`
- Проверим путь до бинарника командой: `whereis python` (если Python установлен отдельно под пользователя, используйте `whereis python3`, путь должен быть `/usr/bin/python3`)
- **a)** Используя модуль `prometheus_server` и `psutil`, создаем метрики, пишем бесконечный цикл для постоянного забора метрик с интервалом 5 секунд, создаем сервис HTTP на 8000 порту (можете указать любой, но учтите, что тогда нужно переписать порт во всех файлах Docker и Kubernetes)

### 4) Создаем Dockerfile (можно взять из репозитория), собираем его и запускаем:
- **a)** Собираем: `docker build -t metrics-collector .` (`-t` — это тег образа, `.` в конце указывает на текущую папку; если путь до Dockerfile не в этой папке, укажите полный путь до него)
- **b)** Запускаем: `docker run -t metrics-collector`

### 5) Развернем 2 kind сущности в k8s (создаем Deployment и Service YAML-файлы):
- **a)** Применяем конфигурации командами:  
  `kubectl apply -f deployment.yaml`  
  `kubectl apply -f service.yaml`

### 6) Пробросим порт 8000 для открытия странички с метриками по адресу `http://localhost:8000`
- **a)** `kubectl port-forward svc/metrics-collector-service 8000:8000` (`svc` в данном случае указывает на kind — `service`)
