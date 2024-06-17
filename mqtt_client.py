import paho.mqtt.client as mqtt

# MQTT Broker Einstellungen
broker = "mqtt.wara.lan"
port = 1883
topic = ""

# Callback-Funktion für Verbindung
def on_connect(client, userdata, flags, rc):
    print(f"Verbunden mit dem Broker. Ergebniscode: {rc}")
    client.subscribe(topic)

# Callback-Funktion für Nachrichten
def on_message(client, userdata, msg):
    print(f"Nachricht empfangen: {msg.payload.decode()} auf Thema: {msg.topic}")

# MQTT-Client initialisieren
client = mqtt.Client()

# Callback-Funktionen festlegen
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("user", "password")
# Verbindung zum Broker herstellen
client.connect(broker, port, 60)

# Nachricht senden
client.publish(topic, "Hallo, MQTT!")

# Starten der Netzwerk-Schleife
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Beende das Programm...")
finally:
    client.disconnect()