"""
views/reservations.py - Interaction logic for Reservations and Guest Management.
"""

from hotel_data import (
    create_reservation, check_in_guest, check_out_guest, add_guest, 
    search_guests, reservations, get_guest_by_id, add_service_to_guest, services
)

def show_reservations_menu():
    while True:
        print("\n--- Reservations & Guests ---")
        print("1. Create New Reservation")
        print("2. Check-In Guest")
        print("3. Check-Out Guest")
        print("4. Add New Guest")
        print("5. Search Guest")
        print("6. Add Service to Guest")
        print("7. View All Reservations")
        print("0. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Guest Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            guest = add_guest(name, phone, email)
            
            room_num = input("Room Number: ")
            check_in = input("Check-in Date (YYYY-MM-DD): ")
            check_out = input("Check-out Date (YYYY-MM-DD): ")
            
            success, result = create_reservation(guest.guest_id, room_num, check_in, check_out)
            if success:
                print(f"Reservation created! ID: {result.res_id}")
            else:
                print(f"Error: {result}")
                
        elif choice == '2':
            res_id = input("Enter Reservation ID: ")
            success, msg = check_in_guest(res_id)
            print(msg)
            
        elif choice == '3':
            res_id = input("Enter Reservation ID: ")
            success, msg = check_out_guest(res_id)
            print(msg)
            
        elif choice == '4':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            guest = add_guest(name, phone, email)
            print(f"Guest added. ID: {guest.guest_id}")
            
        elif choice == '5':
            query = input("Search by name, email, or phone: ")
            found = search_guests(query)
            if found:
                for g in found:
                    print(f"ID: {g.guest_id} | Name: {g.name} | Email: {g.email}")
            else:
                print("No guests found.")
                
        elif choice == '6':
            g_id = input("Guest ID: ")
            print("Available Services:")
            for i, s in enumerate(services):
                print(f"{i+1}. {s['name']} (${s['price']})")
            s_choice = int(input("Select service #: ")) - 1
            if 0 <= s_choice < len(services):
                success, msg = add_service_to_guest(g_id, services[s_choice]['name'])
                print(msg)
            else:
                print("Invalid service choice.")
                
        elif choice == '7':
            display_reservations()
            
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def display_reservations():
    if not reservations:
        print("No reservations on record.")
        return
    
    print(f"{'Res ID':<10} {'Guest ID':<10} {'Room':<6} {'In':<12} {'Out':<12} {'Status':<12}")
    print("-" * 65)
    for r in reservations:
        print(f"{r.res_id:<10} {r.guest_id:<10} {r.room_number:<6} {r.check_in_date:<12} {r.check_out_date:<12} {r.status:<12}")
