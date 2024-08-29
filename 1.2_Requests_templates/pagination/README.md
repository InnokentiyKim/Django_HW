# Пагинация

## Задание

Реализовать пагинацию по csv-файлу с [портала открытых данных](https://data.mos.ru/datasets/752), содержащего список остановок наземного общественного транспорта.

Для этого необходимо реализовать функцию отображение `stations.views.bus_stations`, формируя контекст, как показано в примере.

Путь к файлу хранится в настройках `settings.BUS_STATION_CSV`.

Для чтения csv-файла можно использовать [DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader).

![Пример результата](./res/result.png)

## Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить команду:

```bash
python manage.py runserver
```
