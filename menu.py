def input_courier(courier: list) -> Courier:
    """
    prompts the user to enter information for a new courier 
    and returns the created courier object.

    Args:
    couriers (list): The existing list of couriers.

    Returns
    Courier: The newly created courier object.
    """
    display_title("Add a New courier")

    # Collect last name -cannot be empty
    last_name:str = input("  Last name   : ").strip()
    while not last_name:
        print("Last name cannot be ampty.")
        last_name = input("First name   : ").strip()

        #Collect last name -cannot be empty
        first_name:str = input("  First name   : ").strip()
    while not first_name:
        print("First name cannot be ampty.")
        first_name = input("  First name   : ").strip()
        
        # Collect and validate phone number
        phone:str = input("  Phone(8 digits)   : ").strip()
    while not validate_phone(phone):
        print("Phone number must contain exactly 8 digits.")
        phone = input("   Phone(8 digits)   : ").strip()

        # Collect and validate email address
        email:str = input("  Email   : ").strip()
    while not validate_email(email):
        print("Invalid email -must contain '@' and '.'.")
        last_name = input("First name   : ").strip()

        # Collect vehicle type - connot be empty
    vehicle= input("  Vehicle type (motorbike / car / bicycle) : ").strip()
    while not vehicle:
        print("Vehicle type cannot be ampty.")
        vehicle = input("Vehicle type   : ").strip()

        # Collect delivery zone - connot be empty
        zone: str = input("  Delivery zone : ").strip()
    while not zone:
        print("Delivery zone cannot be ampty.")
        zone = input("Delivery zone   : ").strip()

        # Create and return the new Courier object 
        new_courier = courier(last_name, first_name, phone, email, vehicle, zone)
        print(f"\n Coursier {first_name} {last_name} added!(ID: {new_courier.get_courier_id()})")
        return new_courier

    def display_all_couriers(couriers: list):
        """
        Displays the full list of all registered couriers with their availability.
Shows a message if not coursiers are registered yet

args:
    couriers (list): The list of all coursier objects.
    """
        display_title("All registered couriers")

        # Check if the list is empty
        if not couriers:
         print(" No coursiers registered yet.")
        return
    
    # for loop to display each courier's information
    for index, coursier in enumerate(courier, start=1):
        coursier.display_info()
        # Show availability status explicitly
        status_label = " available" if courier.is_available() else " Unavailable"
        print(f" Status     : {status_label}")
        display_separator()

