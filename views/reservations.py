import flet as ft

from hotel_data import (
    create_guest,
    create_reservation,
    reservations,
)


def reservations_view(page):
    guest_name = ft.TextField(
        label="Guest Name"
    )

    guest_phone = ft.TextField(
        label="Phone"
    )

    guest_email = ft.TextField(
        label="Email"
    )

    room_number = ft.TextField(
        label="Room Number"
    )

    check_in = ft.TextField(
        label="Check In"
    )

    check_out = ft.TextField(
        label="Check Out"
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
                            ft.Text(
                                reservation.status
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

            ft.Row(
                [
                    guest_name,
                    guest_phone,
                    guest_email,
                ]
            ),

            ft.Row(
                [
                    room_number,
                    check_in,
                    check_out,

                    ft.ElevatedButton(
                        "Create Reservation",
                        on_click=create_click,
                    ),
                ]
            ),

            reservation_table,
        ],

        scroll=ft.ScrollMode.AUTO,
    )