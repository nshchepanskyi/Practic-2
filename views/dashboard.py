import flet as ft

from hotel_data import (
    rooms,
    reservations,
    guests,
)

from components.stat_card import stat_card
from components.room_card import room_card


def dashboard_view(page):
    room_grid = ft.GridView(
        runs_count=5,
        spacing=15,
        run_spacing=15,
        height=300,
    )

    for room in rooms:
        room_grid.controls.append(
            room_card(room)
        )

    return ft.Column(
        [
            ft.Text(
                "Overview",
                size=34,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Container(height=20),

            ft.Row(
                [
                    stat_card(
                        "Revenue",
                        "$18,420",
                        ft.Icons.ATTACH_MONEY,
                        "#42C59A",
                    ),

                    stat_card(
                        "Reservations",
                        str(len(reservations)),
                        ft.Icons.BOOK,
                        "#13294B",
                    ),

                    stat_card(
                        "Guests",
                        str(len(guests)),
                        ft.Icons.PEOPLE,
                        "#5B8DEF",
                    ),

                    stat_card(
                        "Rooms",
                        str(len(rooms)),
                        ft.Icons.HOTEL,
                        "#F5A623",
                    ),
                ],

                wrap=True,
            ),

            ft.Container(height=30),

            ft.Container(
                bgcolor="white",

                border_radius=25,

                padding=25,

                content=ft.Column(
                    [
                        ft.Text(
                            "Room Status",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Container(height=20),

                        room_grid,
                    ]
                ),
            ),
        ],

        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )