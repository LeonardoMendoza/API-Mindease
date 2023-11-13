from flask import Flask
import os

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def status():
    return 'OK'

if __name__ == '__main__':
    # Configura la variable de entorno FLASK_ENV
    app.config['FLASK_ENV'] = 'production'
    app.run()


