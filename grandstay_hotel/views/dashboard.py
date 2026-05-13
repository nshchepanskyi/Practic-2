"""
views/dashboard.py - Hotel Dashboard and Reports.
"""

from hotel_data import (
    get_revenue_report, get_all_rooms, get_rooms_by_status, 
    reservations, guests
)

def show_dashboard_menu():
    while True:
        print("\n--- Hotel Dashboard & Reports ---")
        print("1. Revenue Report")
        print("2. Occupancy Summary")
        print("3. Guest Activity Report")
        print("4. Quick Statistics")
        print("0. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            report = get_revenue_report()
            print("\n--- Revenue Report ---")
            print(f"Room Revenue:    ${report['room_revenue']:,.2f}")
            print(f"Service Revenue: ${report['service_revenue']:,.2f}")
            print(f"Total Revenue:   ${report['total']:,.2f}")
            
        elif choice == '2':
            total_rooms = len(get_all_rooms())
            avail = len(get_rooms_by_status("Available"))
            occ = len(get_rooms_by_status("Occupied"))
            maint = len(get_rooms_by_status("Maintenance"))
            
            print("\n--- Occupancy Summary ---")
            print(f"Total Rooms:  {total_rooms}")
            print(f"Available:    {avail}")
            print(f"Occupied:     {occ}")
            print(f"Maintenance:  {maint}")
            if total_rooms > 0:
                print(f"Occupancy Rate: {(occ/total_rooms)*100:.1f}%")
                
        elif choice == '3':
            print("\n--- Guest Activity Report ---")
            if not guests:
                print("No guest data.")
            else:
                for g in guests:
                    total_exp = g.get_total_expenses()
                    status = "Active" if any(res.guest_id == g.guest_id and res.status == "Checked-In" for res in reservations) else "Inactive"
                    print(f"Guest: {g.name:<15} | ID: {g.guest_id:<6} | Expenses: ${total_exp:<8,.2f} | Status: {status}")
                    
        elif choice == '4':
            print("\n--- Quick Statistics ---")
            print(f"Total Reservations: {len(reservations)}")
            print(f"Total Unique Guests: {len(guests)}")
            print(f"Active Check-ins: {len([r for r in reservations if r.status == 'Checked-In'])}")
            
        elif choice == '0':
            break
        else:
            print("Invalid choice.")
