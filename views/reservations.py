import flet as ft

from hotel_data import (
    create_guest,
    create_reservation,
    reservations,
)


def reservations_view(page):
    guest_name = ft.TextField(
        label="Guest Name",
        width=250,
    )

    guest_phone = ft.TextField(
        label="Phone",
        width=250,
    )

    guest_email = ft.TextField(
        label="Email",
        width=250,
    )

    room_number = ft.TextField(
        label="Room Number",
        width=250,
    )

    check_in = ft.TextField(
        label="Check In",
        width=250,
    )

    check_out = ft.TextField(
        label="Check Out",
        width=250,
    )

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

    def refresh():
        reservation_table.rows.clear()

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

    def create_click(e):
        guest = create_guest(
            guest_name.value,
            guest_phone.value,
            guest_email.value,
        )

        create_reservation(
            guest,
            room_number.value,
            check_in.value,
            check_out.value,
        )

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
                                guest_phone,
                                guest_email,
                            ],

                            wrap=True,
                        ),

                        ft.Container(height=15),

                        ft.Row(
                            [
                                room_number,
                                check_in,
                                check_out,

                                ft.ElevatedButton(
                                    "Create",
                                    icon=ft.Icons.ADD,
                                    height=50,
                                    on_click=create_click,
                                ),
                            ],

                            wrap=True,
                        ),
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