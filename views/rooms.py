import flet as ft

from hotel_data import (
    add_room,
    get_all_rooms,
    remove_room,
)


def rooms_view(page: ft.Page):
    table = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text("Room")
            ),

            ft.DataColumn(
                ft.Text("Type")
            ),

            ft.DataColumn(
                ft.Text("Price")
            ),

            ft.DataColumn(
                ft.Text("Status")
            ),
        ],
        rows=[],
    )

    room_number = ft.TextField(
        label="Room Number"
    )

    room_type = ft.Dropdown(
        label="Room Type",
        options=[
            ft.dropdown.Option(
                "Single"
            ),

            ft.dropdown.Option(
                "Double"
            ),

            ft.dropdown.Option(
                "Suite"
            ),
        ],
    )

    room_price = ft.TextField(
        label="Price"
    )

    delete_room = ft.TextField(
        label="Delete Room"
    )

    def refresh():
        table.rows.clear()

        for r in get_all_rooms():
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(
                                r.room_number
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                r.room_type
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                f"${r.price_per_night}"
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                r.status
                            )
                        ),
                    ]
                )
            )

        page.update()

    def add_click(e):
        success, msg = add_room(
            room_number.value,
            room_type.value,
            float(
                room_price.value
            ),
        )

        page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )

        page.snack_bar.open = True

        refresh()

    def delete_click(e):
        success, msg = remove_room(
            delete_room.value
        )

        page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )

        page.snack_bar.open = True

        refresh()

    refresh()

    return ft.Column(
        [
            ft.Row(
                [
                    room_number,
                    room_type,
                    room_price,

                    ft.ElevatedButton(
                        "Add Room",
                        icon=ft.Icons.ADD,
                        on_click=add_click,
                    ),
                ]
            ),

            ft.Row(
                [
                    delete_room,

                    ft.ElevatedButton(
                        "Delete Room",
                        icon=ft.Icons.DELETE,
                        on_click=delete_click,
                    ),
                ]
            ),

            table,
        ]
    )