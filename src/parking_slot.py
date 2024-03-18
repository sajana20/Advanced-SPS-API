from src.ultrasonic_sensor import UltrasonicSensor

class ParkigSlot:
    def __init__(self,
                 id: int = None,
                 echo_pin: int = None,
                 trig_pin: int = None,
                 down_dist: float = 10.0,
                 up_dist: float = 12.0):

        self.id = id
        self.echo_pin = echo_pin
        self.trig_pin = trig_pin
        self.down_dist = down_dist
        self.up_dist = up_dist
        self.ultrasonic_sensor = UltrasonicSensor()
        self.state = "Available"

        self.distance_sensor = self.ultrasonic_sensor.get_distance(trig_pin, echo_pin)
        self.check_status()

    # def check_status(self):


    def set_status(self):
        # TODO: take the current distance

        curr_distance = self.distance_sensor.distance()

        if self.up_dist < curr_distance:
            self.status = '1'
        elif self.down_dist > curr_distance:
            self.status = '0'
        else:
            self.status = self.status

        return self.status