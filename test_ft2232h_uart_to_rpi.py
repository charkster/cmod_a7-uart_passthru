from pyftdi.ftdi import Ftdi
import pyftdi.serialext
import time

Ftdi.show_devices()
port = pyftdi.serialext.serial_for_url('ftdi://ftdi:2232:210328AD3FF5/2', baudrate=2000000, bytesize=8, parity='N', stopbits=1)
port.write(b'Hello World')
time.sleep(1)
num_chars = 0
while (num_chars < 11):
	response = port.read()
	print("read data: {}".format(response))
	num_chars += 1
