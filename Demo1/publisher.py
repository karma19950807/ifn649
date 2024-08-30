import paho.mqtt.publish as publish

publish.single("ifn649", "Hello World", hostname="3.237.203.68")
print("Done")