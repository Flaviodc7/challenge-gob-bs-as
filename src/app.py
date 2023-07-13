from flask import Flask

from config import config

from routes import estacion

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Page not found</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(estacion.main, url_prefix='/estacioncercana')

    # Manejando error 404
    app.register_error_handler(404, page_not_found)
    app.run()