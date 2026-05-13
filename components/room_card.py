import flet as ft


def room_card(room):
    colors = {
        "Available": "#42C59A",
        "Occupied": "#13294B",
        "Cleaning": "#F5A623",
    }

    color = colors.get(
        room.status,
        "#42C59A",
    )

    return ft.Container(
        width=100,
        height=100,

        bgcolor="white",

        border_radius=20,

        shadow=ft.BoxShadow(
            blur_radius=15,
            color="#00000010",
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