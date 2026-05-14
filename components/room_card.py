import flet as ft


def room_card(room):
    colors = {
        "Available":   "#22C55E",
        "Occupied":    "#2563EB",
        "Cleaning":    "#F59E0B",
        "Maintenance": "#EF4444",
    }
    bgs = {
        "Available":   "#F0FDF4",
        "Occupied":    "#EFF6FF",
        "Cleaning":    "#FFFBEB",
        "Maintenance": "#FEF2F2",
    }

    color = colors.get(room.status, "#22C55E")
    bg    = bgs.get(room.status, "#F0FDF4")

    return ft.Container(
        width=80,
        height=80,
        bgcolor=bg,
        border_radius=12,
        border=ft.Border(
            top=ft.BorderSide(1, "#E2E8F0"),
            bottom=ft.BorderSide(1, "#E2E8F0"),
            left=ft.BorderSide(1, "#E2E8F0"),
            right=ft.BorderSide(1, "#E2E8F0"),
        ),
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            [
                ft.Icon(ft.Icons.BED_OUTLINED, color=color, size=22),
                ft.Text(
                    room.room_number,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color="#1E293B",
                ),
                ft.Text(room.status, size=9, color=color),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
    )
