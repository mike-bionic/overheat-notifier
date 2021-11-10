
import time
import board
import adafruit_dht
import os
from datetime import datetime, timedelta


delay_seconds = 30
last_time = datetime.now()

dhtDevice = adafruit_dht.DHT22(board.D18)
caution_message = "biraz gyzyp bashlady"
alert_message = "Alert Alert Alert!!!!!!"
phone_number = "+99361234567"


def send_message(message):
	if datetime.now() > last_time + timedelta(seconds = delay_seconds):
		os.system(f"python3 sendMessage {phone_number} '{caution_message}'")
		print("sending")
		last_time = datetime.now()

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        if temperature_c > 30 and temperature_c < 40:
            send_message(f"python3 sendMessage {phone_number} '{temperature_c}: {caution_message}'")
        elif temperature_c > 41:
            send_message(f"python3 sendMessage {phone_number} '{temperature_c}: {alert_message}'")

        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)
        continue
    except Exception as error:
        print(error)
        continue
        # dhtDevice.exit()
        # raise error

    time.sleep(1.0)