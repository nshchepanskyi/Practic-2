import flet as ft


def topbar():
    return ft.Container(
        padding=10,

        content=ft.Row(
            [
                ft.Text(
                    "Hotel Management Dashboard",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_GREY_900,
                ),

                ft.Row(
                    [
                        ft.TextField(
                            hint_text="Search...",

                            width=250,

                            border_radius=15,

                            prefix_icon=ft.Icons.SEARCH,

                            bgcolor=ft.Colors.WHITE,
                        ),

                        ft.IconButton(
                            icon=ft.Icons.NOTIFICATIONS,

                            icon_color=ft.Colors.BLUE_GREY_900,
                        ),

                        ft.CircleAvatar(
                            bgcolor=ft.Colors.BLUE_900,

                            content=ft.Text(
                                "A",
                                color=ft.Colors.WHITE,
                            ),
                        ),
                    ]
                ),
            ],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )