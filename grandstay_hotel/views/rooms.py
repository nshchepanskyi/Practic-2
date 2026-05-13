"""
views/rooms.py - Interaction logic for Room Management.
"""

from hotel_data import add_room, remove_room, get_all_rooms, get_rooms_by_status, update_room_status

def show_rooms_menu():
    while True:
        print("\n--- Room Management ---")
        print("1. Show All Rooms")
        print("2. Show Available Rooms")
        print("3. Show Occupied Rooms")
        print("4. Add New Room")
        print("5. Remove Room")
        print("6. Change Room Status")
        print("0. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            display_rooms(get_all_rooms())
        elif choice == '2':
            display_rooms(get_rooms_by_status("Available"))
        elif choice == '3':
            display_rooms(get_rooms_by_status("Occupied"))
        elif choice == '4':
            num = input("Room Number: ")
            rtype = input("Room Type (Single/Double/Suite): ")
            price = float(input("Price per Night: "))
            success, msg = add_room(num, rtype, price)
            print(msg)
        elif choice == '5':
            num = input("Enter Room Number to remove: ")
            success, msg = remove_room(num)
            print(msg)
        elif choice == '6':
            num = input("Room Number: ")
            status = input("New Status (Available/Occupied/Maintenance): ")
            success, msg = update_room_status(num, status)
            print(msg)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def display_rooms(room_list):
    if not room_list:
        print("No rooms to display.")
        return
    
    print(f"{'Room #':<10} {'Type':<15} {'Price':<10} {'Status':<15}")
    print("-" * 50)
    for r in room_list:
        print(f"{r.room_number:<10} {r.room_type:<15} ${r.price_per_night:<9} {r.status:<15}")
