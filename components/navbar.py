# components/navbar.py

import flet as ft

from datetime import datetime


PRIMARY = ft.Colors.BLUE_600
PRIMARY_LIGHT = ft.Colors.BLUE_50

TEXT_PRIMARY = ft.Colors.BLUE_GREY_900
TEXT_SECONDARY = ft.Colors.BLUE_GREY_500

BORDER = ft.Colors.BLUE_GREY_100

HOVER = ft.Colors.BLUE_GREY_50


# =====================================
# GLOBAL ACTIVE PAGE
# =====================================

ACTIVE_PAGE_INDEX = 0


def navbar(
    change_page,
):

    global ACTIVE_PAGE_INDEX

    nav_items = []

    nav_data = [
        (ft.Icons.DASHBOARD_OUTLINED, "Dashboard"),
        (ft.Icons.MEETING_ROOM_OUTLINED, "Rooms"),
        (ft.Icons.BOOK_OUTLINED, "Reservations"),
        (ft.Icons.PEOPLE_OUTLINED, "Guests"),
        (ft.Icons.ROOM_SERVICE_OUTLINED, "Services"),
    ]

    # =====================================
    # UPDATE ACTIVE
    # =====================================

    def update_active():

        global ACTIVE_PAGE_INDEX

        for i, item in enumerate(nav_items):

            row = item.content

            icon_control = row.controls[0]

            text_control = row.controls[1]

            # ACTIVE
            if i == ACTIVE_PAGE_INDEX:

                item.bgcolor = PRIMARY_LIGHT

                icon_control.color = PRIMARY

                text_control.color = PRIMARY

                text_control.weight = ft.FontWeight.BOLD

            # INACTIVE
            else:

                item.bgcolor = ft.Colors.TRANSPARENT

                icon_control.color = TEXT_SECONDARY

                text_control.color = TEXT_SECONDARY

                text_control.weight = ft.FontWeight.W_500

        try:
            container.update()
        except Exception:
            pass

    # =====================================
    # NAVIGATION
    # =====================================

    def navigate(index):

        global ACTIVE_PAGE_INDEX

        ACTIVE_PAGE_INDEX = index

        update_active()

        change_page(index)

    # =====================================
    # NAV BUTTON
    # =====================================

    def nav_button(
        icon_name,
        label,
        index,
    ):

        icon_control = ft.Icon(
            icon_name,
            size=22,
            color=TEXT_SECONDARY,
        )

        text_control = ft.Text(
            label,
            size=14,
            color=TEXT_SECONDARY,
            weight=ft.FontWeight.W_500,
        )

        button = ft.Container(

            width=220,

            height=54,

            border_radius=16,

            padding=ft.Padding(
                left=18,
                right=18,
                top=0,
                bottom=0,
            ),

            animate=250,

            ink=True,

            content=ft.Row(
                [
                    icon_control,
                    text_control,
                ],

                spacing=14,

                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        # =====================================
        # HOVER EFFECT
        # =====================================

        def hover_effect(e):

            global ACTIVE_PAGE_INDEX

            if index != ACTIVE_PAGE_INDEX:

                if e.data == "true":

                    button.bgcolor = HOVER

                else:

                    button.bgcolor = ft.Colors.TRANSPARENT

                button.update()

        button.on_hover = hover_effect

        # =====================================
        # CLICK
        # =====================================

        button.on_click = lambda e: navigate(index)

        nav_items.append(button)

        return button

    # =====================================
    # DATE
    # =====================================

    today = datetime.now().strftime(
        "%A, %d %b %Y"
    )

    # =====================================
    # SIDEBAR
    # =====================================

    item_column = ft.Column(
        [
            # LOGO
            ft.Container(
                padding=ft.Padding(
                    left=8,
                    right=8,
                    top=10,
                    bottom=30,
                ),

                content=ft.Row(
                    [
                        ft.Container(
                            width=46,

                            height=46,

                            bgcolor=PRIMARY,

                            border_radius=14,

                            alignment=ft.Alignment(
                                0,
                                0,
                            ),

                            content=ft.Text(
                                "GS",

                                color=ft.Colors.WHITE,

                                size=16,

                                weight=ft.FontWeight.BOLD,
                            ),
                        ),

                        ft.Column(
                            [
                                ft.Text(
                                    "GrandStay",

                                    size=18,

                                    weight=ft.FontWeight.BOLD,

                                    color=TEXT_PRIMARY,
                                ),

                                ft.Text(
                                    "HOTEL MANAGEMENT",

                                    size=10,

                                    color=TEXT_SECONDARY,

                                    weight=ft.FontWeight.W_500,
                                ),
                            ],

                            spacing=0,
                        ),
                    ],

                    spacing=14,
                ),
            ),

            # NAVIGATION
            *[
                nav_button(
                    icon,
                    label,
                    i,
                )
                for i, (
                    icon,
                    label,
                ) in enumerate(nav_data)
            ],

            ft.Container(expand=True),

            # FOOTER
            ft.Container(
                padding=ft.Padding(
                    left=8,
                    right=8,
                    top=14,
                    bottom=14,
                ),

                content=ft.Column(
                    [
                        ft.Divider(
                            height=1,
                            color=BORDER,
                        ),

                        ft.Container(height=10),

                        ft.Row(
                            [
                                ft.Container(
                                    width=8,

                                    height=8,

                                    bgcolor=ft.Colors.GREEN,

                                    border_radius=50,
                                ),

                                ft.Text(
                                    "v2.0 Stable",

                                    size=11,

                                    color=TEXT_SECONDARY,
                                ),
                            ],

                            spacing=6,
                        ),

                        ft.Text(
                            today,

                            size=10,

                            color=ft.Colors.BLUE_GREY_400,
                        ),
                    ],

                    spacing=4,
                ),
            ),
        ],

        spacing=6,

        expand=True,
    )

    container = ft.Container(

        content=item_column,

        width=250,

        bgcolor=ft.Colors.WHITE,

        padding=ft.Padding(
            left=14,
            right=14,
            top=16,
            bottom=16,
        ),

        border=ft.Border(
            right=ft.BorderSide(
                1,
                BORDER,
            )
        ),
    )

    update_active()

    return container