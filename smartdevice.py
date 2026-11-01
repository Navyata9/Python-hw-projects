from abc import ABC, abstractmethod

class smartdevice(ABC):
    def show_device(self, name):
        print("Device Name:", name)

    @abstractmethod 
    def turn_on(self):
        pass

class smartlight(smartdevice):
    def turn_on(self):
        print("Smart Light is turned on.")

class smartfan(smartdevice):
    def turn_on(self):
        print("Smart Fan is turned on")

class smartspeaker(smartdevice):
    def turn_on(self):
        print("Smart Speaker is turned on.")

light= smartlight()
fan= smartfan()
speaker= smartspeaker()

light.show_device("Bedroom  light")
light.turn_on()
fan.show_device("Living room fan")
fan.turn_on()
speaker.show_device("Kitchen speaker")
speaker.turn_on()

class securitycamera:
    def check_status(self):
        print("Security Camera is recording.")

class doorlock:
    def check_status(self):
        print("Door Lock is secured.")

devices= [securitycamera(), doorlock()]

for device in devices:
    device.check_status()



