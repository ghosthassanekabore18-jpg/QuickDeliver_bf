# =============================================================================
# QuickDeliver_BF — DELIVERY MANAGEMENT SYSTEM
# menu.py — User interaction functions (input handling and display)
# Menu is coded by Cheick, Ezekiel and Hassane
# Burkina Institute of Technology 
# =============================================================================

# IMPORTS 
from models import Client, Courier, Parcel, Delivery, VALID_STATUSES
from file_handler import save_delivery, save_report
from utils import (validate_phone, validate_email, validate_weight,
                   display_separator, display_title,
                   find_available_courier, find_delivery_by_id)


# =============================================================================
#                          MAIN MENU — By Hassane
# =============================================================================

def display_main_menu():
    """Displays the DeliveryX main menu with all available options."""
    print("\n" + "=" * 60)
    print("   DELIVERYX — MAIN MENU")
    print("=" * 60)
    print("  1. Add a new client")
    print("  2. Add a new courier")
    print("  3. Create a new delivery")
    print("  4. Track a delivery")
    print("  5. Update delivery status")
    print("  6. View all clients")
    print("  7. View all couriers")
    print("  8. View all deliveries")
    print("  9. Generate report")
    print("  0. Quit")
    print("-" * 60)
