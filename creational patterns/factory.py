from abc import ABC, abstractmethod


# Abstract base class: Vehicle
class Vehicle(ABC):
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
        return f"{self.__class__.__name__} engine started."

    def stop_engine(self):
        """
        Common method to stop the engine of the vehicle.
        """
        return f"{self.__class__.__name__} engine stopped."

    def drive(self):
        """
        Common method to simulate driving the vehicle.
        """
        return f"{self.__class__.__name__} is driving."


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


# Factory
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        """
        Factory method to create a vehicle instance based on the vehicle_type.
        """
        if vehicle_type == "Car":
            return Car()
        elif vehicle_type == "Bike":
            return Bike()
        elif vehicle_type == "Truck":
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")


# Client code
if __name__ == "__main__":
    # List of vehicle types to create
    vehicle_types = ["Car", "Bike", "Truck", "Bus"]

    for v_type in vehicle_types:
        try:
            # Use the factory to create the appropriate vehicle
            vehicle = VehicleFactory.get_vehicle(v_type)
            # Call the get_type method on the created vehicle
            print(vehicle.get_type())
            # Call shared methods
            print(vehicle.start_engine())
            print(vehicle.drive())
            print(vehicle.stop_engine())
        except ValueError as e:
            # Handle the case where an unknown vehicle type is requested
            print(e)
