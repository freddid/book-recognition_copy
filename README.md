# Book Recognition

Book Recognition - это веб-приложение, которое использует камеру для захвата изображения обложки книги и предоставляет информацию о книге. Приложение разработано с использованием Flask, TensorFlow и других технологий.

## Структура проекта

book_recognition/
│
├── app/
│ ├── static/
│ │ ├── css/
│ │ │ └── styles.css
│ │ ├── js/
│ │ │ └── scripts.js
│ │ └── uploads/
│ ├── templates/
│ │ ├── index.html
│ │ └── result.html
│ ├── model.py
│ ├── routes.py
│ └── init.py
├── data/
│ ├── book-covers/
│ └── main_dataset.csv
├── model_training/
│ └── train_model.py
├── app.py
└── requirements.txt

## Технологии

- Flask
- numpy
- tensorflow
- tensorflow.keras
- pandas
- Pillow

## Установка и запуск

### Установка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/book_recognition.git
    cd book_recognition
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

### Обучение модели

1. Поместите обложки книг в папку `data/book-covers` и создайте файл `main_dataset.csv` с информацией о книгах.
2. Запустите обучение модели:
    ```bash
    python model_training/train_model.py
    ```

### Запуск приложения

1. Убедитесь, что модель сохранена в `app/model/book_model.h5`.
2. Запустите Flask приложение:
    ```bash
    python app.py
    ```

3. Перейдите в браузере по адресу [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Использование

1. Откройте веб-приложение в браузере.
2. Разрешите доступ к камере.
3. Нажмите кнопку "Capture", чтобы сделать снимок обложки книги.
4. Приложение отправит изображение на сервер для распознавания.
5. Результат распознавания будет отображен на странице.

## Структура файлов

- `app.py` - Главный файл для запуска Flask приложения.
- `app/__init__.py` - Инициализация приложения Flask.
- `app/routes.py` - Маршруты для обработки запросов.
- `app/model.py` - Функции для загрузки и использования модели.
- `model_training/train_model.py` - Скрипт для обучения модели.
- `app/templates/` - Шаблоны HTML.
- `app/static/css/` - Стили CSS.
- `app/static/js/` - Скрипты JavaScript.
- `app/static/uploads/` - Загрузка изображений.
- `data/` - Данные для обучения и CSV файл с информацией о книгах.

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами:

- Email: ugodayconzass1995@gmail.com
- GitHub: Fred(https://github.com/freddid)

## Лицензия

Этот проект лицензируется на условиях MIT License - подробности см. в файле LICENSE.