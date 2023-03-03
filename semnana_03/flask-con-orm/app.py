from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ

load_dotenv()

app=Flask(__name__)
#print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

conexion.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
