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
        width=80,
        height=80,

        border_radius=18,

        bgcolor="white",

        border=ft.border.Border(
            top=ft.border.BorderSide(
                2,
                color,
            ),

            bottom=ft.border.BorderSide(
                2,
                color,
            ),

            left=ft.border.BorderSide(
                2,
                color,
            ),

            right=ft.border.BorderSide(
                2,
                color,
            ),
        ),

        alignment=ft.Alignment(0, 0),

        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.BED,
                    color=color,
                ),

                ft.Text(
                    room.room_number,
                    weight=ft.FontWeight.BOLD,
                ),
            ],

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )