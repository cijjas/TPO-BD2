import pandas as pd
import redis

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Cargar el archivo CSV
df = pd.read_csv('./resources/bataxi.csv')

# Importar los datos a Redis usando GEOADD
for index, row in df.iterrows():
    r.geoadd("bataxi", (row['origen_viaje_x'], row['origen_viaje_y'], row['id_viaje_r']))

