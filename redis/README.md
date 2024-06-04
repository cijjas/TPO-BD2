# Movimientos previos

Para poder correr los comandos, se necesita tener el contenedor de redis corriendo.

>[!Note]
> Obtener imagen: `docker pull redis`
>
> Correr en el puerto 6379: `docker run --name Myredis -p 6379:6379 -d redis`
> - esto es importante porque si se cambia de puerto hay que alterar los scripts de python
> 
> Comprobar que está corriendo: `docker ps -a | grep Myredis`

Se decidió ejecutar las en python ya que es un lenguaje que se usa mucho con redis y porque la [documentación de redis](https://redis.io/docs/latest/develop/data-types/geospatial/) nos muestra también ejemplos con python. Además es una buena herramienta ya que en la mayoria de las aplicaciones que podrían usar redis lo más probable es que se haga a través la librería específica.

Para eso, se deben tener instaladas las librerías `pandas` y `redis`.

`pip3 install pandas`
`pip3 install redis`

Finalmente podes proceder a la ejecució de las consultas y tareas.


# Comprobando que funciona

| Ejercicio | Ejecución              |
| --------- | ---------------------- |
| a         | `python3 import_data.py` |
| b, c, d   | `python3 query_data.py`  |

Finalmente para responder la pregunta **e: ¿Sobre qué estructura de Redis trabaja el GeoADD?**:

El comando `GEOADD` trabaja sobre la estructura de datos `Sorted Set`, donde las coordenadas son almacenadas como elementos del set con la puntuación correspondiente a las coordenadas geohash.

> The way the sorted set is populated is using a technique called [Geohash](https://en.wikipedia.org/wiki/Geohash). Latitude and Longitude bits are interleaved to form a unique 52-bit integer. We know that a sorted set double score can represent a 52-bit integer without losing precision.
> 
> This format allows for bounding box and radius querying by checking the 1+8 areas needed to cover the whole shape and discarding elements outside it. The areas are checked by calculating the range of the box covered, removing enough bits from the less significant part of the sorted set score, and computing the score range to query in the sorted set for each area.
> 
> - [Documentación de GEOADD](https://redis.io/docs/latest/commands/geoadd/)


