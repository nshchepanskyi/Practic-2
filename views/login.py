import flet as ft

from auth import login_user
from l10n import tr
from theme import get as C


def login_view(
    page,
    go_to_register,
    login_success,
):
    login = ft.TextField(
        label=tr("Username or Email"),

        width=350,

        prefix_icon=ft.Icons.PERSON,
    )

    password = ft.TextField(
        label=tr("Password"),

        password=True,

        can_reveal_password=True,

        width=350,

        prefix_icon=ft.Icons.LOCK,
    )

    message = ft.Text()

    def login_click(e):
        login_val = login.value.strip()

        if not login_val:
            message.value = tr(
                "Enter username or email"
            )

            message.color = (
                ft.Colors.RED
            )

            page.update()

            return

        if not password.value:
            message.value = tr(
                "Enter password"
            )

            message.color = (
                ft.Colors.RED
            )

            page.update()

            return

        success, result = login_user(
            login_val,
            password.value,
        )

        if success:
            login_success()

        else:
            message.value = tr(result)

            message.color = (
                ft.Colors.RED
            )

            page.update()

    return ft.Container(
        expand=True,

        alignment=ft.Alignment(0, 0),

        content=ft.Container(
            width=450,

            bgcolor=C("surface"),

            border_radius=25,

            padding=40,

            shadow=ft.BoxShadow(
                blur_radius=25,
                color=ft.Colors.BLACK12,
            ),

            content=ft.Column(
                [
                    ft.Icon(
                        ft.Icons.HOTEL,

                        size=70,

                        color=C("navbar_brand"),
                    ),

                    ft.Text(
                        tr("GrandStay Login"),

                        size=34,

                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Container(height=20),

                    login,

                    password,

                    message,

                    ft.Container(height=20),

                    ft.ElevatedButton(
                        tr("Login"),

                        width=350,

                        height=50,

                        on_click=login_click,
                    ),

                    ft.TextButton(
                        tr("Create account"),

                        on_click=lambda e:
                        go_to_register(),
                    ),
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )