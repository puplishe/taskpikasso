# Цель
1. Создать Django проект и приложение.
2. Использовать Django REST Framework для создания API.
3. Реализовать модель File, которая будет представлять загруженные файлы. Модель должна содержать поля:
file: поле типа FileField, используемое для загрузки файла.
uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.
processed: поле типа BooleanField, указывающее, был ли файл обработан.
4. Реализовать сериализатор для модели File.
5. Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели File, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.
6. Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.
7. Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.
8. Использовать Docker для развертывания проекта.
9. Реализовать механизм для обработки различных типов файлов (например, изображений, текстовых файлов и т.д.).
10. Предусмотреть обработку ошибок и возвращение соответствующих кодов статуса и сообщений об ошибках.

## Запуск
1. Клонировать репозиторий
2. Прописать docker-compose build
3. Прописать docker-compose up -d
4. Перейти на http://127.0.0.1:8000/api/upload/ и http://127.0.0.1:8000/api/files/ 
5. Также есть дока сформированная автоматически с помощью drf-spectacular