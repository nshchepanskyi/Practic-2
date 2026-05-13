import flet as ft

from hotel_data import seed_data

from components.sidebar import sidebar

from views.dashboard import dashboard_view
from views.rooms import rooms_view
from views.reservations import reservations_view


BG = "#F5F7FB"


def main(page: ft.Page):
    page.title = "GrandStay Hotel"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BG

    page.window.width = 1600
    page.window.height = 950

    page.padding = 15
    page.spacing = 0

    seed_data()

    content = ft.Container(
        expand=True,
        padding=20,
    )

    def change_page(index):
        if index == 0:
            content.content = dashboard_view(page)

        elif index == 1:
            content.content = rooms_view(page)

        elif index == 2:
            content.content = reservations_view(page)

        page.update()

    content.content = dashboard_view(page)

    page.add(
        ft.Row(
            [
                sidebar(change_page),

                content,
            ],
            expand=True,
        )
    )


ft.run(main)