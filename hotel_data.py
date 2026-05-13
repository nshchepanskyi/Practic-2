"""
hotel_data.py - Core data storage and business logic for GrandStay Hotel Management.
Contains classes and global data structures.
"""

from datetime import datetime

# --- Data Structures ---
# In a real app, these would be loaded from a database.
# For now, we use lists to store instances.

rooms = []
guests = []
reservations = []
services = [] # List of available services {name: str, price: float}

# --- Classes ---

class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type # e.g., 'Single', 'Double', 'Suite'
        self.price_per_night = price_per_night
        self.status = "Available" # Available, Occupied, Maintenance

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "room_type": self.room_type,
            "price_per_night": self.price_per_night,
            "status": self.status
        }

class Guest:
    def __init__(self, guest_id, name, phone, email):
        self.guest_id = guest_id
        self.name = name
        self.phone = phone
        self.email = email
        self.expenses = [] # List of {service_name: str, cost: float, date: str}

    def add_expense(self, service_name, cost):
        self.expenses.append({
            "service_name": service_name,
            "cost": cost,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_total_expenses(self):
        return sum(item['cost'] for item in self.expenses)

class Reservation:
    def __init__(self, res_id, guest_id, room_number, check_in_date, check_out_date):
        self.res_id = res_id
        self.guest_id = guest_id
        self.room_number = room_number
        self.check_in_date = check_in_date # Format: YYYY-MM-DD
        self.check_out_date = check_out_date # Format: YYYY-MM-DD
        self.status = "Pending" # Pending, Checked-In, Checked-Out, Canceled

# --- Seed Initial Data ---
def seed_data():
    # Initial Rooms
    rooms.append(Room("101", "Single", 50.0))
    rooms.append(Room("102", "Single", 50.0))
    rooms.append(Room("201", "Double", 80.0))
    rooms.append(Room("202", "Double", 80.0))
    rooms.append(Room("301", "Suite", 150.0))
    
    # Initial Services
    services.extend([
        {"name": "Breakfast", "price": 10.0},
        {"name": "Laundry", "price": 15.0},
        {"name": "Mini-bar", "price": 20.0},
        {"name": "Spa", "price": 50.0}
    ])

# --- Logic Functions ---

# Room Management
def add_room(room_number, room_type, price):
    if any(r.room_number == room_number for r in rooms):
        return False, f"Room {room_number} already exists."
    new_room = Room(room_number, room_type, price)
    rooms.append(new_room)
    return True, f"Room {room_number} added successfully."

def remove_room(room_number):
    global rooms
    initial_count = len(rooms)
    rooms = [r for r in rooms if r.room_number != room_number]
    if len(rooms) < initial_count:
        return True, f"Room {room_number} removed."
    return False, f"Room {room_number} not found."

def get_all_rooms():
    return rooms

def get_rooms_by_status(status):
    return [r for r in rooms if r.status == status]

def update_room_status(room_number, status):
    for r in rooms:
        if r.room_number == room_number:
            r.status = status
            return True, f"Room {room_number} status updated to {status}."
    return False, "Room not found."

# Guest Management
def add_guest(name, phone, email):
    guest_id = f"G{len(guests) + 101}"
    new_guest = Guest(guest_id, name, phone, email)
    guests.append(new_guest)
    return new_guest

def get_guest_by_id(guest_id):
    return next((g for g in guests if g.guest_id == guest_id), None)

def search_guests(query):
    query = query.lower()
    return [g for g in guests if query in g.name.lower() or query in g.email.lower() or query in g.phone]

# Reservation Logic
def create_reservation(guest_id, room_number, check_in, check_out):
    # Check for double booking (simplified: check if room is available)
    room = next((r for r in rooms if r.room_number == room_number), None)
    if not room:
        return False, "Room not found."
    if room.status != "Available":
        return False, f"Room {room_number} is currently {room.status}."
    
    res_id = f"R{len(reservations) + 1001}"
    new_res = Reservation(res_id, guest_id, room_number, check_in, check_out)
    reservations.append(new_res)
    return True, new_res

def check_in_guest(res_id):
    res = next((r for r in reservations if r.res_id == res_id), None)
    if not res:
        return False, "Reservation not found."
    if res.status != "Pending":
        return False, f"Reservation is already {res.status}."
    
    res.status = "Checked-In"
    update_room_status(res.room_number, "Occupied")
    return True, f"Guest checked into room {res.room_number}."

def check_out_guest(res_id):
    res = next((r for r in reservations if r.res_id == res_id), None)
    if not res:
        return False, "Reservation not found."
    if res.status != "Checked-In":
        return False, "Guest is not checked in."
    
    res.status = "Checked-Out"
    update_room_status(res.room_number, "Available")
    return True, f"Guest checked out from room {res.room_number}."

# Service Accounting
def add_service_to_guest(guest_id, service_name):
    guest = get_guest_by_id(guest_id)
    if not guest:
        return False, "Guest not found."
    
    service = next((s for s in services if s['name'] == service_name), None)
    if not service:
        return False, "Service not found."
    
    guest.add_expense(service['name'], service['price'])
    return True, f"Added {service_name} (${service['price']}) to {guest.name}."

# Reports
def get_revenue_report():
    total_room_revenue = 0
    # Simple calculation: Room price * nights for Checked-Out reservations
    for res in reservations:
        if res.status == "Checked-Out":
            room = next((r for r in rooms if r.room_number == res.room_number), None)
            if room:
                # Mock nights = 2 if check_in/out same for simplicity in this demo logic
                # Real apps would diff the dates
                total_room_revenue += room.price_per_night * 1 
    
    total_service_revenue = sum(g.get_total_expenses() for g in guests)
    
    return {
        "room_revenue": total_room_revenue,
        "service_revenue": total_service_revenue,
        "total": total_room_revenue + total_service_revenue
    }
