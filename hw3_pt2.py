import machine
import time

# Define GPIO pin for the LED
led_pin = machine.Pin(27, machine.Pin.OUT)

def blink_led(frequency):
    """Blinks the LED at the specified frequency.

    Args:
        frequency: The blinking frequency in Hz.
    """
    period = 1 / frequency
    while True:
        led_pin.value(1)
        time.sleep(period / 2)
        led_pin.value(0)
        time.sleep(period / 2)

if __name__ == "__main__":
    while True:
        try:
            frequency = float(input("Enter blinking frequency (Hz): "))
            blink_led(frequency)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
