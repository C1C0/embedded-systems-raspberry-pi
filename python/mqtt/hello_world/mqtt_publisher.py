import paho.mqtt.client as mqtt
import constants as C

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

client = mqtt.Client(client_id="RP-S", userdata=None, protocol=mqtt.MQTTv5)

client.on_publish = on_publish

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(username=C.MQTT_USER, password=C.MQTT_PASS)

client.connect(C.MQTT_SERVER, C.MQTT_PORT, 60)
client.publish(C.TOPICS_TEST, payload="Hello My FRIEND!", qos=1)