import serial

__author__ = 'zunin'

class RFID_reader:
    def __init__(self, read_timeout=1):
        self.ser = serial.Serial(port='/dev/ttyAMA0', baudrate=2400, timeout=read_timeout) #start serial port@2400baud named ser
        self.buffered_message = False

    def hasTag(self):
        if len(self.message()) == 0:
            return False
        else:
            return True

    def message(self):
        serial_input = self.ser.read(12)[1:11]
        return serial_input

    def hasNewMessage(self):
        if self.buffered_message == self.message():
            return False
        else:
            self.buffered_message = self.message()
            return True