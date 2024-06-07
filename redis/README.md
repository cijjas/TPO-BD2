
# Ejercicio 3 - Redis

### Paso 1: Movimientos previos

Asegurarse de estar parado sobre el directorio correspondiente al ejercicio `/redis`

### Paso 2: Descargar la imagen de Redis
Utiliza el siguiente comando para descargar la imagen oficial de Redis:
```bash
docker pull redis
```

### Paso 3: Levantar el contenedor
```bash
docker run --name Myredis -p 6379:6379 -d redis
```

## Ejercicio 3.a
***Importar los datos del archivo a Redis***

Se decidió importar el archivo vía python ya que es un lenguaje que se usa mucho con redis y porque la [documentación de redis](https://redis.io/docs/latest/develop/data-types/geospatial/) nos muestra también ejemplos con python. Además es una buena herramienta ya que en la mayoria de las aplicaciones que podrían usar redis lo más probable es que se haga a través la librería específica.

Para eso, se deben tener instaladas las librerías `pandas` y `redis`.

```sh
pip3 install pandas redis
```

luego para ejecutar el script que importará los datos al contenedor

```sh
python3 import_data.py
```

cuando termina de ejecutar se esparará ver la salida:
![[Pasted image 20240607092748.png]]


***

Para correr las siguientes consulta se deben correr los siguientes comandos:

```bash
## Abrir una Shell bash dentro del contenedor
docker exec -it Myredis bash 

## Abrir la shell de Redis
redis-cli 
```

## Ejercicio 3.b
***¿Cuántos viajes se generaron a 1 km de distancia de estos 3 lugares?***



***
## Ejercicio 3.c
***¿Cuántas KEYS hay en la base de datos Redis?***

```
DBSIZE
```

Debería observarse la siguiente salida

![[Pasted image 20240607104117.png]]

***
## Ejercicio 3.d
***¿Cuántos miembros tiene la key 'bataxi'?***

```
ZCARD bataxi
```


Debería observarse la siguiente salida

![[Pasted image 20240607104153.png]]
***
## Ejercicio 3.d
***¿Sobre qué estructura de Redis trabaja el GeoADD?***

El comando `GEOADD` trabaja sobre la estructura de datos `Sorted Set`, donde las coordenadas son almacenadas como elementos del set con la puntuación correspondiente a las coordenadas geohash.


> The way the sorted set is populated is using a technique called [Geohash](https://en.wikipedia.org/wiki/Geohash). Latitude and Longitude bits are interleaved to form a unique 52-bit integer. We know that a sorted set double score can represent a 52-bit integer without losing precision.
> This format allows for bounding box and radius querying by checking the 1+8 areas needed to cover the whole shape and discarding elements outside it. The areas are checked by calculating the range of the box covered, removing enough bits from the less significant part of the sorted set score, and computing the score range to query in the sorted set for each area.
> 
> - [Documentación de GEOADD](https://redis.io/docs/latest/commands/geoadd/)
