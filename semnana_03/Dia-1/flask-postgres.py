from flask import Flask, request
#from psycopg2 import connect

app = Flask(__name__)


if __name__ == '__main__':
    # debug > indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug = True)