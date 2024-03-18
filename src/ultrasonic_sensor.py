import RPi.GPIO as GPIO
import time

class UltrasonicSensor():
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin

        # Setup the pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, GPIO.LOW)

    # calculate distance from time
    def get_distance(self):

        GPIO.output(self.trig, GPIO.HIGH)
        GPIO.output(self.trig, GPIO.LOW)

        start_time = time.time()
        end_time = time.time()

        while GPIO.input(self.trig)==0:
            start_time = time.time()
        while GPIO.input(self.trig)==1:
            end_time = time.time()

        duration = abs(end_time - start_time)
        self._distance = round(duration * 17150, 2)

        return self._distance

    def __del__(self):
        GPIO.cleanup()


