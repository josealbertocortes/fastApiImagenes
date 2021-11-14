# Fast Api Test1
Comenzaremos creando un ambiente virtual para no instalar los paquetes de manera global en la máquina, para esto usaremos virtualenv

    virtualenv -p python3 env
Activamos el ambiente virtual 

    source env/bin/activate

Una vez activado el ambiente virtual se comenzará con instalar fastApi y uvicorn


    pip install fastapi uvicorn


una vez instalado nuestros paquetes generaremos una endponit a la siguiente ruta '/api/sps/helloworld/v1 '
Se creara un CRUD a la ruta que se tratara sobre cocteles.



