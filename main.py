import flet as ft

from hotel_data import seed_data

from views.rooms import rooms_view
from views.reservations import reservations_view
from views.dashboard import dashboard_view


def main(page: ft.Page):
    page.title = "GrandStay Hotel Management"
    page.theme_mode = ft.ThemeMode.DARK

    page.window.width = 1400
    page.window.height = 900

    page.padding = 20

    seed_data()

    tab_content = ft.Container(
        expand=True,
        content=rooms_view(page),
    )

    def change_tab(e):
        if tabs.selected_index == 0:
            tab_content.content = rooms_view(page)

        elif tabs.selected_index == 1:
            tab_content.content = reservations_view(page)

        elif tabs.selected_index == 2:
            tab_content.content = dashboard_view(page)

        page.update()

    tabs = ft.Tabs(
        length=3,
        selected_index=0,

        content=ft.Column(
            [
                ft.TabBar(
                    tabs=[
                        ft.Tab(
                            label="Rooms"
                        ),

                        ft.Tab(
                            label="Reservations"
                        ),

                        ft.Tab(
                            label="Dashboard"
                        ),
                    ],

                    on_click=change_tab,
                ),

                tab_content,
            ],

            expand=True,
        ),
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "GrandStay Hotel Management System",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                ),

                tabs,
            ],

            expand=True,
        )
    )


ft.run(main)