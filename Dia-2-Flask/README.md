 ## crear un entorno virtual
 ......
 python -m venv venv 
 ......
 ## activar el entorno virtual 

# no usar el power shell
 venv\scripts\activate   
 source venv/Scripts/activate
 sourse venv/bin/activate

 ## desacativar entorno virtual
 deactivate
 # flast
 ## instalar flasK
 pip install flasK

 ## verificamos que flasK se instalo con 
 pip freeze

 ## listar las librerias en el archivo 'requirements.txt'

pip freeze > requirements.txt

 ## INSTALAR LAS LIBRERIAS QUE ESTAN listados en nuestro 'requirements.txt'
 pip install -r requirements.txt
