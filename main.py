import flet as ft

from hotel_data import seed_data

from components.navbar import navbar
from components.topbar import topbar

from views.login import login_view
from views.register import register_view

from views.dashboard import dashboard_view
from views.rooms import rooms_view
from views.reservations import reservations_view
from views.guests import guests_view
from views.services import services_view


BACKGROUND = ft.Colors.GREY_100


def main(page: ft.Page):
    page.title = "GrandStay Hotel"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.bgcolor = BACKGROUND

    page.window.width = 1700
    page.window.height = 950

    page.padding = 15

    seed_data()

    main_content = ft.Container(
        expand=True
    )

    def open_dashboard():
        dashboard_content = ft.Container(
            expand=True,
        )

        def change_page(index):
            if index == 0:
                dashboard_content.content = (
                    dashboard_view(page)
                )

            elif index == 1:
                dashboard_content.content = (
                    rooms_view(page)
                )

            elif index == 2:
                dashboard_content.content = (
                    reservations_view(page)
                )

            elif index == 3:
                dashboard_content.content = (
                    guests_view(page)
                )

            elif index == 4:
                dashboard_content.content = (
                    services_view(page)
                )

            page.update()

        dashboard_content.content = (
            dashboard_view(page)
        )

        main_content.content = ft.Row(
            [
                navbar(change_page),

                ft.Column(
                    [
                        topbar(),

                        dashboard_content,
                    ],

                    expand=True,
                ),
            ],

            expand=True,
        )

        page.update()

    def open_login():
        main_content.content = login_view(
            page,

            open_register,

            open_dashboard,
        )

        page.update()

    def open_register():
        main_content.content = register_view(
            page,

            open_login,
        )

        page.update()

    open_login()

    page.add(main_content)


ft.run(main)