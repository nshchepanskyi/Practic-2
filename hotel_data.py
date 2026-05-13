from datetime import datetime

rooms = []
guests = []
reservations = []
services = []


class Room:
    def __init__(
        self,
        room_number,
        room_type,
        price_per_night,
    ):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
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
        self.expenses = []

    def add_expense(
        self,
        service_name,
        cost,
    ):
        self.expenses.append(
            {
                "service_name": service_name,
                "cost": cost,
                "date": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
            }
        )

    def get_total_expenses(self):
        return sum(
            item["cost"]
            for item in self.expenses
        )


class Reservation:
    def __init__(
        self,
        res_id,
        guest_id,
        room_number,
        check_in_date,
        check_out_date,
    ):
        self.res_id = res_id
        self.guest_id = guest_id
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = "Pending"


def seed_data():
    if rooms:
        return

    rooms.append(Room("101", "Single", 50))
    rooms.append(Room("102", "Single", 50))
    rooms.append(Room("201", "Double", 80))
    rooms.append(Room("202", "Double", 80))
    rooms.append(Room("301", "Suite", 150))

    services.extend(
        [
            {
                "name": "Breakfast",
                "price": 10,
            },

            {
                "name": "Laundry",
                "price": 15,
            },

            {
                "name": "Mini-bar",
                "price": 20,
            },

            {
                "name": "Spa",
                "price": 50,
            },
        ]
    )


# ---------------- ROOM MANAGEMENT ----------------

def add_room(
    room_number,
    room_type,
    price,
):
    if any(
        r.room_number == room_number
        for r in rooms
    ):
        return False, "Room already exists."

    rooms.append(
        Room(
            room_number,
            room_type,
            price,
        )
    )

    return True, "Room added successfully."


def remove_room(room_number):
    global rooms

    before = len(rooms)

    rooms = [
        r
        for r in rooms
        if r.room_number != room_number
    ]

    if len(rooms) < before:
        return True, "Room removed."

    return False, "Room not found."


def get_all_rooms():
    return rooms


def get_rooms_by_status(status):
    return [
        r
        for r in rooms
        if r.status == status
    ]


def update_room_status(
    room_number,
    status,
):
    for r in rooms:
        if r.room_number == room_number:
            r.status = status
            return True, "Status updated."

    return False, "Room not found."


# ---------------- GUEST MANAGEMENT ----------------

def add_guest(
    name,
    phone,
    email,
):
    guest_id = f"G{len(guests) + 101}"

    guest = Guest(
        guest_id,
        name,
        phone,
        email,
    )

    guests.append(guest)

    return guest


def get_guest_by_id(guest_id):
    return next(
        (
            g
            for g in guests
            if g.guest_id == guest_id
        ),
        None,
    )


def search_guests(query):
    query = query.lower()

    return [
        g
        for g in guests
        if query in g.name.lower()
        or query in g.email.lower()
        or query in g.phone
    ]


# ---------------- RESERVATIONS ----------------

def create_reservation(
    guest_id,
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
        return False, "Room not found."

    if room.status != "Available":
        return False, "Room unavailable."

    res_id = f"R{len(reservations) + 1001}"

    reservation = Reservation(
        res_id,
        guest_id,
        room_number,
        check_in,
        check_out,
    )

    reservations.append(reservation)

    return True, reservation


def check_in_guest(res_id):
    reservation = next(
        (
            r
            for r in reservations
            if r.res_id == res_id
        ),
        None,
    )

    if not reservation:
        return False, "Reservation not found."

    reservation.status = "Checked-In"

    update_room_status(
        reservation.room_number,
        "Occupied",
    )

    return True, "Guest checked in."


def check_out_guest(res_id):
    reservation = next(
        (
            r
            for r in reservations
            if r.res_id == res_id
        ),
        None,
    )

    if not reservation:
        return False, "Reservation not found."

    reservation.status = "Checked-Out"

    update_room_status(
        reservation.room_number,
        "Available",
    )

    return True, "Guest checked out."


# ---------------- SERVICES ----------------

def add_service_to_guest(
    guest_id,
    service_name,
):
    guest = get_guest_by_id(guest_id)

    if not guest:
        return False, "Guest not found."

    service = next(
        (
            s
            for s in services
            if s["name"] == service_name
        ),
        None,
    )

    if not service:
        return False, "Service not found."

    guest.add_expense(
        service["name"],
        service["price"],
    )

    return True, "Service added."


# ---------------- REPORTS ----------------

def get_revenue_report():
    room_revenue = 0

    for res in reservations:
        if res.status == "Checked-Out":
            room = next(
                (
                    r
                    for r in rooms
                    if r.room_number == res.room_number
                ),
                None,
            )

            if room:
                room_revenue += (
                    room.price_per_night
                )

    service_revenue = sum(
        g.get_total_expenses()
        for g in guests
    )

    return {
        "room_revenue": room_revenue,
        "service_revenue": service_revenue,
        "total": room_revenue
        + service_revenue,
    }