import copy
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

    def clone(self):
        """
        Create a copy of the vehicle instance.
        """
        return copy.deepcopy(self)


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


# Prototype Registry
class VehiclePrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register_vehicle(self, vehicle_type, prototype):
        """
        Register a vehicle prototype.
        """
        self._prototypes[vehicle_type] = prototype

    def unregister_vehicle(self, vehicle_type):
        """
        Unregister a vehicle prototype.
        """
        if vehicle_type in self._prototypes:
            del self._prototypes[vehicle_type]

    def get_vehicle(self, vehicle_type):
        """
        Get a cloned instance of the registered vehicle prototype.
        """
        prototype = self._prototypes.get(vehicle_type)
        if not prototype:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        return prototype.clone()


# Client code
if __name__ == "__main__":
    # Create vehicle prototypes
    car_prototype = Car()
    bike_prototype = Bike()
    truck_prototype = Truck()

    # Register prototypes
    registry = VehiclePrototypeRegistry()
    registry.register_vehicle("Car", car_prototype)
    registry.register_vehicle("Bike", bike_prototype)
    registry.register_vehicle("Truck", truck_prototype)

    # List of vehicle types to create
    vehicle_types = ["Car", "Bike", "Truck", "Bus"]

    for v_type in vehicle_types:
        try:
            # Use the registry to create a cloned vehicle
            vehicle = registry.get_vehicle(v_type)
            # Call the get_type method on the created vehicle
            print(vehicle.get_type())
            # Call shared methods
            print(vehicle.start_engine())
            print(vehicle.drive())
            print(vehicle.stop_engine())
        except ValueError as e:
            # Handle the case where an unknown vehicle type is requested
            print(e)
