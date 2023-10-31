# build-in libraries
import logging

# Added libraries
import serial

# Project libraries
from tools import *


class UartFTDI(object):
    """
    Uart methods.
    """

    def __init__(self, port="COM3", baud_rate=57600):
        """
        Class constructor.
        :param port: Port designator.
        :param baud_rate: Speed to set into uart peripheral.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.ser = None

        try:
            self.ser = serial.Serial(self.port, self.baud_rate, timeout=0.2)

            # Close the serial if it is open
            if self.ser.isOpen:
                self.ser.close()

            # Open the serial
            self.ser.open()
            logging.debug('Serial is open!')

        except serial.SerialException as e:
            logging.error(f"Failed to receive data: {e}")

    def send(self, hex_buffer, reply=False):
        """
        Send data to uart and waits reply if "cont" is set to True.

        :param hex_buffer: {__iter__} Hex values format.
        :param reply: {bool} Say whether the command needs to wait the answer ot not.
        :return: Data if expected, None otherwise.
        """
        data = None
        try:
            # Clean serial buffer
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()

            crc = bytes.fromhex('00')

            stx = bytes.fromhex(hex_buffer[0])
            size = bytes.fromhex(hex_buffer[1])
            byte_buffer = [stx, size]
            size = int.from_bytes(size, 'big')
            hex_buffer = hex_buffer[-size:]

            for hex_val in hex_buffer:
                byte_val = bytes.fromhex(hex_val)
                byte_buffer.append(byte_val)
                crc = byte_xor(crc, byte_val)

            crc = byte_xor(crc, bytes.fromhex('ff'))
            byte_buffer.append(crc)

            # Send the buffer
            data = [int.from_bytes(val, 'big') for val in byte_buffer]
            self.ser.write(data)
            logging.debug(f"TX: {byte_buffer}")
            if reply:
                data = self.__receive()
            else:
                data = None

        except serial.SerialException as e:
            data = None
            logging.error(f"Failed to send data: {e}")

        finally:
            return data

    def __receive(self):
        """
        Receive a string o data and return it.

        :return: Data from the target or None if something happens.
        """
        try:
            data = self.ser.readall()

            if data:
                hex_buffer = [format(byte, '02x') for byte in data]
                crc = bytes.fromhex('00')

                received_crc = bytes.fromhex(hex_buffer[-1])

                hex_buffer_only_payload = hex_buffer[2:-1]
                for hex_val in hex_buffer_only_payload:
                    byte_val = bytes.fromhex(hex_val)
                    crc = byte_xor(crc, byte_val)

                crc = byte_xor(crc, bytes.fromhex('ff'))

                if received_crc == crc:
                    logging.debug(f"RX: {hex_buffer}")
                    return hex_buffer

                else:
                    logging.debug("Invalid CRC!")
                    return None
            else:
                logging.debug("No data received!")
                return None

        except serial.SerialException as e:
            logging.error(f"Failed to receive data: {e}")
            return None

    def __del__(self):
        """
        Destructor to close the serial port when the object is deleted.
        """
        if self.ser and self.ser.isOpen():
            self.ser.close()
