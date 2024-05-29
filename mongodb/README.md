
# Mongodb

## Movimiento previos
Antes que nada, instalamos la imagen de mongo y la corremos.

Cuando ya tenemos mongo corriendo en el puerto deseado podemos empezar a pasarle los archivos de interés (en este caso hay uno único en la carpeta `resources`).

`docker cp ../resources/albumlist.csv Mymongo:/home/`

una vez que tenemos el archivo en el contenedor, importamos el csv a la base de datos (tenemos que estar adentro del contenedor `docker exec -it Mymongo bash`)

`mongoimport --db music --collection albums --type csv --file /home/albumlist.csv --headerline`

Estos dos comandos se pueden ejecutar con `sh eja.sh` pero como son para setear el entorno de trabajo decidimos ponerlo en este apartado del README.md. 

## Comprobar que funciona

Usaremos mongo shell para enviar las consultas de los ejercicios b,c y d al puerto correspondiente para ver el funcionamiento correcto.

Para proceder con la ejecución de las consultas moverse a la carpeta `scripts` luego ejegutar el archivo `.sh` correspondientes.

| inciso |descripción| ejecución  |
| --------- |--| ---------- |
| b         |Cuente la cantidad de álbumes por año y ordénelos de manera descendente (mostrando los años con mayor cantidad de álbumes al principio).| `sh ejb.c` |
| c         |A cada documento, agregarle un nuevo atributo llamado 'score' que sea 501-Number.| `sh ejc.c` |
| d         |Realice una consulta que muestre el 'score' de cada artista.| `sh ejd.c` |

