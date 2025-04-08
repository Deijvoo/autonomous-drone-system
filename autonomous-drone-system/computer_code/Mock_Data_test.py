import serial
import json
import time
import random

# Simulated position and velocity output
def generate_mock_data():
    return {
        "pos": [round(random.uniform(-1, 1), 2) for _ in range(4)],
        "vel": [round(random.uniform(-0.5, 0.5), 2) for _ in range(3)]
    }

# Serial to ESP32 sender
ser = serial.Serial('COM4', 1000000)

drone_index = 0

while True:
    payload = generate_mock_data()
    json_str = f"{drone_index}" + json.dumps(payload)
    ser.write(json_str.encode('utf-8'))
    print(f"Sent: {json_str}")
    time.sleep(0.1)
