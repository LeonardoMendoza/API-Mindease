from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, Perla :D!'

@app.route('/')
def status():
    return 'OK'

@app.route('/hola_choki')
def saludos_choki():
    return 'Kionda pa'

if __name__ == '__main__':
    # Configura la variable de entorno FLASK_ENV
    app.config['FLASK_ENV'] = 'production'
    app.run()


