from datetime import datetime

rooms = []
guests = []
reservations = []


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

            Room("301", "Suite", 150),
        ]
    )


def add_room(
    number,
    room_type,
    price,
):
    room = Room(
        number,
        room_type,
        price,
    )

    rooms.append(room)


def remove_room(number):
    global rooms

    rooms = [
        r
        for r in rooms
        if r.room_number != number
    ]


def create_guest(
    name,
    phone,
    email,
):
    guest = Guest(
        f"G{len(guests)+1}",
        name,
        phone,
        email,
    )

    guests.append(guest)

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
        f"R{len(reservations)+1}",
        guest,
        room,
        check_in,
        check_out,
    )

    reservations.append(reservation)

    room.status = "Occupied"

    return True