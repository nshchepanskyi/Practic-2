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

    room_number = ft.TextField(
        label="Room Number",
        width=200,
    )

    room_type = ft.Dropdown(
        label="Room Type",

        width=200,

        options=[
            ft.dropdown.Option("Single"),
            ft.dropdown.Option("Double"),
            ft.dropdown.Option("Suite"),
        ],
    )

    room_price = ft.TextField(
        label="Price",
        width=200,
    )

    delete_room_field = ft.TextField(
        label="Delete Room",
        width=200,
    )

    def refresh():
        table.rows.clear()

        for room in rooms:
            status_color = (
                "green"
                if room.status == "Available"
                else "blue"
            )

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
                            ft.Container(
                                padding=8,

                                border_radius=12,

                                bgcolor=status_color,

                                content=ft.Text(
                                    room.status,
                                    color="white",
                                ),
                            )
                        ),
                    ]
                )
            )

        page.update()

    def add_click(e):
        add_room(
            room_number.value,
            room_type.value,
            float(room_price.value),
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

            ft.Container(height=20),

            ft.Container(
                bgcolor="white",

                border_radius=20,

                padding=20,

                content=ft.Column(
                    [
                        ft.Text(
                            "Add Room",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        ft.Row(
                            [
                                room_number,
                                room_type,
                                room_price,

                                ft.ElevatedButton(
                                    "Add Room",
                                    icon=ft.Icons.ADD,
                                    height=50,
                                    on_click=add_click,
                                ),
                            ]
                        ),
                    ]
                ),
            ),

            ft.Container(height=20),

            ft.Container(
                bgcolor="white",

                border_radius=20,

                padding=20,

                content=ft.Column(
                    [
                        ft.Text(
                            "Delete Room",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        ft.Row(
                            [
                                delete_room_field,

                                ft.ElevatedButton(
                                    "Delete",
                                    icon=ft.Icons.DELETE,
                                    bgcolor="red",
                                    color="white",
                                    height=50,
                                    on_click=delete_click,
                                ),
                            ]
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
                            "Room List",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        table,
                    ]
                ),
            ),
        ],

        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )