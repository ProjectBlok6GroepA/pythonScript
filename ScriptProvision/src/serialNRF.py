import serial
import serial.tools.list_ports;
import time


ser = serial.Serial()


class Opcodes:
    ECHO = 0x02


class Device:
    uuid = None


def setup_serial_connection():
    global ser
    available_ports = [comport.device for comport in serial.tools.list_ports.comports()]

    print(available_ports)  # Print list of comports

    comport = ''.join(available_ports[0])

    ser.baudrate = 115200
    ser.port = comport
    ser.open()

    print("Serial port is open: " + str(ser.is_open))


def close_serial_connection():
    global ser
    ser.close()


def read_and_display():
    time.sleep(1)
    s = ser.read(1)
    waiting = ser.in_waiting
    while waiting != 0:
        s = s + ser.read(1)
        waiting = ser.in_waiting
    print(s.hex())
    ser.reset_input_buffer()
    print()


def write_serial(value):
    ser.write(value)
    read_and_display()


def process_unprov_device():
    time.sleep(1)
    s = ser.read(27)
    print(s.hex())
    print()


def main():
    print("hello world")
    setup_serial_connection()
    ser.reset_input_buffer()
    write_serial(b'\x06\x02\x48\x41\x4c\x4c\x4f')
    write_serial(b'\x01\x61')
    process_unprov_device()
    write_serial(b'\x01\x62')
    close_serial_connection()


if __name__ == "__main__":
    main()
