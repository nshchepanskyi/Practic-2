import flet as ft

from auth import register_user
from l10n import tr
from theme import get as C


def register_view(
    page,
    go_to_login,
):
    username = ft.TextField(
        label=tr("Username"),

        width=350,

        prefix_icon=ft.Icons.PERSON,
    )

    email = ft.TextField(
        label=tr("Email"),

        width=350,

        prefix_icon=ft.Icons.EMAIL,
    )

    password = ft.TextField(
        label=tr("Password"),

        password=True,

        can_reveal_password=True,

        width=350,

        prefix_icon=ft.Icons.LOCK,
    )

    confirm = ft.TextField(
        label=tr("Confirm Password"),

        password=True,

        can_reveal_password=True,

        width=350,

        prefix_icon=ft.Icons.LOCK,
    )

    message = ft.Text()

    def register_click(e):
        if not username.value:
            message.value = tr(
                "Enter username"
            )

            message.color = (
                ft.Colors.RED
            )

            page.update()

            return

        if not email.value:
            message.value = tr(
                "Enter email"
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

        if password.value != confirm.value:
            message.value = tr(
                "Passwords do not match"
            )

            message.color = (
                ft.Colors.RED
            )

            page.update()

            return

        success, result = register_user(
            username.value,
            email.value,
            password.value,
        )

        message.value = tr(result)

        if success:
            message.color = (
                ft.Colors.GREEN
            )

        else:
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
                        ft.Icons.PERSON_ADD,

                        size=70,

                        color=ft.Colors.GREEN_400,
                    ),

                    ft.Text(
                        tr("Create Account"),

                        size=34,

                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Container(height=20),

                    username,

                    email,

                    password,

                    confirm,

                    message,

                    ft.Container(height=20),

                    ft.ElevatedButton(
                        tr("Register"),

                        width=350,

                        height=50,

                        on_click=register_click,
                    ),

                    ft.TextButton(
                        tr("Back to login"),

                        on_click=lambda e:
                        go_to_login(),
                    ),
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )