import RPi.GPIO as GPIO
import time

# define GPIO pin
led_pin = 23

#set up GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

def blink_led(frequency):
  period = 1
  while True:
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(period / 2)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(period / 2)

if __name__ == "__main__":
  try:
    while True:
      frequency = float(input("enter blinking frequency (Hz): "))
      blink_led(frequency)
  except KeyboardInterrupt:
    GPIO.cleanup()
    print("program terminated.")

