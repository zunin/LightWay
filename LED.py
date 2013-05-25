import RPi.GPIO as GPIO
from time import sleep


class LED:
    """An LED that can light up"""
    def __init__(self, kathode, annode):
        self.kathode = kathode
        self.annode = annode
    def light(self):
        def __init__(self, pulsetime=0.003, pausetime = 0.5):
            self.pulsetime = pulsetime
            self.pausetime = pausetime

        GPIO.setup(self.kathode, GPIO.OUT)
        GPIO.setup(self.annode, GPIO.OUT)

        led = GPIO.PWM(self.kathode, 100)
        led.start(0)
        GPIO.output(self.annode, GPIO.LOW)
        for i in range(0, 101):
            led.ChangeDutyCycle(i)
            sleep(self.pulsetime)
        for i in range(100, -1, -1):
            led.ChangeDutyCycle(i)
            sleep(self.pulsetime)
        led.stop()

        GPIO.setup(self.kathode, GPIO.IN)
        GPIO.setup(self.annode, GPIO.IN)

        sleep(self.pausetime)

        #For debugging
        print("I am lighting up using", self.kathode, "as kathode and", self.annode, "as annode")


class LEDs:
    """This class contains the charlieplexing setup for 32 LEDs"""
    def __init__(self, pin1, pin2, pin3, pin4, pin5, pin6, pin7):
        self.chain1 = [
            LED(pin1,pin2),
            LED(pin2,pin1),
            LED(pin1,pin3),
            LED(pin3,pin1),
            LED(pin1,pin4),
            LED(pin4,pin1),
            LED(pin1,pin5),
            LED(pin5,pin1)
        ]

        self.chain2 = [
            LED(pin1,pin6),
            LED(pin6,pin1),
            LED(pin1,pin7),
            LED(pin7,pin1),
            LED(pin2,pin3),
            LED(pin3,pin2),
            LED(pin2,pin4),
            LED(pin4,pin2)
        ]

        self.chain3 = [
            LED(pin2,pin5),
            LED(pin5,pin2),
            LED(pin2,pin6),
            LED(pin6,pin2),
            LED(pin2,pin7),
            LED(pin7,pin2),
            LED(pin3,pin4),
            LED(pin4,pin3)
        ]

        self.chain4 = [
            LED(pin3,pin5),
            LED(pin5,pin3),
            LED(pin3,pin6),
            LED(pin6,pin3),
            LED(pin3,pin7),
            LED(pin7,pin3),
            LED(pin4,pin5),
            LED(pin5,pin4)
        ]

