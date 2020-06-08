import paho.mqtt.client as paho
import time
import matplotlib.pyplot as plt
import numpy as np
import serial
mqttc = paho.Client()

# Settings for connection
host = "localhost"
topic= "Mbed"
port = 1883

x = []
y = []
z = []
tilt = []

# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")
    info = msg.payload
    print(info.split())
    x.append(float(info.split()[0]))
    y.append(float(info.split()[1]))
    z.append(float(info.split()[2]))
    tilt.append(float(info.split()[3]))
    print(len(x))
    if(len(x))==20 :
        t = np.arange(0,20,1)
        fig, ax = plt.subplots(2, 1)
        ax[0].plot(t,x,label='X')
        ax[0].plot(t,y,label='Y')
        ax[0].plot(t,z,label='Z')
        ax[0].legend()
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Acc Vector')
        ax[1].stem(t,tilt)
        ax[1].set_xlabel('Time')
        ax[1].set_ylabel('Tilt')
        plt.show()
   
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

mqttc.loop_forever()