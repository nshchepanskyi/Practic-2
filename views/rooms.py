import flet as ft

from hotel_data import (
    rooms,
    add_room,
    remove_room,
)


def rooms_view(page):
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Room")),
            ft.DataColumn(ft.Text("Type")),
            ft.DataColumn(ft.Text("Price")),
            ft.DataColumn(ft.Text("Status")),
        ],

        rows=[],
    )

    number = ft.TextField(
        label="Room Number"
    )

    room_type = ft.Dropdown(
        label="Room Type",

        options=[
            ft.dropdown.Option("Single"),
            ft.dropdown.Option("Double"),
            ft.dropdown.Option("Suite"),
        ],
    )

    price = ft.TextField(
        label="Price"
    )

    delete_room_field = ft.TextField(
        label="Delete Room"
    )

    def refresh():
        table.rows.clear()

        for room in rooms:
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(
                                room.room_number
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                room.room_type
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                f"${room.price}"
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                room.status
                            )
                        ),
                    ]
                )
            )

        page.update()

    def add_click(e):
        add_room(
            number.value,
            room_type.value,
            float(price.value),
        )

        refresh()

    def delete_click(e):
        remove_room(
            delete_room_field.value
        )

        refresh()

    refresh()

    return ft.Column(
        [
            ft.Text(
                "Rooms",
                size=34,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Row(
                [
                    number,
                    room_type,
                    price,

                    ft.ElevatedButton(
                        "Add Room",
                        on_click=add_click,
                    ),
                ]
            ),

            ft.Row(
                [
                    delete_room_field,

                    ft.ElevatedButton(
                        "Delete",
                        on_click=delete_click,
                    ),
                ]
            ),

            table,
        ],

        scroll=ft.ScrollMode.AUTO,
    )