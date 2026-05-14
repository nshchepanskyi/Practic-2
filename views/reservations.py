import flet as ft

from auth import validate_email

from hotel_data import (
    create_guest,
    create_reservation,
    reservations,
    rooms,
)


def reservations_view(page):

    guest_name = ft.TextField(
        label="Guest Name",
        width=250,
    )

    country_code = ft.Dropdown(
        width=120,
        label="Code",
        value="+380",
        options=[
            ft.dropdown.Option("+380"),
            ft.dropdown.Option("+1"),
            ft.dropdown.Option("+44"),
            ft.dropdown.Option("+49"),
            ft.dropdown.Option("+33"),
        ],
    )

    phone_number = ft.TextField(
        label="Phone Number",
        width=200,
    )

    guest_email = ft.TextField(
        label="Email",
        width=250,
    )

    room_number = ft.Dropdown(
        label="Available Rooms",
        width=250,
        options=[],
    )

    check_in = ft.TextField(
        label="Check In",
        read_only=True,
        width=200,
    )

    check_out = ft.TextField(
        label="Check Out",
        read_only=True,
        width=200,
    )

    message = ft.Text()

    # =====================================
    # DATE PICKERS
    # =====================================

    def set_check_in(e):

        if e.control.value:

            check_in.value = str(
                e.control.value.date()
            )

            page.update()

    def set_check_out(e):

        if e.control.value:

            check_out.value = str(
                e.control.value.date()
            )

            page.update()

    check_in_picker = ft.DatePicker(
        on_change=set_check_in,
    )

    check_out_picker = ft.DatePicker(
        on_change=set_check_out,
    )

    page.overlay.append(check_in_picker)
    page.overlay.append(check_out_picker)

    def open_check_in(e):

        check_in_picker.open = True

        page.update()

    def open_check_out(e):

        check_out_picker.open = True

        page.update()

    # =====================================
    # TABLE
    # =====================================

    reservation_table = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text("Reservation")
            ),

            ft.DataColumn(
                ft.Text("Guest")
            ),

            ft.DataColumn(
                ft.Text("Room")
            ),

            ft.DataColumn(
                ft.Text("Status")
            ),
        ],

        rows=[],
    )

    # =====================================
    # REFRESH ROOMS
    # =====================================

    def refresh_rooms():

        room_number.options = [
            ft.dropdown.Option(
                room.room_number
            )
            for room in rooms
            if room.status == "Available"
        ]

    # =====================================
    # REFRESH TABLE
    # =====================================

    def refresh():

        reservation_table.rows.clear()

        refresh_rooms()

        for reservation in reservations:

            reservation_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(
                                reservation.reservation_id
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                reservation.guest.name
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                reservation.room.room_number
                            )
                        ),

                        ft.DataCell(
                            ft.Container(
                                padding=8,

                                border_radius=12,

                                bgcolor="#13294B",

                                content=ft.Text(
                                    reservation.status,
                                    color="white",
                                ),
                            )
                        ),
                    ]
                )
            )

        page.update()

    # =====================================
    # CREATE RESERVATION
    # =====================================

    def create_click(e):

        if not guest_name.value:

            message.value = "Enter guest name"

            message.color = "red"

            page.update()

            return

        if not guest_email.value:

            message.value = "Enter email"

            message.color = "red"

            page.update()

            return

        if not validate_email(
            guest_email.value
        ):

            message.value = "Invalid email"

            message.color = "red"

            page.update()

            return

        if not room_number.value:

            message.value = "Select room"

            message.color = "red"

            page.update()

            return

        if not check_in.value:

            message.value = (
                "Select check in date"
            )

            message.color = "red"

            page.update()

            return

        if not check_out.value:

            message.value = (
                "Select check out date"
            )

            message.color = "red"

            page.update()

            return

        if check_out.value <= check_in.value:

            message.value = (
                "Check out must be later"
            )

            message.color = "red"

            page.update()

            return

        full_phone = (
            f"{country_code.value}"
            f"{phone_number.value}"
        )

        guest = create_guest(
            guest_name.value,
            full_phone,
            guest_email.value,
        )

        success = create_reservation(
            guest,
            room_number.value,
            check_in.value,
            check_out.value,
        )

        if success:

            message.value = (
                "Reservation created"
            )

            message.color = "green"

            guest_name.value = ""

            phone_number.value = ""

            guest_email.value = ""

            room_number.value = None

            check_in.value = ""

            check_out.value = ""

        else:

            message.value = (
                "Reservation failed"
            )

            message.color = "red"

        refresh()

    refresh()

    return ft.Column(
        [
            ft.Text(
                "Reservations",
                size=34,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Container(height=20),

            ft.Container(
                bgcolor="white",

                border_radius=20,

                padding=20,

                content=ft.Column(
                    [
                        ft.Text(
                            "Create Reservation",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        ft.Row(
                            [
                                guest_name,

                                country_code,

                                phone_number,

                                guest_email,
                            ],

                            wrap=True,
                        ),

                        ft.Container(height=15),

                        ft.Row(
                            [
                                room_number,

                                ft.Row(
                                    [
                                        check_in,

                                        ft.IconButton(
                                            icon=ft.Icons.CALENDAR_MONTH,
                                            on_click=open_check_in,
                                        ),
                                    ]
                                ),

                                ft.Row(
                                    [
                                        check_out,

                                        ft.IconButton(
                                            icon=ft.Icons.CALENDAR_MONTH,
                                            on_click=open_check_out,
                                        ),
                                    ]
                                ),

                                ft.ElevatedButton(
                                    "Create",

                                    icon=ft.Icons.ADD,

                                    height=50,

                                    on_click=create_click,
                                ),
                            ],

                            wrap=True,
                        ),

                        ft.Container(height=10),

                        message,
                    ]
                ),
            ),

            ft.Container(height=20),

            ft.Container(
                bgcolor="white",

                border_radius=20,

                padding=20,

                expand=True,

                content=ft.Column(
                    [
                        ft.Text(
                            "Reservation List",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        reservation_table,
                    ]
                ),
            ),
        ],

        scroll=ft.ScrollMode.AUTO,

        expand=True,
    )