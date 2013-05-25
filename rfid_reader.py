import serial

__author__ = 'zunin'

class RFID_reader:
    def __init__(self, port='/dev/ttyAMA0', read_timeout=1):
        self.ser = serial.Serial(port=port, baudrate=2400, timeout=read_timeout) #start serial port@2400baud named ser
        self.buffered_message = False

    def has_tag(self):
        if len(self.message()) == 0:
            return False
        else:
            return True

    def message(self):
        serial_input = self.ser.read(12)[1:11]
        return serial_input

    def has_new_message(self):
        if self.buffered_message == self.message():
            return False
        else:
            self.buffered_message = self.message()
            return True