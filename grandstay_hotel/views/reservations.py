import flet as ft

from auth import validate_email

from hotel_data import (
    create_guest,
    create_reservation,
    reservations,
    rooms,
)
from l10n import tr
from theme import get as C


def reservations_view(page):

    guest_name = ft.TextField(
        label=tr("Guest Name"),
        width=250,
    )

    COUNTRIES = [
        ("+380", "UA"),
        ("+1", "US"),
        ("+44", "UK"),
        ("+49", "DE"),
        ("+33", "FR"),
        ("+48", "PL"),
        ("+39", "IT"),
        ("+34", "ES"),
        ("+90", "TR"),
        ("+81", "JP"),
        ("+86", "CN"),
        ("+91", "IN"),
    ]

    country_code = ft.Dropdown(
        width=150,
        label=tr("Code"),
        value="+380",
        options=[
            ft.dropdown.Option(key=code, text=f"{cc} {code}")
            for code, cc in COUNTRIES
        ],
    )

    phone_number = ft.TextField(
        label=tr("Phone Number"),
        width=200,
    )

    guest_email = ft.TextField(
        label=tr("Email"),
        width=250,
    )

    room_number = ft.Dropdown(
        label=tr("Available Rooms"),
        width=250,
        options=[],
    )

    check_in = ft.TextField(
        label=tr("Check In"),
        read_only=True,
        width=200,
    )

    check_out = ft.TextField(
        label=tr("Check Out"),
        read_only=True,
        width=200,
    )

    message = ft.Text()

    # =====================================
    # DATE PICKERS
    # =====================================

    def _to_local_date(dt):
        if dt.tzinfo is not None:
            dt = dt.astimezone()
        return dt.strftime("%Y-%m-%d")

    def set_check_in(e):

        if e.control.value:

            check_in.value = _to_local_date(
                e.control.value
            )

            page.update()

    def set_check_out(e):

        if e.control.value:

            check_out.value = _to_local_date(
                e.control.value
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
                ft.Text(tr("Reservation"))
            ),

            ft.DataColumn(
                ft.Text(tr("Guest"))
            ),

            ft.DataColumn(
                ft.Text(tr("Room"))
            ),

            ft.DataColumn(
                ft.Text(tr("Status"))
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

                                bgcolor=ft.Colors.BLUE_GREY_900,

                                content=ft.Text(
                                    tr(reservation.status),
                                    color=ft.Colors.WHITE,
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

            message.value = tr("Enter guest name")

            message.color = "red"

            page.update()

            return

        if not guest_email.value:

            message.value = tr("Enter email")

            message.color = "red"

            page.update()

            return

        if not validate_email(
            guest_email.value
        ):

            message.value = tr("Invalid email")

            message.color = "red"

            page.update()

            return

        if not room_number.value:

            message.value = tr("Select room")

            message.color = "red"

            page.update()

            return

        if not check_in.value:

            message.value = tr(
                "Select check in date"
            )

            message.color = "red"

            page.update()

            return

        if not check_out.value:

            message.value = tr(
                "Select check out date"
            )

            message.color = "red"

            page.update()

            return

        if check_out.value <= check_in.value:

            message.value = tr(
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

            message.value = tr(
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

            message.value = tr(
                "Reservation failed"
            )

            message.color = "red"

        refresh()

    refresh()

    return ft.Column(
        [
                ft.Text(
                    tr("Reservations"),
                    size=34,
                    weight=ft.FontWeight.BOLD,
                ),

            ft.Container(height=20),

            ft.Container(
                bgcolor=C("surface"),

                border_radius=20,

                padding=20,

                content=ft.Column(
                    [
                        ft.Text(
                            tr("Create Reservation"),
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
                                    tr("Create"),

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
                bgcolor=C("surface"),

                border_radius=20,

                padding=20,

                expand=True,

                content=ft.Column(
                    [
                        ft.Text(
                            tr("Reservation List"),
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