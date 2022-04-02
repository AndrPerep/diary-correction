# Исправление дневника

Проект исправляет записи на сайте электронного школьного дневника. Для работы необходим доступ к серверу дневника.  

### Установка
Файл `scripts.py` должен находиться в основной папке электронного дневника. [Репозиторий дневника с документацией](https://github.com/devmanorg/e-diary)  
В этой же папке должен находиться файл с базой данных `schoolbase.sqlite3`.

### Запуск
- Запустите в консоли django shell командой `python manage.py shell`;
- Скопируйте весь код из `scripts.py` в консоль;
- Используйте `schoolkid = get_schoolkid()`, а затем введите фамилию и имя ученика, для которого будет исправляться дневник: например, `Иванов Иван`.

Скрипт готов к работе. Действия выше необходимо выполнять при каждом запуске терминала.

### Использование
- `fix_marks(schoolkid)` исправит все плохие оценки ученика (двойки и тройки) на пятёрки;
- `remove_chastisements(schoolkid)` удалит все замечания ученика;
- `create_commendation(schoolkid)` создаст случайно выбранную из списка похвалу. Программа потребует ввести название предмета — например, `математика`. Похвала будет прикреплена для последнего урока по выбранному предмету.

### Цель проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).