from datetime import datetime

rooms = []
guests = []
reservations = []
service_orders = []


class Room:
    def __init__(
        self,
        room_number,
        room_type,
        price,
    ):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = "Available"


class Guest:
    def __init__(
        self,
        guest_id,
        name,
        phone,
        email,
    ):
        self.guest_id = guest_id
        self.name = name
        self.phone = phone
        self.email = email


class Reservation:
    def __init__(
        self,
        reservation_id,
        guest,
        room,
        check_in,
        check_out,
    ):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.status = "Pending"


class ServiceOrder:
    def __init__(
        self,
        order_id,
        guest,
        service_name,
        service_price,
        quantity,
    ):
        self.order_id = order_id
        self.guest = guest
        self.service_name = service_name
        self.service_price = service_price
        self.quantity = quantity
        self.total = service_price * quantity
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.status = "Pending"


SERVICES_CATALOG = [
    {"name": "Breakfast",         "price": 10},
    {"name": "Laundry",           "price": 15},
    {"name": "Spa",               "price": 50},
    {"name": "Airport Transfer",  "price": 25},
    {"name": "Room Cleaning",     "price": 20},
    {"name": "Mini Bar Restock",  "price": 30},
]


def seed_data():
    if rooms:
        return

    rooms.extend(
        [
            Room("101", "Single", 50),
            Room("102", "Single", 50),
            Room("103", "Single", 50),
            Room("201", "Double", 80),
            Room("202", "Double", 80),
            Room("301", "Suite",  150),
        ]
    )


def add_room(number, room_type, price):
    rooms.append(Room(number, room_type, price))


def remove_room(number):
    global rooms
    rooms = [r for r in rooms if r.room_number != number]


def create_guest(name, phone, email):
    guest = Guest(
        f"G{len(guests) + 1}",
        name,
        phone,
        email,
    )
    guests.append(guest)
    return guest


def create_reservation(guest, room_number, check_in, check_out):
    room = next(
        (r for r in rooms if r.room_number == room_number),
        None,
    )
    if not room:
        return False
    if room.status != "Available":
        return False

    reservation = Reservation(
        f"R{len(reservations) + 1}",
        guest,
        room,
        check_in,
        check_out,
    )
    reservations.append(reservation)
    room.status = "Occupied"
    return True


# ── Service Orders ────────────────────────────────────────────────────────────

def create_service_order(guest_id, service_name, service_price, quantity=1):
    """Persist a new service order linked to a guest."""
    guest = next((g for g in guests if g.guest_id == guest_id), None)
    if not guest:
        return False, "Guest not found"

    order = ServiceOrder(
        order_id=f"SO{len(service_orders) + 1}",
        guest=guest,
        service_name=service_name,
        service_price=service_price,
        quantity=quantity,
    )
    service_orders.append(order)
    return True, order


def update_service_order_status(order_id, new_status):
    order = next((o for o in service_orders if o.order_id == order_id), None)
    if not order:
        return False
    order.status = new_status
    return True


# ── Revenue / Report helpers ──────────────────────────────────────────────────

def calc_reservation_revenue():
    """
    Sum revenue from checked-out (completed) reservations.
    For reservations still Pending / Checked-In we use the nightly rate × 1
    as an estimate (real projects would use actual night count).
    """
    total = 0.0
    for r in reservations:
        try:
            nights = max(
                (
                    datetime.strptime(r.check_out, "%Y-%m-%d")
                    - datetime.strptime(r.check_in,  "%Y-%m-%d")
                ).days,
                1,
            )
        except Exception:
            nights = 1
        total += r.room.price * nights
    return total


def calc_service_revenue():
    """Sum of all service order totals."""
    return sum(o.total for o in service_orders)


def calc_total_revenue():
    return calc_reservation_revenue() + calc_service_revenue()


def get_occupancy_rate():
    if not rooms:
        return 0
    occupied = sum(1 for r in rooms if r.status == "Occupied")
    return round(occupied / len(rooms) * 100)


def get_services_summary():
    """Return list of {name, count, revenue} per service type."""
    summary = {}
    for o in service_orders:
        entry = summary.setdefault(
            o.service_name,
            {"name": o.service_name, "count": 0, "revenue": 0.0},
        )
        entry["count"]   += o.quantity
        entry["revenue"] += o.total
    return sorted(summary.values(), key=lambda x: x["revenue"], reverse=True)
