import flet as ft

from hotel_data import (
    rooms,
    reservations,
    add_room,
    remove_room,
)
from l10n import tr
from theme import get as C


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
        label=tr("Room Number"),
        width=200,
    )

    room_type = ft.Dropdown(
        label=tr("Room Type"),

        width=200,

        options=[
            ft.dropdown.Option(tr("Single")),
            ft.dropdown.Option(tr("Double")),
            ft.dropdown.Option(tr("Suite")),
        ],
    )

    room_price = ft.TextField(
        label=tr("Price"),
        width=200,
    )

    delete_room_field = ft.TextField(
        label=tr("Room Number"),
        width=200,
    )

    delete_message = ft.Text(
        size=13,
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
                                    color=ft.Colors.WHITE,
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
        number = delete_room_field.value.strip()

        if not number:

            delete_message.value = tr("Enter a room number")
            delete_message.color = "red"

            page.update()

            return

        room = next(
            (r for r in rooms if r.room_number == number),
            None,
        )

        if not room:

            delete_message.value = tr(
                "Room {number} not found", number=number
            )

            delete_message.color = "red"

            page.update()

            return

        has_reservation = any(
            r.room.room_number == number
            for r in reservations
        )

        if has_reservation or room.status != "Available":

            delete_message.value = tr(
                "Cannot delete room {number} — it has active reservations", number=number
            )

            delete_message.color = "red"

            page.update()

            return

        remove_room(number)

        delete_room_field.value = ""

        delete_message.value = tr(
            "Room {number} deleted", number=number
        )

        delete_message.color = "green"

        refresh()

    refresh()

    return ft.Column(
        [
                ft.Text(
                    tr("Rooms"),
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
                            tr("Add Room"),
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
                                    tr("Add Room"),
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
                bgcolor=C("surface"),

                border_radius=20,

                padding=20,

                content=ft.Column(
                    [
                        ft.Text(
                            tr("Delete Room"),
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        ft.Row(
                            [
                                delete_room_field,

                                ft.ElevatedButton(
                                    tr("Delete"),
                                    icon=ft.Icons.DELETE,
                                    bgcolor=ft.Colors.RED_600,
                                    color=ft.Colors.WHITE,
                                    height=50,
                                    on_click=delete_click,
                                ),
                            ]
                        ),

                        delete_message,
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
                            tr("Room List"),
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