#!/bin/bash

# Copiar el archivo CSV al contenedor
docker cp ../resources/albumlist.csv Mymongo:/home/

# Ejecutar el comando de importación dentro del contenedor
docker exec -it Mymongo mongoimport --db music --collection albums --type csv --file /home/albumlist.csv --headerline

# En caso de que se quiera usar un host y puerto particular, usar la linea que está comentada
# mongoimport --host localhost:27017 --db tp-albums --collection albums --type csv --file /../resources/albumlist.csv --headerline
