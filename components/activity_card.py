import flet as ft


def activity_card(
    name,
    room,
    status,
):
    return ft.Container(
        bgcolor="white",

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
                            color="grey",
                        ),
                    ],

                    spacing=2,
                ),

                ft.Container(
                    padding=10,

                    border_radius=12,

                    bgcolor="#E8FFF4",

                    content=ft.Text(
                        status,
                        color="#42C59A",
                    ),
                ),
            ],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )