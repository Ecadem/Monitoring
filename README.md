<!-- ![logo_transparent_background](https://user-images.githubusercontent.com/62354692/209298221-2cf465d6-9127-4f10-a4e4-b55b28d228ab.png) -->

<img src="https://user-images.githubusercontent.com/62354692/209298221-2cf465d6-9127-4f10-a4e4-b55b28d228ab.png" alt="drawing" width="600"/>

# monitoring

#### Esta API se encuentra desarrollada en python y su framework FastAPI.
Para hacer uso en local se debe contar con al menos una de las siguientes dos tecnologias:
- **Uvicorn**: Para mas información de como instalar uvicorn visitar la [Documentación de FastAPI](https://fastapi.tiangolo.com/tutorial/).
- **Docker**: Ver información para su instalación en los distintos sistemas operativos en la pagina oficial de [Docker](https://www.docker.com/).


### Con uvicorn
En la raiz de proyecto dirigirse a la carpeta `./app` y seguir los siguientes pasos:
1. `uvicorn main:app --reload --port 8000`
2. En el explorador web ingresar a la url `http://localhost:8000/docs`

### Con docker
En la raiz de proyecto dirigirse a la carpeta `./app` y seguir los siguientes pasos:
1. `docker build -t monitoring .`
2. `docker run -p 8000:8000 monitoring`
3. En el explorador web ingresar a la url `http://localhost:8000/docs`

*Nota: tener en cuenta ejecutar solo una de las dos opciones*

## Cargar al repositorio de imagenes de Ecadem
*_(Proximamente)_*
