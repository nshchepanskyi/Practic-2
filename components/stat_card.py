import flet as ft


def stat_card(
    title,
    value,
    icon,
    color,
):
    return ft.Container(
        width=250,
        height=150,

        bgcolor="white",

        border_radius=20,

        padding=20,

        shadow=ft.BoxShadow(
            blur_radius=20,
            color="#00000015",
        ),

        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            title,
                            size=16,
                            color="grey",
                        ),

                        ft.Container(
                            width=40,
                            height=40,

                            border_radius=12,

                            bgcolor=color,

                            alignment=ft.Alignment(0, 0),

                            content=ft.Icon(
                                icon,
                                color="white",
                            ),
                        ),
                    ],

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Container(height=20),

                ft.Text(
                    value,
                    size=32,
                    weight=ft.FontWeight.BOLD,
                ),
            ]
        ),
    )