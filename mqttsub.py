import paho.mqtt.client as paho
import json
import pandas as pd
import pymysql.cursors
from datetime import datetime
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
pd.set_option('max_columns', 50)

#connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='',
#
#                             db='colibri',
#                             autocommit=True,
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("CONNACK received with code %d." % (rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/SERM")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.payload:
        print(msg.payload)
        #datalist =  list(msg.payload)
        #print(datalist.pop(0))
        #print(datalist.pop(1))
        #print(datalist.pop(2))
    else:
        print("empty message")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
    
client = paho.Client(clean_session=True)

client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.connect("broker.hivemq.com", 1883, 0)

client.loop_forever()

