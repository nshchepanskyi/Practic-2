# main.py

import flet as ft

from hotel_data import load_all_data

from components.navbar import navbar
from components.topbar import topbar

from views.login import login_view
from views.register import register_view

from views.dashboard import dashboard_view
from views.rooms import rooms_view
from views.reservations import reservations_view
from views.guests import guests_view
from views.services import services_view

import theme


def main(page: ft.Page):
    page.title = "GrandStay Hotel"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = theme.get("bg")
    page.window.width = 1700
    page.window.height = 950
    page.window.maximized = True
    page.padding = 0

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE_600,
            secondary=ft.Colors.CYAN_400,
        ),
    )

    load_all_data()

    main_content = ft.Container(
        expand=True,
        animate_opacity=300,
        animate_scale=300,
    )

    def open_dashboard(active_page=0):
        from components import navbar as navbar_module
        navbar_module.ACTIVE_PAGE_INDEX = active_page

        dashboard_content = ft.Container(
            expand=True,
            padding=24,
            animate_opacity=400,
            animate_scale=300,
        )

        def change_page(index):
            from components import navbar as navbar_module
            navbar_module.ACTIVE_PAGE_INDEX = index

            dashboard_content.opacity = 0
            page.update()

            if index == 0:
                dashboard_content.content = dashboard_view(page)
            elif index == 1:
                dashboard_content.content = rooms_view(page)
            elif index == 2:
                dashboard_content.content = reservations_view(page)
            elif index == 3:
                dashboard_content.content = guests_view(page)
            elif index == 4:
                dashboard_content.content = services_view(page)

            dashboard_content.opacity = 1
            page.update()

        def go_to_reservations():
            change_page(2)

        def rebuild_dashboard():
            page.theme_mode = ft.ThemeMode.DARK if theme.is_dark() else ft.ThemeMode.LIGHT
            page.bgcolor = theme.get("bg")
            from components import navbar as navbar_module
            open_dashboard(navbar_module.ACTIVE_PAGE_INDEX)

        def change_language():
            from l10n import toggle_lang
            toggle_lang()
            rebuild_dashboard()

        def change_theme():
            theme.toggle()
            rebuild_dashboard()

        def logout():
            open_login()

        change_page(active_page)

        main_content.content = ft.Row(
            [
                navbar(
                    change_page,
                    logout,
                ),

                ft.Column(
                    [
                        topbar(
                            page,
                            go_to_reservations,
                            change_language,
                            change_theme,
                        ),

                        dashboard_content,
                    ],

                    expand=True,

                    spacing=0,
                ),
            ],

            expand=True,

            spacing=0,
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