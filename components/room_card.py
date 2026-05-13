import flet as ft


def room_card(room):
    colors = {
        "Available": ft.Colors.GREEN_400,
        "Occupied": ft.Colors.BLUE_700,
        "Cleaning": ft.Colors.ORANGE_400,
        "Maintenance": ft.Colors.RED_400,
    }

    color = colors.get(
        room.status,
        ft.Colors.GREEN_400,
    )

    return ft.Container(
        width=100,
        height=100,

        bgcolor=ft.Colors.WHITE,

        border_radius=20,

        shadow=ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.BLACK12,
        ),

        alignment=ft.Alignment(0, 0),

        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.BED,
                    color=color,
                    size=32,
                ),

                ft.Text(
                    room.room_number,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_GREY_900,
                ),

                ft.Text(
                    room.status,
                    size=12,
                    color=color,
                ),
            ],

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )