# Internet Status LED

This is a simple script that checks if the internet is up and running. If it is, it will turn on a LED. If it is not, it will turn off the LED.

## Requirements
- python3.9 or higher
- psutil
- hidapi
- adafruit-blinka

## Installing System Dependencies
```bash
sudo apt-get install libusb-1.0 libudev-dev
```

## Installing Python Dependencies
```bash
pip3 install -r requirements.txt
```

## Setting up UDEV rules
```bash
sudo nano /etc/udev/rules.d/99-mcp2221.rules
```
Add the following line to the file:
```bash
SUBSYSTEM=="usb", ATTRS{idVendor}=="04d8", ATTR{idProduct}=="00dd", MODE="0666"
```

## Remove native driver
```bash
sudo rmmod hid_mcp2221
```

### Remove it from bootup
```bash
sudo nano /etc/modprobe.d/blacklist.conf
```

Add the following line to the file:
```bash
blacklist hid_mcp2221
```

### Update Initramfs
```bash
sudo update-initramfs -u
```

### Set environment variable
```bash
export BLINKA_MCP2221=1
```

### Run the script
```bash
python3 main.py
```