import redis

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

places = [
    {"place": "Parque Chas", "lon": -58.479258, "lat": -34.582497},
    {"place": "UTN", "lon": -58.468606, "lat": -34.658304},
    {"place": "ITBA Madero", "lon": -58.367862, "lat": -34.602938}
]

total_viajes = 0
viajes_por_lugar = {}

for place in places:
    viajes_cerca = r.georadius("bataxi", place["lon"], place["lat"], 1, unit='km')
    num_viajes_cerca = len(viajes_cerca)
    total_viajes += num_viajes_cerca
    viajes_por_lugar[place["place"]] = num_viajes_cerca

print(f"b. Total de viajes a 1 km de los 3 lugares: {total_viajes}")

for lugar, count in viajes_por_lugar.items():
    print(f"-- Total de viajes a 1 km de {lugar}: {count}")

print(f"")
total_keys = r.dbsize()
print(f"c. Total de KEYS en la base de datos: {total_keys}")
print(f"")

miembros_bataxi = r.zcard("bataxi")
print(f"d. Total de miembros en la key 'bataxi': {miembros_bataxi}")
