# Nexu Backend Coding Exercise

## Estructura

```
nexu-backend-test
│   README.md
│   requirements.txt
│   config.yml
│
└───src
│   │
│   └───nexu
│       │   __init__.py
│       │   scouts.py
│       │   version.py
│       └───web
│           │   __init__.py
│           │   __main__.py
│           │   wsgi.py
│           └───services
│               │    __init__.py
│               │    new_brand.py
│               │    new_model_brand.py
│               │    search_brands.py
│               │    search_model_filter.py
│               │    search_models.py
│               │    update_model.py
│   
└───static
└───templates
```

## Configuración

Versión de python utilizada: 3.8
Versión de pip utilizada: 22.2.2

* Colocarse dentro del directorio `nexu-backend-test`
* Usando consola del SO de preferencia crear nuevo entorno virtual:
```
$ virtualenv <env_name>
```
* Activar entorno virtual
```
$ source <env_name>/bin/activate
```
* Con el entorno virtual activo instalar paquetes requeridos
```
(<env_name>)$ pip install -r requirements.txt
```
En caso de encontrarse a través de un proxy:
```
(<env_name>)$pip install --proxy http://<usr_name>:<password>@<proxyserver_name>:<port#> -r requirements.txt
```
* Editar `config.yml` con los datos de la BD de mongo

_**NOTA:** La base de datos utilizada es mongo, con una única colección. El id de los datos proporcionados, está en bd como \_id_ 

## Despliegue de la aplicación

### Consola
Teniendo el entorno virtual activo y encontradose dentro de `nexu-backend-test` usando la configuración por defecto:
```
python -m src.nexu.web.__main__
```
En caso de necesitar desplegar por otro puerto o utilizar otro archivo de configuración se puede utilizar:
```
python -m src.nexu.web.__main__ -p <port> -c <config.yml>
```

### Usando IDE PyCharm

![Employee data](static/Config_PyCharm.png?raw=true "Config PyCharm")
 Después de crear esa configuración dar click a botón de Run

## Debuggear aplicación

Repetir los pasos de `Usando IDE PyCharm` solo que utilizar el botón de Debug en esta ocasión

## Probando aplicación
Se incluye colección con todos los path del aplicativo para ser probado en postman. Se puede encontrar en `static/nexu-backend-test.postman_collection.json`

## Que no incluye el aplicativo
* Manejo de excepciones ajeno a los descritos en la funcionalidad de cada path.
* Comprobación de parámetros recibidos (longitudes, tipo de dato, etc)
* Códigos de error específicos en las respuestas que tienen algún error.