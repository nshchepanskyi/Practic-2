import json
import os

from datetime import datetime


STORAGE_DIR = "storage"

if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

ROOMS_FILE = os.path.join(STORAGE_DIR, "rooms.json")
GUESTS_FILE = os.path.join(STORAGE_DIR, "guests.json")
RESERVATIONS_FILE = os.path.join(STORAGE_DIR, "reservations.json")
SERVICES_FILE = os.path.join(STORAGE_DIR, "service_orders.json")


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
        status="Available",
    ):

        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = status


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

        self.timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

        self.status = "Pending"


SERVICES_CATALOG = [
    {"name": "Breakfast", "price": 10},
    {"name": "Laundry", "price": 15},
    {"name": "Spa", "price": 50},
    {"name": "Airport Transfer", "price": 25},
    {"name": "Gym", "price": 20},
    {"name": "Pool", "price": 15},
    {"name": "Parking", "price": 12},
    {"name": "Room Service", "price": 8},
    {"name": "Mini Bar", "price": 18},
    {"name": "Dry Cleaning", "price": 22},
    {"name": "Conference Room", "price": 100},
    {"name": "Movie Rental", "price": 12},
    {"name": "Bicycle Rental", "price": 30},
]


def create_default_rooms():

    if rooms:
        return

    rooms.extend(
        [
            Room("101", "Single", 50),
            Room("102", "Single", 50),
            Room("201", "Double", 80),
            Room("202", "Double", 80),
            Room("301", "Suite", 150),
        ]
    )

    save_rooms()






def save_rooms():

    data = []

    for room in rooms:

        data.append(
            {
                "room_number": room.room_number,
                "room_type": room.room_type,
                "price": room.price,
                "status": room.status,
            }
        )

    with open(ROOMS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_rooms():

    rooms.clear()

    if not os.path.exists(ROOMS_FILE):

        create_default_rooms()

        return

    with open(ROOMS_FILE, "r") as f:
        data = json.load(f)

    for item in data:

        rooms.append(
            Room(
                item["room_number"],
                item["room_type"],
                item["price"],
                item["status"],
            )
        )






def save_guests():

    data = []

    for guest in guests:

        data.append(
            {
                "guest_id": guest.guest_id,
                "name": guest.name,
                "phone": guest.phone,
                "email": guest.email,
            }
        )

    with open(GUESTS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_guests():

    guests.clear()

    if not os.path.exists(GUESTS_FILE):
        return

    with open(GUESTS_FILE, "r") as f:
        data = json.load(f)

    for item in data:

        guests.append(
            Guest(
                item["guest_id"],
                item["name"],
                item["phone"],
                item["email"],
            )
        )






def save_reservations():

    data = []

    for reservation in reservations:

        data.append(
            {
                "reservation_id": reservation.reservation_id,
                "guest_id": reservation.guest.guest_id,
                "room_number": reservation.room.room_number,
                "check_in": reservation.check_in,
                "check_out": reservation.check_out,
                "status": reservation.status,
            }
        )

    with open(RESERVATIONS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_reservations():

    reservations.clear()

    if not os.path.exists(RESERVATIONS_FILE):
        return

    with open(RESERVATIONS_FILE, "r") as f:
        data = json.load(f)

    for item in data:

        guest = next(
            (
                g
                for g in guests
                if g.guest_id == item["guest_id"]
            ),
            None,
        )

        room = next(
            (
                r
                for r in rooms
                if r.room_number == item["room_number"]
            ),
            None,
        )

        if guest and room:

            reservation = Reservation(
                item["reservation_id"],
                guest,
                room,
                item["check_in"],
                item["check_out"],
            )

            reservation.status = item["status"]

            reservations.append(reservation)






def add_room(
    number,
    room_type,
    price,
):

    room_exists = next(
        (
            r
            for r in rooms
            if r.room_number == number
        ),
        None,
    )

    if room_exists:
        return False

    rooms.append(
        Room(
            number,
            room_type,
            price,
        )
    )

    save_rooms()

    return True


def remove_room(number):

    rooms[:] = [
        r
        for r in rooms
        if r.room_number != number
    ]

    save_rooms()






def create_guest(
    name,
    phone,
    email,
):

    guest = Guest(
        f"G{len(guests) + 1}",
        name,
        phone,
        email,
    )

    guests.append(guest)

    save_guests()

    return guest






def create_reservation(
    guest,
    room_number,
    check_in,
    check_out,
):

    room = next(
        (
            r
            for r in rooms
            if r.room_number == room_number
        ),
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

    save_rooms()

    save_reservations()

    return True






def create_service_order(
    guest_id,
    service_name,
    service_price,
    quantity=1,
):

    guest = next(
        (
            g
            for g in guests
            if g.guest_id == guest_id
        ),
        None,
    )

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

    save_service_orders()

    return True, order


def update_service_order_status(
    order_id,
    new_status,
):

    order = next(
        (
            o
            for o in service_orders
            if o.order_id == order_id
        ),
        None,
    )

    if not order:
        return False

    order.status = new_status

    save_service_orders()

    return True






def save_service_orders():

    data = []

    for order in service_orders:

        data.append(
            {
                "order_id": order.order_id,
                "guest_id": order.guest.guest_id,
                "service_name": order.service_name,
                "service_price": order.service_price,
                "quantity": order.quantity,
                "total": order.total,
                "timestamp": order.timestamp,
                "status": order.status,
            }
        )

    with open(SERVICES_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_service_orders():

    service_orders.clear()

    if not os.path.exists(SERVICES_FILE):
        return

    with open(SERVICES_FILE, "r") as f:
        data = json.load(f)

    for item in data:

        guest = next(
            (
                g
                for g in guests
                if g.guest_id == item["guest_id"]
            ),
            None,
        )

        if not guest:
            continue

        order = ServiceOrder(
            item["order_id"],
            guest,
            item["service_name"],
            item["service_price"],
            item["quantity"],
        )

        order.total = item["total"]
        order.timestamp = item["timestamp"]
        order.status = item["status"]

        service_orders.append(order)






def calc_reservation_revenue():

    total = 0

    for reservation in reservations:

        try:

            nights = max(
                (
                    datetime.strptime(
                        reservation.check_out,
                        "%Y-%m-%d",
                    )

                    -

                    datetime.strptime(
                        reservation.check_in,
                        "%Y-%m-%d",
                    )

                ).days,

                1,
            )

        except Exception:

            nights = 1

        total += reservation.room.price * nights

    return total


def calc_service_revenue():

    total = 0

    for order in service_orders:

        total += order.total

    return total


def calc_total_revenue():

    return (
        calc_reservation_revenue()
        +
        calc_service_revenue()
    )


def get_occupancy_rate():

    if not rooms:
        return 0

    occupied = sum(
        1
        for room in rooms
        if room.status == "Occupied"
    )

    return round(
        occupied / len(rooms) * 100
    )


def get_services_summary():

    summary = {}

    for order in service_orders:

        if order.service_name not in summary:

            summary[order.service_name] = {
                "name": order.service_name,
                "count": 0,
                "revenue": 0,
            }

        summary[order.service_name]["count"] += order.quantity

        summary[order.service_name]["revenue"] += order.total

    return list(summary.values())






def load_all_data():

    load_rooms()

    load_guests()

    load_reservations()

    load_service_orders()