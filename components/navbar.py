import flet as ft


ACTIVE_PAGE_INDEX = 0


# =====================================
# NAVBAR
# =====================================

def navbar(change_page, logout_callback):

    global ACTIVE_PAGE_INDEX

    nav_items = [

        {
            "title": "Dashboard",
            "icon": ft.Icons.DASHBOARD,
        },

        {
            "title": "Rooms",
            "icon": ft.Icons.HOTEL,
        },

        {
            "title": "Reservations",
            "icon": ft.Icons.BOOK_ONLINE,
        },

        {
            "title": "Guests",
            "icon": ft.Icons.PEOPLE,
        },

        {
            "title": "Services",
            "icon": ft.Icons.ROOM_SERVICE,
        },
    ]

    buttons = []

    # =====================================
    # UPDATE ACTIVE
    # =====================================

    def update_active():

        for i, btn in enumerate(buttons):

            if i == ACTIVE_PAGE_INDEX:

                btn.bgcolor = ft.Colors.BLUE_600

                btn.content.controls[0].color = ft.Colors.WHITE

                btn.content.controls[1].color = ft.Colors.WHITE

            else:

                btn.bgcolor = ft.Colors.TRANSPARENT

                btn.content.controls[0].color = ft.Colors.BLUE_GREY_700

                btn.content.controls[1].color = ft.Colors.BLUE_GREY_700

        navbar_container.update()

    # =====================================
    # NAVIGATION
    # =====================================

    def navigate(index):

        global ACTIVE_PAGE_INDEX

        ACTIVE_PAGE_INDEX = index

        update_active()

        change_page(index)

    # =====================================
    # NAV BUTTONS
    # =====================================

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

    # =====================================
    # LOGOUT BUTTON
    # =====================================

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
                    "Logout",

                    color=ft.Colors.WHITE,

                    size=15,

                    weight=ft.FontWeight.BOLD,
                ),
            ],

            spacing=12,
        ),
    )

    # =====================================
    # NAVBAR CONTAINER
    # =====================================

    navbar_container = ft.Container(

        width=260,

        bgcolor=ft.Colors.WHITE,

        padding=20,

        border=ft.Border(
            right=ft.BorderSide(
                1,
                ft.Colors.BLUE_GREY_100,
            )
        ),

        content=ft.Column(
            [
                ft.Text(
                    "GrandStay",

                    size=28,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.BLUE_700,
                ),

                ft.Divider(
                    color=ft.Colors.BLUE_GREY_100,
                ),

                *buttons,

                ft.Container(expand=True),

                ft.Divider(
                    color=ft.Colors.BLUE_GREY_100,
                ),

                logout_button,
            ],

            spacing=10,
        ),
    )

    return navbar_container