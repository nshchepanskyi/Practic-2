import flet as ft


def stat_card(title, value, icon, color):
    return ft.Container(
        width=240,
        bgcolor="white",
        border_radius=14,
        padding=20,
        border=ft.Border(
            top=ft.BorderSide(1, "#E2E8F0"),
            bottom=ft.BorderSide(1, "#E2E8F0"),
            left=ft.BorderSide(1, "#E2E8F0"),
            right=ft.BorderSide(1, "#E2E8F0"),
        ),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(title, size=12, color="#64748B",
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
                    color="#1E293B",
                ),
            ],
            spacing=0,
        ),
    )
