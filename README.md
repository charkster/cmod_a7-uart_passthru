# cmod_a7-uart_passthru
![picture](https://cdn11.bigcommerce.com/s-7gavg/images/stencil/320w/products/516/4033/Cmod_A7-obl-600__50330.1614011629.png)

This is a demonstration of UART communication using the FT2232 on the Cmod-a7 FPGA board. The TX and RX are passed through the FPGA to board pins, which then connect to my Raspberry Pi. Bi-directional communication is demonstrated in Python.

<p>Dependancies:<br>
pip3 install pyftdi<br>
pip3 install pyserial==3.4</p>

See the following repo for an example of Cmod-a7 external SRAM control using UART over the USB cable (FT2232H)
https://github.com/ricynlee/cmod-a7-uart-sram-test
