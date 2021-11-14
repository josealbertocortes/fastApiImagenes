from fastapi import FastAPI,UploadFile,File
from fastapi.responses import FileResponse,JSONResponse
from fastapi.datastructures import UploadFile
from config.db import client
from bson import ObjectId
from os import getcwd,path,mkdir, remove

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

@app.get("/imagen/{id}")
def get_imagen(id:str):
    nameimagen = client.imagen.imagen.find_one({"_id":ObjectId(id)})
    return FileResponse(getcwd()+"/imagenes/"+nameimagen['nombre'])

@app.get("/download/{id}")
def get_imagen(id:str):
    nameimagen = client.imagen.imagen.find_one({"_id":ObjectId(id)})
    return FileResponse(getcwd()+"/imagenes/"+nameimagen['nombre'],media_type="application/octet-stream",filename=nameimagen['nombre'])



