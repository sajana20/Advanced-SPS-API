from src.parking_slot import ParkigSlot
from src.repositories.parking_area_repository import ParkingAreaRepository


class ParkigArea:
    def __init__(self):
        self.slots = 12 # Total spaces in this parking Area
        self.ECHO = 8
        self.TRIG = 10

        self.parking_slot = ParkigSlot(id=1,
                                      echo_pin=self.ECHO,
                                      trig_pin=self.TRIG
                                      )

        # Parking Lot available
        self.total_spaces = self.slots

        # All parkings state
        self.all_slots = {self.parking_slot:'Available'}
        self.availability_data = ParkingAreaRepository().get_parking_availability()

    def check_status_change(self):
        parking_spaces = list(self.all_slots.keys())
        print("check status change")
        print(parking_spaces)
        for parking in parking_spaces:
            past_status = self.all_slots[parking]
            current_status = parking.set_status()

            if past_status != current_status:
                self.all_slots[parking] = current_status
                self.update_parking_availability()

    def update_parking_availability(self):
        empty_spaces = 0

        for parking, state in self.all_slots.items():
            if state == 1:
                empty_spaces += 1

        # todo: # Send data to a web socket

        self.available_spaces = empty_spaces

