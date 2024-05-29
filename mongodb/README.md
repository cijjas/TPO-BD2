
# Mongodb

# Movimiento previos
Primero que nada, instalamos la imagen de mongo y la corremos.

Cuando ya tenemos mongo corriendo en el puerto deseado podemos empezar a pasarle los archivos de interés (en este caso hay uno único en la carpeta `resources`).

`docker cp ../resources/albumlist.csv Mymongo:/home/`

una vez que tenemos el archivo en el contenedor, importamos el csv a la base de datos (tenemos que estar adentro del contenedor `docker exec -it Mymongo bash`)

`mongoimport --db music --collection albums --type csv --file /home/albumlist.csv --headerline`

# Comprobar que funciona

Usaremos mongo shell para enviar las consultas de los ejercicios b,c y d al puerto correspondiente para ver el funcionamiento correcto.

Para proceder con la ejecución de las consultas moverse a la carpeta `scripts` luego ejegutar el archivo `.sh` correspondientes.

| ejercicio | ejecución  |
| --------- | ---------- |
| b         | `sh ejb.c` |
| c         | `sh ejc.c` |
| d         | `sh ejd.c` |

