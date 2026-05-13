import flet as ft


PRIMARY = "#13294B"
ACTIVE = "#42C59A"


def navbar(change_page):
    selected_index = 0

    nav_items = []

    container = ft.Container()

    def update_active():
        for i, item in enumerate(nav_items):

            icon = item.content

            if i == selected_index:
                item.bgcolor = ACTIVE
                icon.color = "white"

            else:
                item.bgcolor = "transparent"
                icon.color = "#B8C7E0"

        try:
            container.update()

        except:
            pass

    def navigate(index):
        nonlocal selected_index

        selected_index = index

        update_active()

        change_page(index)

    def nav_button(icon_name, index):
        btn = ft.Container(
            width=60,
            height=60,

            border_radius=18,

            alignment=ft.Alignment(0, 0),

            animate=300,

            content=ft.Icon(
                icon_name,
                size=30,
                color="#B8C7E0",
            ),
        )

        btn.on_click = lambda e: navigate(index)

        nav_items.append(btn)

        return btn

    item_column = ft.Column(
        [
            ft.Container(
                width=55,
                height=55,

                bgcolor=ACTIVE,

                border_radius=18,

                alignment=ft.Alignment(0, 0),

                content=ft.Icon(
                    ft.Icons.HOTEL,
                    color="white",
                    size=28,
                ),
            ),

            ft.Container(height=40),

            nav_button(
                ft.Icons.DASHBOARD,
                0,
            ),

            nav_button(
                ft.Icons.MEETING_ROOM,
                1,
            ),

            nav_button(
                ft.Icons.BOOK,
                2,
            ),

            nav_button(
                ft.Icons.PEOPLE,
                3,
            ),

            nav_button(
                ft.Icons.ROOM_SERVICE,
                4,
            ),
        ],

        spacing=15,
    )

    container.content = item_column

    container.width = 100
    container.bgcolor = PRIMARY
    container.border_radius = 25
    container.padding = 20

    update_active()

    return container