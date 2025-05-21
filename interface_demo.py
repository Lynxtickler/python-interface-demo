from abc import abstractmethod
from interfaces import implements, check_implements
from utils import plot_twist


class PowerSource:

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @abstractmethod
    def temperature(self):
        pass

    @temperature.setter
    @abstractmethod
    def temperature(self, value):
        pass


@implements(PowerSource)
class Engine:

    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def start(self):
        self._temperature = 90

    def stop(self):
        self._temperature = 0


# @implements(PowerSource)  # Uncomment this to get an error on startup
class EngineWithoutIgnition:

    def __init__(self):
        super().__init__()
        self._temperature = 0

    def stop(self):
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.getter
    def temperature(self, value):
        self._temperature = value


# @implements(PowerSource)  # Uncomment this to get an error on startup
class EngineWithoutTemperature:

    def __init__(self):
        super().__init__()

    def start(self):
        self._temperature = 90

    def stop(self):
        self._temperature = 0


class Car:
    """
    This class expects requires a PowerSource interface.
    """

    @check_implements("power_source", PowerSource)
    def __init__(self, power_source):
        super().__init__()
        self.power_source = power_source

    def start(self):
        self.power_source.start()

    def stop(self):
        self.power_source.stop()

    def overheat(self):
        self.power_source.temperature = 120

    def print_temp(self):
        print(f"Temperature: {self.power_source.temperature}")


def main():
    print("Hooray all good here!")
    input()
    eng = EngineWithoutIgnition()  # Uncomment this to get an error with the car
    eng = Engine()  # Comment this out to get an error with the car
    car = Car(eng)
    print("Here we have a car with a valid power source in the garage.")
    car.print_temp()
    input()
    print("Let's start it and let it idle for some time...")
    car.start()
    car.print_temp()
    input()
    plot_twist(car)


if __name__ == "__main__":
    main()
