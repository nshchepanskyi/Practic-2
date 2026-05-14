import flet as ft

from datetime import datetime


def topbar(page=None):
    today = datetime.now().strftime("%A, %d %B %Y")

    return ft.Container(
        bgcolor="white",
        padding=ft.Padding(left=28, right=28, top=14, bottom=14),
        border=ft.Border(bottom=ft.BorderSide(1, "#E2E8F0")),
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            "Hotel Dashboard",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color="#1E293B",
                        ),
                        ft.Text(today, size=12, color="#94A3B8"),
                    ],
                    spacing=1,
                ),

                ft.Row(
                    [
                        ft.ElevatedButton(
                            "+ New Reservation",
                            bgcolor="#2563EB",
                            color="white",
                            height=40,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                elevation=0,
                            ),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                            icon_color="#64748B",
                            icon_size=22,
                            style=ft.ButtonStyle(
                                bgcolor={"": "#F8FAFC"},
                                shape={"": ft.RoundedRectangleBorder(radius=10)},
                            ),
                        ),
                        ft.CircleAvatar(
                            bgcolor="#2563EB",
                            radius=18,
                            content=ft.Text(
                                "A",
                                color="white",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),
                    ],
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )
