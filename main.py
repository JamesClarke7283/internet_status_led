from utils import check_internet
import time
import os
import board
import digitalio

if os.environ["BLINKA_MCP2221"] == "1":
    print("Using MCP2221")
else:
    print("Need to set BLINKA_MCP2221=1")


led = digitalio.DigitalInOut(board.G0)
led.direction = digitalio.Direction.OUTPUT

while True:
    if check_internet():
        print("Internet is up!")
        led.value = True
    else:
        print("Internet is down!")
        led.value = False
    time.sleep(2)
