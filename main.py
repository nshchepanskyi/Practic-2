import flet as ft

from hotel_data import seed_data

from components.navbar import navbar
from components.topbar import topbar

from views.dashboard import dashboard_view
from views.rooms import rooms_view
from views.reservations import reservations_view
from views.guests import guests_view
from views.services import services_view


BACKGROUND = "#F5F7FB"


def main(page: ft.Page):
    page.title = "GrandStay Hotel"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.bgcolor = BACKGROUND

    page.window.width = 1700
    page.window.height = 950

    page.padding = 15

    seed_data()

    content = ft.Container(
        expand=True,
    )

    def change_page(index):
        if index == 0:
            content.content = dashboard_view(page)

        elif index == 1:
            content.content = rooms_view(page)

        elif index == 2:
            content.content = reservations_view(page)

        elif index == 3:
            content.content = guests_view(page)

        elif index == 4:
            content.content = services_view(page)

        page.update()

    content.content = dashboard_view(page)

    page.add(
        ft.Row(
            [
                navbar(change_page),

                ft.Column(
                    [
                        topbar(),

                        content,
                    ],

                    expand=True,
                ),
            ],

            expand=True,
        )
    )


ft.run(main)