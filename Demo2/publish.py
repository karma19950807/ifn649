import paho.mqtt.publish as publish

publish.single("LED/Blink", "LED_ON", hostname="3.237.203.68")
print("LED_ON")
