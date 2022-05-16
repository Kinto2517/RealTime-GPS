from datetime import datetime, timedelta
import json
import uuid

import numpy as np
import pandas as pd
from pymongo import MongoClient
import isodate as ISODate

cluster = "mongodb+srv://admin:admin@cluster1.jxkbw.mongodb.net/carsGeo?retryWrites=true&w=majority"
client = MongoClient(cluster)
db = client['carsGeo']
firstDay1 = db.get_collection('firstDay1')

start = datetime.now()
end = start - timedelta(seconds=1800)

# BURADA SİSTEM SAATİNE GÖRE E
# lat_1 = []
# long_1 = []
# carid_1 = []
# myquery = {"Time": {"$gte": str(end.time()), "$lt": str(start.time())}}
# for x in firstDay1.find(myquery):
#     lat_1.append(x['Latitude'])
#     long_1.append(x['Longtitude'])
#     carid_1.append(x['Carid'])
#     print(x)



lat_5 = []
long_5 = []
carid_5 = []
a = 0
myquery = {"Carid": "5"}
for x in firstDay1.find(myquery):
    lat_5.append(x['Latitude'])
    long_5.append(x['Longtitude'])
    carid_5.append(x['Carid'])
    a += 1
#DATABASAEDEN ÇEKİLEN BİLGİLERİ DATAFRAMEYE AT
df1 = pd.DataFrame(np.column_stack([lat_5, long_5, carid_5]), columns=['Latitude', 'Longtitude', 'Carid'])
result = df1.to_json('car_five.json', orient="records")

# DATAFRAMEYİ JSONA ÇEVİR VE BU JSONDAN LAT LONG VE CARİD BİLGİLERİNİ AL (JSONA ÇEVİRMEDEN DE ASLINDA LAT LONG LİSTESİNİ GÖNDEREBİLİRİZ
input_file = open("./car_five.json")
json_array = json.load(input_file)
lat = []
long = []
carid = []
for i in range(30):
    lat.append(json_array[i]['Latitude'])
    long.append(json_array[i]['Longtitude'])
    carid.append(json_array[i]['Carid'])

def generate_uuid():
    return uuid.uuid4()


def generate_checkpoint(lat, long):
    a = 0
    for i in range(len(lat)):
        data = {}
        data['a'] = '00001'
        data['key'] = data['a'] + "_" + str(generate_uuid())
        data['latitude'] = lat[i]
        data['longtitude'] = long[i]
        message = json.dumps(data)
        print(message)
        a += 1


generate_checkpoint(lat, long)
