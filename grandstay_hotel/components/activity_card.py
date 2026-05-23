import flet as ft
from theme import get as C


def activity_card(
    name,
    room,
    status,
):
    return ft.Container(
        bgcolor=C("surface"),

        border_radius=18,

        padding=15,

        margin=5,

        content=ft.Row(
            [
                ft.CircleAvatar(
                    content=ft.Text(
                        name[0],
                    ),
                ),

                ft.Column(
                    [
                        ft.Text(
                            name,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Text(
                            room,
                            color=C("text_secondary"),
                        ),
                    ],

                    spacing=2,
                ),

                ft.Container(
                    padding=10,

                    border_radius=12,

                    bgcolor=ft.Colors.GREEN_50,

                    content=ft.Text(
                        status,
                        color=ft.Colors.GREEN_400,
                    ),
                ),
            ],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )