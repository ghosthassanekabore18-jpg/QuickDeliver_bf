# =============================================================================
# QuickDeliver_BF — DELIVERY MANAGEMENT SYSTEM
# main.py — Entry point of the application
# Member 6 : Hassane
# Burkina Institute of Technology — Programming I with Python
# =============================================================================

# --- IMPORTS ---
from menu import (
    display_main_menu,
    input_client,
    input_courier,
    create_delivery,
    track_delivery,
    update_delivery_status,
    display_all_clients,
    display_all_couriers,
    display_all_deliveries,
    generate_report
)


def main():
    """
    Main function that launches the QuickDeliver_BF application.
    Initialises the data lists and runs the main menu loop
    until the user decides to quit.
    """

    # In-memory data lists for the current session
    clients: list = []
    couriers: list = []
    deliveries: list = []

    # Welcome banner
    print("=" * 60)
    print("   QuickDeliver_BF — DELIVERY MANAGEMENT SYSTEM")
    print("   Burkina Institute of Technology")
    print("   Programming I with Python — May 2026")
    print("=" * 60)
    print("   Welcome! Use the menu below to get started.")

    # Main application loop — runs until the user enters 0
    running: bool = True
    while running:
        display_main_menu()
        choice: str = input("Your choice : ").strip()

        # Option 1 : For add a new client 
        if choice == "1":
            new_client = input_client(clients)
            if new_client:
                clients.append(new_client)

        # Option 2 : For add a new courier 
        elif choice == "2":
            new_courier = input_courier(couriers)
            if new_courier:
                couriers.append(new_courier)

        # Option 3 : Create a new delivery 
        elif choice == "3":
            create_delivery(clients, couriers, deliveries)

        # Option 4 : Track a delivery by ID 
        elif choice == "4":
            track_delivery(deliveries)

        # Option 5 : Update the status of a delivery 
        elif choice == "5":
            update_delivery_status(deliveries)

        # Option 6 : Display all registered clients 
        elif choice == "6":
            display_all_clients(clients)

        # Option 7 : Display all registered couriers 
        elif choice == "7":
            display_all_couriers(couriers)

        # Option 8 : Display all deliveries 
        elif choice == "8":
            display_all_deliveries(deliveries)

        # Option 9 : Generate and save a report 
        elif choice == "9":
            generate_report(deliveries)

        # Option 0 : Quit the application 
        elif choice == "0":
            print("\nThank you for using QuickDeliver_BF. Goodbye! ")
            running = False

        # Invalid input 
        else:
            print("\n Invalid choice. Please enter a number between 0 and 9.")


# Entry point — only runs if this file is executed directly
if __name__ == "__main__":
    main()
