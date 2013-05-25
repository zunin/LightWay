import LED

# Start setup
pin1 = 18
pin2 = 19
pin3 = 21
pin4 = 22
pin5 = 23
pin6 = 24
pin7 = 26

checkpoint = LED.LEDs(pin1, pin2, pin3, pin4, pin5, pin6, pin7)

# End setup

#Code
for led in checkpoint.chain1:
    led.light()

for led in reversed(checkpoint.chain1):
    led.light()