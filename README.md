# k8s-deployment-arm64
##Развертывание single node кластера k8s с использованием Docker Desktop на arm64 архитектуре:
###1) Развернем single node кластер
###2) Напишем плейбук для установки и добавление репозитория внутри пода: kubectl, helm, helm repo
###3) Напишем python скрипт который использует prometheus_server на 8000 порту куда идут логи метрик CPU/RAM
###4) Напишем Dockerfile и соберем образ под arm64 архитектуру
###5) Развернем Deployment kind (1 под) и Service kind(для доступа к 8000 порту)
###6) с помощью kubectl настроим port-forwarding 



#1)Необходимо включить k8s в настройках Docker Desktop (там есть галочка Enable Kubernetes)
Settings → Kubernetes → Enable → Apply & Restart

#2) Установим ansible:
###a) brew install ansible (или ansible-core), после этого в директории Ansible наполняем файлы из данного репозитория
###b) запустим плейбук ansible-playbook k8s-setup.yml и смотрим RECAP, если все ок - идем дальше

#3) Убедимся, что установлен python, проверим командой python --version и проверим путь до бинарника командой whereis python (т.к я устанавливал пайтон отдельно под своего юзера у меня это будет команда whereis python 3 и путь должен быть /usr/bin/python3)
###a) Используя модуль prometheus_server и psutil создаем метрики, пишем бесконечный цикл для постоянного забора метрик с интервалом 5 секунд, создаем сервис http на 8000 порту (можете указать любой, но учтите, что тогда нужно переписать порт во всех файлах докера и куба)

#4) Создаем Dockerfile (можно взять из репозитория) собираем его и запускаем:
###a) Собираем: docker build -t metrich-collector . (-t это тег образа, "." в конце указывает на текущую папку , если путь до докерфайла не в этой папке укажите полный путь до него
###b) Запускаем: docker run -t metrics-collector

#5)Развертываем 2 kind сущности в k8s (создаем Deployment и Service ямлы):
###a) применяем конфигурации командами: kubectl apply -f deployment.yaml | kubectl apply -f service.yaml

#6)Пробросим порт 8000 для открытия странички с метриками по адресу http://localhost:8000
###a) kubectl port-forward svc/metrics-collector-service 8000:8000 (svc в данном случае указание kind - service)


