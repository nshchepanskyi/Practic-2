import flet as ft


PRIMARY = "#13294B"


def sidebar(change_page):
    def nav(index):
        change_page(index)

    return ft.Container(
        width=90,

        bgcolor=PRIMARY,

        border_radius=20,

        padding=20,

        content=ft.Column(
            [
                ft.Container(
                    width=50,
                    height=50,

                    border_radius=15,

                    bgcolor="#42C59A",

                    alignment=ft.Alignment(0, 0),

                    content=ft.Icon(
                        ft.Icons.HOTEL,
                        color="white",
                    ),
                ),

                ft.Container(height=30),

                ft.IconButton(
                    icon=ft.Icons.DASHBOARD,

                    icon_color="white",

                    icon_size=30,

                    on_click=lambda e: nav(0),
                ),

                ft.IconButton(
                    icon=ft.Icons.MEETING_ROOM,

                    icon_color="white",

                    icon_size=30,

                    on_click=lambda e: nav(1),
                ),

                ft.IconButton(
                    icon=ft.Icons.BOOK,

                    icon_color="white",

                    icon_size=30,

                    on_click=lambda e: nav(2),
                ),
            ]
        ),
    )