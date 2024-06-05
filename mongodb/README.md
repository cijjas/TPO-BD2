
# Ejercicio 1 - Mongodb

##Configuración
Para la configuración de Mongo es necesario haber instalado Docker previamente
### Paso 1: Descargar la imagen de MongoDB
Utiliza el siguiente comando para descargar la imagen oficial de MongoDB:
```bash
docker pull mongo
```

### Paso 2: Levantar el contenedor
```bash
docker run --name Mymongo -p 27017:27017 -d mongo
```

## Ejercicio 1.a
***Importe el archivo albumlist.csv (o su versión RAW) a una colección. 
Este archivo cuenta con el top 500 de álbumes musicales de todos los tiempos según la revista Rolling Stones.***

Copiar el archivo CSV al contenedor

```bash
docker cp mongodb/resources/albumlist.csv Mymongo:/home/
```
Ejecutar el comando de importación dentro del contenedor

```bash
docker exec -it Mymongo mongoimport --db music --collection albums --type csv --file /home/albumlist.csv --headerline
```

***

Para correr cada consulta, primero se deben correr los siguientes comandos:

```bash
docker exec -it Mymongo bash ##Levanta un Shell bash dentro del contenedor
```
```bash
mongosh ##Ejecuta el Shell de MongoDB
```
```bash
use music ##Para usar la base de datos 'music'
```

## Ejercicio 1.b
***Cuente la cantidad de álbumes por año y ordénelos de manera descendente (mostrando los años con mayor cantidad de álbumes al principio).***

Dentro de la shell de MongoDB ejecutar la consulta:
```bash
db.albums.aggregate([
  { $group: { _id: "$Year", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]).forEach(printjson);
```
***
## Ejercicio 1.c
***A cada documento, agregarle un nuevo atributo llamado 'score' que sea 501- Number.***

Dentro de la shell de MongoDB ejecutar la consulta:
```bash
db.albums.updateMany(
  {},
  [{ $set: { score: { $subtract: [501, "$Number"] } } }]
);
```
***
## Ejercicio 1.d
***Realice una consulta que muestre el 'score' de cada artista.***


Dentro de la shell de MongoDB ejecutar la consulta:
```bash
db.albums.aggregate(
  {$group: {_id:"$Artist", score: {$sum:"$score"}}}
);
```