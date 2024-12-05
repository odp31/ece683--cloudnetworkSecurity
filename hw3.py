import RPi.GPIO as GPIO
import time

# define GPIO pins
button_pin = 18
led_pin = 21

# set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

# debouncing function
def debounce(pin):
  while GPIO.input(pin):
    time.sleep(0.02)

# main loop
try:
  while True:
    debounce(button_pin)
    GPIO.output(led_pin, not GPIO.input(led_pin))
    print("LED state:", GPIO.input(led_pin))

except KeyboardInterrupt:
  GPIO.cleanup()
