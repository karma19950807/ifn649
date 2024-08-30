import paho.mqtt.publish as publish

publish.single("LED/Blink", "LED_OFF", hostname="3.237.203.68")
print("LED_OFF")
