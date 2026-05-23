import flet as ft
from theme import get as C


def room_card(room):
    colors = {
        "Available":   ft.Colors.GREEN_500,
        "Occupied":    ft.Colors.BLUE_600,
        "Cleaning":    ft.Colors.AMBER_500,
        "Maintenance": ft.Colors.RED_500,
    }
    bgs = {
        "Available":   ft.Colors.GREEN_50,
        "Occupied":    ft.Colors.BLUE_50,
        "Cleaning":    ft.Colors.AMBER_50,
        "Maintenance": ft.Colors.RED_50,
    }

    color = colors.get(room.status, ft.Colors.GREEN_500)
    bg    = bgs.get(room.status, ft.Colors.GREEN_50)

    return ft.Container(
        width=80,
        height=80,
        bgcolor=bg,
        border_radius=12,
        border=ft.Border(
            top=ft.BorderSide(1, C("border")),
            bottom=ft.BorderSide(1, C("border")),
            left=ft.BorderSide(1, C("border")),
            right=ft.BorderSide(1, C("border")),
        ),
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            [
                ft.Icon(ft.Icons.BED_OUTLINED, color=color, size=22),
                ft.Text(
                    room.room_number,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color=C("text_primary"),
                ),
                ft.Text(room.status, size=9, color=color),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
    )
