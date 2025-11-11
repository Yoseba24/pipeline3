
import logging
from flask import Flask, request

app = Flask(__name__)

# Configuración básica del log
logging.basicConfig(
    level=logging.INFO,  # Nivel de log (puedes usar DEBUG para más detalle)
    format='%(asctime)s [%(levelname)s] %(message)s',  # Formato del mensaje
)

@app.before_request
def log_request_info():
    app.logger.info(f"Petición entrante: {request.method} {request.path}")

@app.route('/')
def hola_mundo():
    app.logger.info("Se llamó al endpoint '/'")
    return "Hola Mundo 1"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    app.logger.info(f"Se llamó al endpoint '/saludo/{nombre}'")
    return f"Hola, {nombre}!"

if __name__ == '__main__':
    app.logger.info("Iniciando aplicación Flask...")
    app.run(host='0.0.0.0', port=8080)

    