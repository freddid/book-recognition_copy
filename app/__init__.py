from flask import Flask

app = Flask(__name__)

# Важно: конфигурация должна указывать на путь к папке загрузок
app.config['UPLOAD_FOLDER'] = 'app/static/uploads/'

from app import routes
