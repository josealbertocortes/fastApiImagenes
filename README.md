# Fast Api SubirImagenes

### Crearemos un endpoint donde se puedan subir imágenes que se guardaran de manera local y guardaremos el nombre del archivo en mongodb para tenerlos identificados. 

Comenzaremos generando un ambiente virtual para no instalar los paquetes de manera global en la máquina, para esto usaremos virtualenv

    virtualenv -p python3 env
Activamos el ambiente virtual 

    source env/bin/activate

Una vez activado el ambiente virtual se comenzará con instalar fastApi, uvicorn, pymongo y python-multipart o podemos instalar el requirements.txt con pip install requirements.txt


    pip install fastapi uvicorn pymongo python-multipart


Una vez instalado nuestros paquetes generaremos una endponit a la siguiente ruta '/imagenes'

Nuestro archivo principal que contendrá la siguiente lógica 
1. Verificar si la carpeta imágenes existe si no crearla, ya que aquí se guardaran las imágenes
2. leer la imagen para después guardarla.
3. Revisar si el archivo ya existía, si ya exista se hace una consulta a la base de datos  de mongo para retornar el id , si no existía se hace una inserción a la base de datos, se obtiene el id.
4. Retornar un mensaje de imagen subida con el id.


```python
from fastapi import FastAPI,UploadFile,File
from fastapi.datastructures import UploadFile
from config.db import client
from os import getcwd,path,mkdir

app = FastAPI()

@app.post('/imagenes')
async def upload_imagen(file:UploadFile=File(...)):
    if path.exists(getcwd()+'/imagenes/'):
        pass
    else:
        mkdir(getcwd()+'/imagenes/')
    
    with open(getcwd()+'/imagenes/'+file.filename,"wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    
    if(path.exists(getcwd()+'/imagenes/'+file.filename)):
        id = client.imagen.imagen.find_one({'nombre':file.filename})
        id =id['_id']
    else:
        id = client.imagen.imagen.insert_one({"nombre":file.filename}).inserted_id
    return {"msg":"imagen subida","id":str(id)}
```

### Conexión a base de datos
Para la conexión a la base de datos se debe crear un cluster en mongo atlas y a través de 
la url proporcionado en mongo atlas que tiene la siguiente forma  'mongodb+srv://<username>:<password>@cluster0.cl3ku.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
donde se debe crear un usuario y contraseña. 

La configuración a la base de datos quedaría de la siguiente manera 
```python


import pymongo
# Replace the uri string with your MongoDB deployment's connection string.
conn_str = 'mongodb+srv://mern_user:S7tNE4ahVRZqr8Lu@cluster0.cl3ku.mongodb.net/'
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")
```
#### Probando el endpoint 
Para correr el aplicativo se deben colocar en la carpeta microservicios y ejecutar el siguiente comando 


`uvicorn app:app --reload`

La request para este endopoint será 
		file:archivo_de_imagen

La respuesta será la siguiente 

{"msg":"imagen subida","id":"54984113"}






