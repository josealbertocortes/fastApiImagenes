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
    if(path.exists(getcwd()+'/imagenes/'+file.filename)):
        id = client.imagen.imagen.find_one({'nombre':file.filename})
        id =id['_id']
        with open(getcwd()+'/imagenes/'+file.filename,"wb") as myfile:
            content = await file.read()
            myfile.write(content)
            myfile.close()
    else:
        with open(getcwd()+'/imagenes/'+file.filename,"wb") as myfile:
            content = await file.read()
            myfile.write(content)
            myfile.close()
        id = client.imagen.imagen.insert_one({"nombre":file.filename}).inserted_id
    return {"msg":"imagen subida","id":str(id)}