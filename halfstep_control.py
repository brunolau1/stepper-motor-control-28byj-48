import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

control_pins = [7,11,13,15]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

step_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

for i in range(512):
  for step in range(len(step_seq)):
    for pin in range(4):
      GPIO.output(control_pins[pin], step_seq[step][pin])
    time.sleep(0.0008)

GPIO.cleanup()
