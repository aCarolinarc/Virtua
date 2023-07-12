from flask import Flask
from flask_cors import CORS
from obtener import Data

app = Flask(__name__)
CORS(app)

@app.route('/proof', methods=['GET'])
def prueba():
    return "Funciona correctamente"

@app.route('/mostrar', methods=['GET'])
def mostrar():
    return 

if __name__ == '__main__':
    app.run()