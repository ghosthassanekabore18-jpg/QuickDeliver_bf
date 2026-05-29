# QUICKDELIVER_BF — DELIVERY MANAGEMENT SYSTEM
# models.py — All classes : Person, Client, Courier, Parcel, Delivery
# Burkina Institute of Technology 

import datetime
import uuid

VALID_STATUSES = ("pending", "in_transit", "delivered", "cancelled")
BASE_RATE_PER_KG: float = 500.0     # FCFA per kilogram
MINIMUM_FEE: float = 1000.0         # Minimum shipping fee in FCFA
FRAGILE_SURCHARGE: float = 0.20     # 20% surcharge for fragile parcels


# =============================================================================
# PARENT CLASS — Person
# Coded by : Nimatou
# =============================================================================

class Person:
    """
    Parent class representing a person in the QuickDeliver_BF system.
    Serves as the base class for Client and Courier.
    Demonstrates : Encapsulation (private attributes) and Abstraction.
    """

    def _init_(self, last_name: str, first_name: str, phone: str, email: str):
        """
        Initialises a person with their basic personal information.


class Person:
    """
    Parent class representing a person in the QuickDeliver_BF system.
    Serves as the base class for Client and Courier.
    Demonstrates : Encapsulation (private attributes) and Abstraction.
    """

    def __init__(self, last_name: str, first_name: str, phone: str, email: str):
        """
        Initialises a person with their basic personal information.

        Args:
            last_name (str): The person's last name.
            first_name (str): The person's first name.
            phone (str): The person's phone number.
            email (str): The person's email address.
        
        # Private attributes — encapsulation
        self._last_name: str = last_name
        self._first_name: str = first_name
        self._phone: str = phone
        self._email: str = email

    # --- Getters ---

    def get_last_name(self) -> str:
        """Returns the last name of the person."""
        return self._last_name

    def get_first_name(self) -> str:
        """Returns the first name of the person."""
        return self._first_name

    def get_phone(self) -> str:
        """Returns the phone number of the person."""
        return self._phone

    def get_email(self) -> str:
        """Returns the email address of the person."""
        return self._email

    # --- Setters ---

    def set_phone(self, phone: str):
        """
        Updates the phone number of the person.

        Args:
            phone (str): The new phone number.
        """
        if phone.strip():   # check that the value is not empty
            self._phone = phone

    def set_email(self, email: str):
        """
        Updates the email address of the person.

        Args:
            email (str): The new email address.
        """
        if email.strip():   # check that the value is not empty
            self._email = email

    def display_info(self):
        """
        Displays the basic information of the person.
        This method is overridden in child classes (polymorphism).
        """
        print(f"  Name    : {self._first_name} {self._last_name}")
        print(f"  Phone   : {self._phone}")
        print(f"  Email   : {self._email}")

    def __str__(self) -> str:
        """Returns a short string representation of the person."""
        return f"{self._first_name} {self._last_name} — {self._phone}"




# CHILD CLASS : Courier
# Coded by : Ezekiel
# Inherits from : Person





class Courier(Person):
    """
    Represents a courier who transports parcels.
    Inherits from Person — demonstrates Inheritance and Polymorphism.
    """

    def __init__(self, last_name: str, first_name: str, phone: str,
                 email: str, vehicle: str, zone: str):
        """
        Initialises a courier with personal and professional information.

        Args:
            last_name (str): The courier's last name.
            first_name (str): The courier's first name.
            phone (str): The courier's phone number.
            email (str): The courier's email address.
            vehicle (str): Vehicle type (motorbike, car, bicycle...).
            zone (str): The geographical delivery zone.
        """
        # Call the parent constructor — inheritance
        super().__init__(last_name, first_name, phone, email)

        # Courier-specific private attributes
        self._vehicle: str = vehicle
        self._zone: str = zone
        self._courier_id: str = str(uuid.uuid4())[:8].upper()  # auto-generated unique ID
        self._completed_deliveries: list = []                   # list of delivery IDs
        self._available: bool = True                            # available by default

    # --- Getters ---

    def get_courier_id(self) -> str:
        """Returns the unique identifier of the courier."""
        return self._courier_id

    def get_vehicle(self) -> str:
        """Returns the vehicle type used by the courier."""
        return self._vehicle

    def get_zone(self) -> str:
        """Returns the delivery zone of the courier."""
        return self._zone

    def is_available(self) -> bool:
        """Returns True if the courier is available, False otherwise."""
        return self._available

    # --- Setters ---

    def set_availability(self, available: bool):
        """
        Updates the availability status of the courier.

        Args:
            available (bool): True if available, False if busy.
        """
        self._available = available

    # --- Methods ---

    def add_delivery(self, delivery_id: str):
        """
        Records a completed delivery in the courier's history.

        Args:
            delivery_id (str): The unique ID of the completed delivery.
        """
        self._completed_deliveries.append(delivery_id)

    def display_info(self):
        """
        Displays the full information of the courier.
        Overrides Person.display_info() — demonstrates Polymorphism.
        """
        # Availability shown as readable text
        status = "Available" if self._available else "Busy"

        print(f"  Courier ID  : {self._courier_id}")
        print(f"  Name        : {self._first_name} {self._last_name}")
        print(f"  Phone       : {self._phone}")
        print(f"  Email       : {self._email}")
        print(f"  Vehicle     : {self._vehicle}")
        print(f"  Zone        : {self._zone}")
        print(f"  Status      : {status}")
        print(f"  Deliveries  : {len(self._completed_deliveries)}")

    def display_completed_deliveries(self):
        """Displays all delivery IDs completed by this courier."""
        if not self._completed_deliveries:
            print("  No deliveries completed yet.")
        else:
            print(f"  Deliveries by {self._first_name} {self._last_name}:")
            # for loop to list each delivery
            for index, delivery_id in enumerate(self._completed_deliveries, start=1):
                print(f"    {index}. Delivery ID : {delivery_id}")

    def __str__(self) -> str:
        """Returns a short string representation of the courier."""
        availability = "Available" if self._available else "Busy"
        return f"[COURIER] {self._first_name} {self._last_name} — {self._zone} — {availability}"
