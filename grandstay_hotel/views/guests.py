import flet as ft

from hotel_data import guests
from l10n import tr
from theme import get as C


def guests_view(page):
    guests_table = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text(tr("Guest ID"))
            ),

            ft.DataColumn(
                ft.Text(tr("Name"))
            ),

            ft.DataColumn(
                ft.Text(tr("Phone"))
            ),

            ft.DataColumn(
                ft.Text(tr("Email"))
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
                tr("Guests"),
                size=34,
                weight=ft.FontWeight.BOLD,
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
                            tr("Guest List"),
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