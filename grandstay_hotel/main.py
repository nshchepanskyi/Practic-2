"""
main.py - Entry point for the GrandStay Hotel Management System.
"""

import sys
import os

# Add the current directory to sys.path to ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hotel_data import seed_data
from views.rooms import show_rooms_menu
from views.reservations import show_reservations_menu
from views.dashboard import show_dashboard_menu

def clear_console():
    # Only useful if running in a real terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    # Load some initial data
    seed_data()
    
    while True:
        print("\n" + "="*40)
        print("  GRANDSTAY HOTEL MANAGEMENT SYSTEM  ")
        print("="*40)
        print("1. Room Management")
        print("2. Reservations & Guests")
        print("3. Dashboard & Reports")
        print("0. Exit Application")
        
        choice = input("\nSelect a module: ")
        
        if choice == '1':
            show_rooms_menu()
        elif choice == '2':
            show_reservations_menu()
        elif choice == '3':
            show_dashboard_menu()
        elif choice == '0':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nApplication closed by user.")
        sys.exit(0)
