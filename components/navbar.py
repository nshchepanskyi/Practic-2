import flet as ft


PRIMARY = "#13294B"


def navbar(change_page):
    def nav(index):
        change_page(index)

    return ft.Container(
        width=100,

        bgcolor=PRIMARY,

        border_radius=25,

        padding=20,

        content=ft.Column(
            [
                ft.Container(
                    width=55,
                    height=55,

                    bgcolor="#42C59A",

                    border_radius=18,

                    alignment=ft.Alignment(0, 0),

                    content=ft.Icon(
                        ft.Icons.HOTEL,
                        color="white",
                        size=28,
                    ),
                ),

                ft.Container(height=40),

                ft.IconButton(
                    icon=ft.Icons.DASHBOARD,

                    icon_color="white",

                    icon_size=32,

                    on_click=lambda e: nav(0),
                ),

                ft.IconButton(
                    icon=ft.Icons.MEETING_ROOM,

                    icon_color="white",

                    icon_size=32,

                    on_click=lambda e: nav(1),
                ),

                ft.IconButton(
                    icon=ft.Icons.BOOK,

                    icon_color="white",

                    icon_size=32,

                    on_click=lambda e: nav(2),
                ),

                ft.IconButton(
                    icon=ft.Icons.PEOPLE,

                    icon_color="white",

                    icon_size=32,

                    on_click=lambda e: nav(3),
                ),

                ft.IconButton(
                    icon=ft.Icons.ROOM_SERVICE,

                    icon_color="white",

                    icon_size=32,

                    on_click=lambda e: nav(4),
                ),
            ]
        ),
    )