from flask import Flask

def create_app():
    app = Flask(__name__)

    # Настройка конфигурации (если необходимо)
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    app.config['MAX_CONTENT_PATH'] = 1024 * 1024 * 10  # 10 MB

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app