import flet as ft

from hotel_data import (
    add_guest,
    create_reservation,
    reservations,
    check_in_guest,
    check_out_guest,
    search_guests,
)


def reservations_view(
    page: ft.Page,
):
    table = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text(
                    "Reservation ID"
                )
            ),

            ft.DataColumn(
                ft.Text("Guest ID")
            ),

            ft.DataColumn(
                ft.Text("Room")
            ),

            ft.DataColumn(
                ft.Text("Check In")
            ),

            ft.DataColumn(
                ft.Text("Check Out")
            ),

            ft.DataColumn(
                ft.Text("Status")
            ),
        ],
        rows=[],
    )

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
        label="Check In YYYY-MM-DD"
    )

    check_out = ft.TextField(
        label="Check Out YYYY-MM-DD"
    )

    reservation_id = ft.TextField(
        label="Reservation ID"
    )

    search_field = ft.TextField(
        label="Search Guest"
    )

    search_results = ft.Column()

    def refresh():
        table.rows.clear()

        for r in reservations:
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(r.res_id)
                        ),

                        ft.DataCell(
                            ft.Text(
                                r.guest_id
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                r.room_number
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                r.check_in_date
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                r.check_out_date
                            )
                        ),

                        ft.DataCell(
                            ft.Text(r.status)
                        ),
                    ]
                )
            )

        page.update()

    def create_click(e):
        guest = add_guest(
            guest_name.value,
            guest_phone.value,
            guest_email.value,
        )

        success, result = create_reservation(
            guest.guest_id,
            room_number.value,
            check_in.value,
            check_out.value,
        )

        if success:
            message = (
                f"Reservation "
                f"{result.res_id} "
                f"created."
            )

        else:
            message = result

        page.snack_bar = ft.SnackBar(
            ft.Text(message)
        )

        page.snack_bar.open = True

        refresh()

    def check_in_click(e):
        success, msg = check_in_guest(
            reservation_id.value
        )

        page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )

        page.snack_bar.open = True

        refresh()

    def check_out_click(e):
        success, msg = check_out_guest(
            reservation_id.value
        )

        page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )

        page.snack_bar.open = True

        refresh()

    def search_click(e):
        search_results.controls.clear()

        found = search_guests(
            search_field.value
        )

        if not found:
            search_results.controls.append(
                ft.Text(
                    "No guests found"
                )
            )

        for guest in found:
            search_results.controls.append(
                ft.Card(
                    content=ft.Container(
                        padding=15,
                        content=ft.Column(
                            [
                                ft.Text(
                                    guest.name,
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Text(
                                    f"ID: "
                                    f"{guest.guest_id}"
                                ),

                                ft.Text(
                                    guest.email
                                ),

                                ft.Text(
                                    guest.phone
                                ),
                            ]
                        ),
                    )
                )
            )

        page.update()

    refresh()

    return ft.Column(
        [
            ft.Text(
                "Create Reservation",
                size=20,
            ),

            guest_name,
            guest_phone,
            guest_email,

            room_number,
            check_in,
            check_out,

            ft.ElevatedButton(
                "Create Reservation",
                icon=ft.Icons.ADD,
                on_click=create_click,
            ),

            ft.Divider(),

            reservation_id,

            ft.Row(
                [
                    ft.ElevatedButton(
                        "Check In",
                        icon=ft.Icons.LOGIN,
                        on_click=check_in_click,
                    ),

                    ft.ElevatedButton(
                        "Check Out",
                        icon=ft.Icons.LOGOUT,
                        on_click=check_out_click,
                    ),
                ]
            ),

            ft.Divider(),

            ft.Text(
                "Search Guests",
                size=20,
            ),

            ft.Row(
                [
                    search_field,

                    ft.ElevatedButton(
                        "Search",
                        icon=ft.Icons.SEARCH,
                        on_click=search_click,
                    ),
                ]
            ),

            search_results,

            ft.Divider(),

            table,
        ]
    )