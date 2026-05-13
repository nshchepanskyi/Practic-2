import flet as ft


def stat_card(
    title,
    value,
    icon,
    color,
):
    return ft.Container(
        width=260,
        height=160,

        bgcolor=ft.Colors.WHITE,

        border_radius=22,

        padding=20,

        shadow=ft.BoxShadow(
            blur_radius=25,
            color=ft.Colors.BLACK12,
        ),

        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            title,
                            size=16,
                            color=ft.Colors.GREY_600,
                        ),

                        ft.Container(
                            width=45,
                            height=45,

                            border_radius=14,

                            bgcolor=color,

                            alignment=ft.Alignment(0, 0),

                            content=ft.Icon(
                                icon,
                                color=ft.Colors.WHITE,
                            ),
                        ),
                    ],

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Container(height=25),

                ft.Text(
                    value,
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_GREY_900,
                ),
            ]
        ),
    )