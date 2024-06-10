# Ejercicio 2 - Neo4J

## Contenidos

1. [Instrucciones](#instrucciones)
  - [Paso 1: Movimientos previos](#paso-1-movimientos-previos)
  - [Paso 2: Abrir la sandbox](#paso-2-abrir-la-sandbox)
  - [Paso 3: Generar la base de datos](#paso-3-generar-la-base-de-datos)
  - [Paso 4: Cargar la base de datos](#paso-4-cargar-la-base-de-datos)
  - [Paso 5: Cargar relaciones](#paso-5-cargar-relaciones)
2. [Ejercicios](#ejercicios)
  - [Ejercicio 2.a](#ejercicio-2a)
  - [Ejercicio 2.b](#ejercicio-2b)
  - [Ejercicio 2.c](#ejercicio-2c)
  - [Ejercicio 2.d](#ejercicio-2d)

## Instrucciones
### Paso 1: Movimientos previos

Abrir una sandbox en blanco en el sitio de Neo4J: https://sandbox.neo4j.com.

### Paso 2: Abrir la sandbox

Una vez seleccionada la sandbox en blanco, nos aseguramos que esté corriendo y le damos a 'open'

![Alt text](./resources/Pasted%20image%2020240529082108.png)

### Paso 3: Generar la base de datos 

Para generar la base de grafos, ejecutar desde la interfaz web de Neo4J el comando:

```bash
:play northwind-graph
```

![Alt text](./resources/Pasted%20image%2020240529082443.png)

### Paso 4: Cargar la base de datos

Trás ejecutar el comando, dirigirse a la página 2 y correr los primeros 3 comandos disponibles para usar, los cuales cargaran la base a través de un LOAD CSV:
![Alt text](./resources/Pasted%20image%2020240529082622.png)

Verificar que los comandos se ejecutaron correctamente:
![Alt text](./resources/Pasted%20image%2020240529082721.png)

### Paso 5: Cargar relaciones

Dirigirse a la página 3 y ejecutar los únicos 2 comandos disponibles, los cuales cargaran las relaciones para los datos subidos anteriormente.
![Alt text](./resources/Pasted%20image%2020240529082759.png)

Ahora nos encontramos en condiciones de realizar los ejercicios.
## Ejercicios
### Ejercicio 2.a
***¿Cuántos productos hay en la base?***

Desde la interfaz de web de Neo4J, ejecutar el siguiente comando:

```bash
MATCH (p:Product) RETURN count(p) AS totalProducts
```

La salida debería ser la siguiente:

![Alt text](./resources/Pasted%20image%2020240529083418.png)

### Ejercicio 2.b
***¿Cuánto cuesta el "Queso Cabrales"?***

Desde la interfaz de web de Neo4J, ejecutar el siguiente comando:

```bash
MATCH (p:Product {productName: "Queso Cabrales"}) RETURN p.unitPrice as price
```

La salida debería ser la siguiente:

![Alt text](./resources/Pasted%20image%2020240529083545.png)

### Ejercicio 2.c
***¿Cuántos productos pertenecen a la categoría "Condiments"?***

Desde la interfaz de web de Neo4J, ejecutar el siguiente comando:

```bash
MATCH (p:Product)-[:PART_OF]->(c:Category {categoryName: "Condiments"}) 
RETURN count(p) as totalCondiments
```

La salida debería ser la siguiente:

![Alt text](./resources/Pasted%20image%2020240529084055.png)

### Ejercicio 2.d
***Del conjunto de productos que ofrecen los proveedores de "UK", ¿Cuál es el nombre y el precio unitario de los tres productos más caros?***

Desde la interfaz de web de Neo4J, ejecutar el siguiente comando:

```bash
MATCH (p:Product)<-[:SUPPLIES]-(s:Supplier {country: "UK"})
RETURN p.productName AS productName, p.unitPrice AS unitPrice
ORDER BY p.unitPrice DESC
LIMIT 3
```

La salida debería ser la siguiente:

![Alt text](./resources/Pasted%20image%2020240529084151.png)
