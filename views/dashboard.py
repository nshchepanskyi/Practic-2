import flet as ft

from hotel_data import (
    get_revenue_report,
    get_all_rooms,
    get_rooms_by_status,
    reservations,
    guests,
)


def stat_card(
    title,
    value,
    icon,
):
    return ft.Container(
        width=280,
        padding=20,
        border_radius=20,
        bgcolor=ft.Colors.BLUE_GREY_900,
        content=ft.Column(
            [
                ft.Icon(
                    icon,
                    size=40,
                ),

                ft.Text(
                    title,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    value,
                    size=28,
                ),
            ]
        ),
    )


def dashboard_view(
    page: ft.Page,
):
    content = ft.Row(
        wrap=True,
        spacing=20,
    )

    def refresh(e=None):
        content.controls.clear()

        report = get_revenue_report()

        total_rooms = len(
            get_all_rooms()
        )

        occupied = len(
            get_rooms_by_status(
                "Occupied"
            )
        )

        occupancy = 0

        if total_rooms > 0:
            occupancy = (
                occupied / total_rooms
            ) * 100

        content.controls.extend(
            [
                stat_card(
                    "Total Revenue",
                    f"${report['total']}",
                    ft.Icons.ATTACH_MONEY,
                ),

                stat_card(
                    "Reservations",
                    str(
                        len(
                            reservations
                        )
                    ),
                    ft.Icons.BOOK,
                ),

                stat_card(
                    "Guests",
                    str(len(guests)),
                    ft.Icons.PEOPLE,
                ),

                stat_card(
                    "Occupancy",
                    f"{occupancy:.1f}%",
                    ft.Icons.HOTEL,
                ),
            ]
        )

        page.update()

    refresh()

    return ft.Column(
        [
            ft.ElevatedButton(
                "Refresh Dashboard",
                icon=ft.Icons.REFRESH,
                on_click=refresh,
            ),

            ft.Container(height=20),

            content,
        ]
    )