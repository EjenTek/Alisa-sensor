# Alisa-sensor

1) Подключаем все необходимые датчики к Алисе
2) идем на https://oauth.yandex.ru/client/new/ для создания своего сервиса
    - Назваине любое какое нравится (например "Умный дом")
    - Платформы приложения - оставляяем только "Веб-сервисы", URL = https://oauth.yandex.ru/verification_code
    - Доступ к данным - добавляем "ioc:view" - для чтения, "ioc: control" - для управления (если оно потребуется, если нет, то не нужно)
3) Получаем ClientID
4) Прехедим по ссылке https://oauth.yandex.ru/authorize?response_type=token&client_id=ВашClientID и получаем Токен
5) можно протестировать полученый токен запросом url -i -X GET ‘https://api.iot.yandex.net/v1.0/user/info’ -H ‘Authorization: Bearer ВАШ ТОКЕН’ (получите полную информацию о всех устройствах)
6) записываем Device ID нужного устройства
7) тестируем устройство запросом curl -i -X GET ‘https://api.iot.yandex.net/v1.0/devices/Divice ID Вашего усройства’ -H ‘Authorization: Bearer Токен’
8) Получим информацию по конкретному устройству

На этом настройка и тестирование яндекса закончено.
Переходим кнастройке сервера Zabbix.

1) подключаемся по SSH
2) Создаем папку для скрипта и копируем скрипт
    mkdir /tmp/script
    wget sensor.py
3) Открываем скрипт и подставляем значения своего Токена и Device ID
    nano /tmp/script/sensor.py
4) делаем скрипт исполняемым
    chmod +x /tmp/script/sensor.py
5) Создаем расписание для пороса датчика каждые 10 минут
    crontab -e
    добавляем строку */10 * * * * /tmp/script/sensor.py
6) Проверяем работу скрипта. Запускаем его. В Папке со скриптом должны появиться файлы с названием параметра получаемого с помощью устройства и содержимым равного его значению (пример файл temperature со значение 22,3)
7) В конфигурации zabbix_agentd.conf добавляем пользовательские параметры полученые с помощью скрипта в любом удобном месте (как пример расматривается датчик температуры)
   nano /etc/zabbix/zabbix_agentd.conf
    UserParameter = temp, cat /tmp/script/temperature
    UserParameter = humidity, cat /tmp/script/humidity
    UserParameter = battery, cat /script/battery_level
8) Перезапускаем агента
    service zabbix-agent restart

Настрока из консоли закончена, переходим к настройке в веб интерфейсе Zabbix

