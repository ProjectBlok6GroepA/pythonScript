# pythonScript to provision device via serial interface

[TOC]

# Functions

## setup_serial_connection()

    In this function, a serial port is opened and a connection is made to a nRF developer kit containing the serial example made bij nordic.

    The setup process is done automatically by using the serial.tools.list_ports library. This library easilly gives a list of COM ports with devices connected. 

    As of now in version 0.1 the script only works when solely nRF DK kits are connected. If multiple nRF DK kits are used, the script will choose the first one it finds.

## close_serial_connection()

    This function is used to close the serial port at the end of the program.

## read_and_display()

    This function is used to read out the serial port for event responses recieved from the nRF DK. The device reads the first item in the serial buffer to check the length of the message sent. Then, it checks if there is anything else in the serial input buffer.

    The function uses a while loop to see if there is anything left in the serial buffer and keeps reading while this is the case. 

    After reading the full message, the response is printed to the commandline console. 

## write_serial(value)

    This function is used to write to the serial port. the parameter value contains a byte array of the hexadecimal values used to communicate with the nRF DK.

    After writing to the console, it calls for the read_and_display() function.

## Process_unprov_device()

    This function is used to specifically read the response 

## UnprovisionedDevice

    A class containing an unprovisioned device. This class will be passed to a provisioning function to complete the process. The class contains the device uuid and the provisioning state.

