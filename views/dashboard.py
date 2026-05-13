import flet as ft

from hotel_data import (
    rooms,
    guests,
    reservations,
)

from components.stat_card import stat_card
from components.room_card import room_card
from components.activity_card import activity_card


def dashboard_view(page):
    room_grid = ft.GridView(
        runs_count=4,
        spacing=10,
        run_spacing=10,
        expand=False,
        height=400,
    )

    for room in rooms:
        room_grid.controls.append(
            room_card(room)
        )

    activity = ft.Column()

    for reservation in reservations:
        activity.controls.append(
            activity_card(
                reservation.guest.name,
                f"Room {reservation.room.room_number}",
                reservation.status,
            )
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
                        "Occupancy",
                        f"{len(reservations)}%",
                        ft.Icons.HOTEL,
                        "#42C59A",
                    ),

                    stat_card(
                        "Revenue",
                        "$18,420",
                        ft.Icons.ATTACH_MONEY,
                        "#13294B",
                    ),

                    stat_card(
                        "Check-ins",
                        str(len(reservations)),
                        ft.Icons.LOGIN,
                        "#5B8DEF",
                    ),
                ],

                wrap=True,
            ),

            ft.Container(height=30),

            ft.Row(
                [
                    ft.Container(
                        expand=1,

                        bgcolor="white",

                        border_radius=20,

                        padding=20,

                        content=ft.Column(
                            [
                                ft.Text(
                                    "Room Status",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Container(height=20),

                                room_grid,
                            ]
                        ),
                    ),

                    ft.Container(
                        width=400,

                        bgcolor="white",

                        border_radius=20,

                        padding=20,

                        content=ft.Column(
                            [
                                ft.Text(
                                    "Today's Activity",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Container(height=20),

                                activity,
                            ]
                        ),
                    ),
                ],

                expand=True,
            ),
        ],

        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )