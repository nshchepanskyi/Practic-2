import flet as ft

from auth import login_user


def login_view(
    page,
    go_to_register,
    login_success,
):
    login = ft.TextField(
        label="Username or Email",

        width=350,

        prefix_icon=ft.Icons.PERSON,
    )

    password = ft.TextField(
        label="Password",

        password=True,

        can_reveal_password=True,

        width=350,

        prefix_icon=ft.Icons.LOCK,
    )

    message = ft.Text()

    def login_click(e):
        if not login.value:
            message.value = (
                "Enter username or email"
            )

            message.color = (
                ft.Colors.RED
            )

            page.update()

            return

        if not password.value:
            message.value = (
                "Enter password"
            )

            message.color = (
                ft.Colors.RED
            )

            page.update()

            return

        success, result = login_user(
            login.value,
            password.value,
        )

        if success:
            login_success()

        else:
            message.value = result

            message.color = (
                ft.Colors.RED
            )

            page.update()

    return ft.Container(
        expand=True,

        alignment=ft.Alignment(0, 0),

        content=ft.Container(
            width=450,

            bgcolor=ft.Colors.WHITE,

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

                        color=ft.Colors.BLUE_900,
                    ),

                    ft.Text(
                        "GrandStay Login",

                        size=34,

                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Container(height=20),

                    login,

                    password,

                    message,

                    ft.Container(height=20),

                    ft.ElevatedButton(
                        "Login",

                        width=350,

                        height=50,

                        on_click=login_click,
                    ),

                    ft.TextButton(
                        "Create account",

                        on_click=lambda e:
                        go_to_register(),
                    ),
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )