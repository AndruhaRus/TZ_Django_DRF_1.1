# TZ_Django_DRF_1.1

### Описание реализации сервиса для формирования и прохождения тестов
Данный проект представляет собой сервис, разработанный с использованием Django и Django REST Framework (DRF), предназначенный для создания и прохождения тестов. Сервис позволяет формировать набор вопросов с вариантами ответов "Да" или "Нет" и указывать правильный ответ для каждого вопроса. По результатам тестирования доступна общая информация о тесте, включающая количество прохождений, процент успешного прохождения и самый сложный вопрос.

### Особенности и функциональность
Разработано с использованием Django и DRF, популярных фреймворков для разработки веб-приложений на Python.
Для хранения данных используется встроенный функционал базы данных SQLite3, что исключает необходимость установки и настройки внешней базы данных.
В проекте реализованы модели Question (вопрос) и TestResult (результат теста) для представления данных о вопросах и прохождении тестов.
Запросы к API выполняются посредством созданных представлений (views) и использования сериализаторов для преобразования данных в формат JSON.
Для получения дополнительной информации о тесте использован класс TestAnalytics с отдельными методами для расчета количества прохождений, процента успешного прохождения и самого сложного вопроса.
Авторизация не требуется, сервис доступен для всех пользователей.

### Установка и запуск проекта
Убедитесь, что на вашей машине установлен Python 3.11.

### Создайте виртуальное окружение и активируйте его:
```
python3.11 -m venv myenv
source myenv/bin/activate  # для Linux/macOS
myenv\Scripts\activate  # для Windows
```

### Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### Выполните миграции базы данных:
```
python manage.py migrate
```
### Создайте суперпользователя для доступа к административной панели Django:
```
python manage.py createsuperuser
```

### Запустите локальный сервер разработки:
```
python manage.py runserver
```

Теперь вы можете открыть API в браузере по адресу http://127.0.0.1:8000/api/ и выполнять запросы к нему.

### Использование API
API предоставляет следующие конечные точки (endpoints):

- questions/: Конечная точка для работы с вопросами. Вы можете выполнять CRUD-операции (создание, чтение, обновление, удаление) вопросов с использованием запросов HTTP (GET, POST, PUT, PATCH, DELETE).
  URL(http://127.0.0.1:8000/api/questions/)
- results/: Конечная точка для работы с результатами тестов. Аналогично вопросам, вы можете выполнять CRUD-операции для управления результатами тестирования.
  URL(http://127.0.0.1:8000/api/results/)
- questions/difficult_question/: Конечная точка для получения самого сложного вопроса. Запрос GET к этой конечной точке вернет информацию о вопросе, считаемом самым сложным в соответствии с имеющимися данными.
  URL(http://127.0.0.1:8000/api/questions/difficult_question/)

### Дополнительные комментарии
В проекте использованы лучшие практики разработки с использованием Django и DRF.
Файлы models.py, serializers.py, views.py и analytics.py предоставляют детали имплементации моделей, сериализаторов, представлений и класса для аналитических отчетов. Вы можете вносить изменения в эти файлы для дальнейшей доработки функциональности.
Документация по API доступна на конечной точке http://127.0.0.1:8000/api/docs/.
Возможно использование других инструментов авторизации в проекте (например, JSON Web Tokens или OAuth), но в данной реализации авторизация не требуется.
Вклад
Этот проект является результатом выполнения тестового задания и предоставлен в качестве демонстрации навыков разработки с использованием Django и DRF.

Автор
Автором проекта является [AndreyRus].
