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
                ),

                ft.Row(
                    [
                        ft.TextField(
                            hint_text="Search...",
                            width=250,
                            border_radius=15,
                            prefix_icon=ft.Icons.SEARCH,
                        ),

                        ft.IconButton(
                            icon=ft.Icons.NOTIFICATIONS,
                        ),

                        ft.CircleAvatar(
                            content=ft.Text("A"),
                        ),
                    ]
                ),
            ],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )