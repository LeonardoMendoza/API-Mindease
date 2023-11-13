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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='mindeaseapi.azurewebsites.net', port=port)


