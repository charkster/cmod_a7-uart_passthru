#!/usr/bin/python3
import serial, time

ser = serial.Serial()
ser.port         = "/dev/ttyS0"
ser.baudrate     = 2000000
ser.bytesize     = serial.EIGHTBITS     # number of bits per bytes
ser.parity       = serial.PARITY_NONE   # set parity check: no parity
ser.stopbits     = serial.STOPBITS_ONE  # number of stop bits
ser.timeout      = None                    # options: None, 0, x where None is wait forever, 0 is return immediately, x is a float in seconds
ser.xonxoff      = False                # disable software flow control
ser.rtscts       = False                # disable hardware (RTS/CTS) flow control
ser.dsrdtr       = False                # disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2                    # timeout for write

ser.open()
ser.flushInput()  # flush input buffer, discarding all its contents
ser.flushOutput() # flush output buffer, aborting current output and discard all that is in buffer

num_bytes = 0
while (num_bytes < 11):
	response = ser.read()
	print("read data: {}".format(response))
	num_bytes += 1

ser.write(b'Hello World')
ser.close()
