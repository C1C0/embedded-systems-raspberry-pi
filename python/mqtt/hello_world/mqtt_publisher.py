import paho.mqtt.publish as publish
import constants as C

publish.single(C.TOPICS_TEST, "Hello World!", hostname=C.MQTT_SERVER)