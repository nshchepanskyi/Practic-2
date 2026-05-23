import flet as ft
from theme import get as C


def stat_card(title, value, icon, color):
    return ft.Container(
        width=240,
        bgcolor=C("surface"),
        border_radius=14,
        padding=20,
        border=ft.Border(
            top=ft.BorderSide(1, C("border")),
            bottom=ft.BorderSide(1, C("border")),
            left=ft.BorderSide(1, C("border")),
            right=ft.BorderSide(1, C("border")),
        ),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(title, size=12, color=C("text_secondary"),
                                weight=ft.FontWeight.W_500),
                        ft.Container(
                            width=36, height=36,
                            border_radius=10,
                            bgcolor=color + "1A",
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(icon, color=color, size=18),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=12),
                ft.Text(
                    value,
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=C("text_primary"),
                ),
            ],
            spacing=0,
        ),
    )
