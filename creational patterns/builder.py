from abc import ABC, abstractmethod


# Abstract base class: Vehicle
class Vehicle(ABC):
    def __init__(self):
        self.engine_started = False
        self.driving = False

    @abstractmethod
    def get_type(self):
        """
        Abstract method to return the type of vehicle.
        Must be implemented by all concrete subclasses.
        """
        pass

    def start_engine(self):
        """
        Common method to start the engine of the vehicle.
        """
        self.engine_started = True
        return f"{self.__class__.__name__} engine started."

    def stop_engine(self):
        """
        Common method to stop the engine of the vehicle.
        """
        self.engine_started = False
        return f"{self.__class__.__name__} engine stopped."

    def drive(self):
        """
        Common method to simulate driving the vehicle.
        """
        if self.engine_started:
            self.driving = True
            return f"{self.__class__.__name__} is driving."
        else:
            return f"{self.__class__.__name__} cannot drive without starting the engine."


# Concrete product: Car
class Car(Vehicle):
    def get_type(self):
        """
        Implementation of the abstract method for Car.
        """
        return "This is a car."


# Concrete product: Bike
class Bike(Vehicle):
    def get_type(self):
        """
        Implementation of the abstract method for Bike.
        """
        return "This is a bike."


# Concrete product: Truck
class Truck(Vehicle):
    def get_type(self):
        """
        Implementation of the abstract method for Truck.
        """
        return "This is a truck."


# Builder base class
class VehicleBuilder(ABC):
    def __init__(self):
        self.vehicle = None

    @abstractmethod
    def create_new_vehicle(self):
        pass

    def get_vehicle(self):
        return self.vehicle

    def start_engine(self):
        if self.vehicle:
            return self.vehicle.start_engine()

    def stop_engine(self):
        if self.vehicle:
            return self.vehicle.stop_engine()

    def drive(self):
        if self.vehicle:
            return self.vehicle.drive()


# Concrete Builder for Car
class CarBuilder(VehicleBuilder):
    def create_new_vehicle(self):
        self.vehicle = Car()


# Concrete Builder for Bike
class BikeBuilder(VehicleBuilder):
    def create_new_vehicle(self):
        self.vehicle = Bike()


# Concrete Builder for Truck
class TruckBuilder(VehicleBuilder):
    def create_new_vehicle(self):
        self.vehicle = Truck()


# Director
class VehicleDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_vehicle(self):
        self._builder.create_new_vehicle()


# Client code
if __name__ == "__main__":
    # List of vehicle types to create
    vehicle_types = ["Car", "Bike", "Truck", "Bus"]

    for v_type in vehicle_types:
        if v_type == "Car":
            builder = CarBuilder()
        elif v_type == "Bike":
            builder = BikeBuilder()
        elif v_type == "Truck":
            builder = TruckBuilder()
        else:
            print(f"Unknown vehicle type: {v_type}")
            continue

        director = VehicleDirector(builder)
        director.construct_vehicle()
        vehicle = builder.get_vehicle()

        # Call the get_type method on the created vehicle
        print(vehicle.get_type())
        # Call shared methods
        print(vehicle.start_engine())
        print(vehicle.drive())
        print(vehicle.stop_engine())
