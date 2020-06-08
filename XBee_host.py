import paho.mqtt.client as paho
import time
import matplotlib.pyplot as plt
import numpy as np
import serial
mqttc = paho.Client()

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x136\r\n".encode())
char = s.read(3)
print("Set MY 0x136.")
print(char.decode())

s.write("ATDL 0x236\r\n".encode())
char = s.read(3)
print("Set DL 0x236.")
print(char.decode())

s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

# call RPC

print("start sending RPC")
for i in range(20):
    # send 20 times RPC to remote
    s.write("/myled1/write 0\r".encode())
    time.sleep(1)

# Get the data we collected

x=[]
y=[]
z=[]
tilt=[]
num=[]

for i in range(40):
    line=s.readline()
    x.append(line)
    line=s.readline()
    y.append(line)
    line=s.readline()
    z.append(line)
    line=s.readline()
    tilt.append(line)

for i in range(20):
    line=s.readline()
    num.append(line)
'''
# MQTT connection

host = "localhost"
topic= "Mbed"
port = 1883

# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect

mqttc.connect(host, port=1883, keepalive=60)


for i in range(20):
    mesg = x[i] + y [i] + z[i] + num[i]
    mqttc.publish(topic, mesg)
    print(mesg)
    time.sleep(1)
'''
for i in range(40):
    print(float(x[i]))
    print(float(y[i]))
    print(float(z[i]))
    print(float(tilt[i]))
    
'''
# draw
t = np.arange(0,20,1)
plt.plot(t,num, color = "blue", linewidth = 1)
plt.show()
'''
'''
t = np.arange(0,20,0.5)
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
'''
plt.show()
s.close()