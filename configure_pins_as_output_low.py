import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

control_pins = [7,11,13,15]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
