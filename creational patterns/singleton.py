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


# Singleton base class
class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        """
        Ensure only one instance of each singleton class exists.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


# Concrete product: Car (Singleton)
class Car(Vehicle, Singleton):
    def get_type(self):
        """
        Implementation of the abstract method for Car.
        """
        return "This is a car."


# Concrete product: Bike (Singleton)
class Bike(Vehicle, Singleton):
    def get_type(self):
        """
        Implementation of the abstract method for Bike.
        """
        return "This is a bike."


# Concrete product: Truck (Singleton)
class Truck(Vehicle, Singleton):
    def get_type(self):
        """
        Implementation of the abstract method for Truck.
        """
        return "This is a truck."


# Client code
if __name__ == "__main__":
    # List of vehicle types to create
    vehicle_types = ["Car", "Bike", "Truck", "Car", "Bike"]

    for v_type in vehicle_types:
        if v_type == "Car":
            vehicle = Car()
        elif v_type == "Bike":
            vehicle = Bike()
        elif v_type == "Truck":
            vehicle = Truck()
        else:
            print(f"Unknown vehicle type: {v_type}")
            continue

        # Call the get_type method on the created vehicle
        print(vehicle.get_type())
        # Call shared methods
        print(vehicle.start_engine())
        print(vehicle.drive())
        print(vehicle.stop_engine())

    # Demonstrate that each type of vehicle is a Singleton
    car1 = Car()
    car2 = Car()
    print(f"Car instances are the same: {car1 is car2}")

    bike1 = Bike()
    bike2 = Bike()
    print(f"Bike instances are the same: {bike1 is bike2}")

    truck1 = Truck()
    truck2 = Truck()
    print(f"Truck instances are the same: {truck1 is truck2}")
