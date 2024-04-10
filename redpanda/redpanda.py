import json
import time 

from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

server = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=json_serializer
)

# producer.bootstrap_connected()

import pandas as pd
columns = ['lpep_pickup_datetime',
'lpep_dropoff_datetime',
'PULocationID',
'DOLocationID',
'passenger_count',
'trip_distance',
'tip_amount']

df_green = pd.read_csv('redpanda/green_tripdata_2019-10.csv', encoding='utf-8',usecols=columns)


# print(df_green)


t0 = time.time()

topic_name = 'green-topic'

for row in df_green.itertuples(index=False):
    row_dict = {col: getattr(row, col) for col in row._fields}
    print(row_dict)
    producer.send(topic_name, value=row_dict)
    # break
producer.flush()

t1 = time.time()
print(f'took {(t1 - t0):.2f} seconds')

