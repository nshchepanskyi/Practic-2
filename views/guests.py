import flet as ft

from hotel_data import guests


def guests_view(page):
    guests_table = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text("Guest ID")
            ),

            ft.DataColumn(
                ft.Text("Name")
            ),

            ft.DataColumn(
                ft.Text("Phone")
            ),

            ft.DataColumn(
                ft.Text("Email")
            ),
        ],

        rows=[],
    )

    def refresh():
        guests_table.rows.clear()

        for guest in guests:
            guests_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(
                                guest.guest_id
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                guest.name
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                guest.phone
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                guest.email
                            )
                        ),
                    ]
                )
            )

        page.update()

    refresh()

    return ft.Column(
        [
            ft.Text(
                "Guests",
                size=34,
                weight=ft.FontWeight.BOLD,
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
                            "Guest List",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        guests_table,
                    ]
                ),
            ),
        ],

        expand=True,
    )