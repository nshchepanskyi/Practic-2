import flet as ft

from l10n import tr
from theme import get as C


ACTIVE_PAGE_INDEX = 0






def navbar(change_page, logout_callback):

    global ACTIVE_PAGE_INDEX

    nav_items = [

        {
            "title": tr("Dashboard"),
            "icon": ft.Icons.DASHBOARD,
        },

        {
            "title": tr("Rooms"),
            "icon": ft.Icons.HOTEL,
        },

        {
            "title": tr("Reservations"),
            "icon": ft.Icons.BOOK_ONLINE,
        },

        {
            "title": tr("Guests"),
            "icon": ft.Icons.PEOPLE,
        },

        {
            "title": tr("Services"),
            "icon": ft.Icons.ROOM_SERVICE,
        },
    ]

    buttons = []





    def update_active():

        for i, btn in enumerate(buttons):

            if i == ACTIVE_PAGE_INDEX:

                btn.bgcolor = C("primary")

                btn.content.controls[0].color = C("on_primary")

                btn.content.controls[1].color = C("on_primary")

            else:

                btn.bgcolor = ft.Colors.TRANSPARENT

                btn.content.controls[0].color = C("navbar_inactive")

                btn.content.controls[1].color = C("navbar_inactive")

        navbar_container.update()





    def navigate(index):

        global ACTIVE_PAGE_INDEX

        ACTIVE_PAGE_INDEX = index

        update_active()

        change_page(index)





    for index, item in enumerate(nav_items):

        btn = ft.Container(

            border_radius=14,

            padding=12,

            ink=True,

            on_click=lambda e, i=index:
            navigate(i),

            content=ft.Row(
                [
                    ft.Icon(
                        item["icon"],
                        size=22,
                    ),

                    ft.Text(
                        item["title"],
                        size=15,
                        weight=ft.FontWeight.W_500,
                    ),
                ],

                spacing=12,
            ),
        )

        buttons.append(btn)





    logout_button = ft.Container(

        border_radius=14,

        padding=12,

        bgcolor=ft.Colors.RED_500,

        ink=True,

        on_click=lambda e:
        logout_callback(),

        content=ft.Row(
            [
                ft.Icon(
                    ft.Icons.LOGOUT,

                    color=ft.Colors.WHITE,

                    size=22,
                ),

                ft.Text(
                    tr("Logout"),

                    color=C("on_primary"),

                    size=15,

                    weight=ft.FontWeight.BOLD,
                ),
            ],

            spacing=12,
        ),
    )





    navbar_container = ft.Container(

        width=260,

        bgcolor=C("surface"),

        padding=20,

        border=ft.Border(
            right=ft.BorderSide(
                1,
                C("divider"),
            )
        ),

        content=ft.Column(
            [
                ft.Text(
                    tr("GrandStay"),

                    size=28,

                    weight=ft.FontWeight.BOLD,

                    color=C("navbar_brand"),
                ),

                ft.Divider(
                    color=C("divider"),
                ),

                *buttons,

                ft.Container(expand=True),

                ft.Divider(
                    color=C("divider"),
                ),

                logout_button,
            ],

            spacing=10,
        ),
    )

    return navbar_container