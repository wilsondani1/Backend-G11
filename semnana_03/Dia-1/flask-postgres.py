from flask import Flask, request
#from psycopg2 import connect

app = Flask(__name__)
# me conecto a la bd


@app.route('/', methods = ['GET'])
def inicial():
    return {
        'message': 'Bienvenido a mi API'
    }

@app.route('/alumnos', methods = ['GET', 'POST'])
def alumnos():
    if request.method == 'GET':
        return {
            'message':'yo soy el GET'
        }
    elif request.method == 'POST':
        return {
             'message':'yo soy el POST'

        }
        



if __name__ == '__main__':
    # debug > indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug = True)