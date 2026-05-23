import flet as ft
import random
import json
import os

from datetime import datetime

from l10n import tr
from theme import get as C, is_dark


NOTIFICATIONS_FILE = "storage/notifications.json"


if not os.path.exists("storage"):
    os.makedirs("storage")


if not os.path.exists(NOTIFICATIONS_FILE):
    data = [
        {"user": "Emma Wilson", "message": "Requested extra towels for room 201"},
        {"user": "Michael Brown", "message": "Checked into room 305"},
        {"user": "Sophia Davis", "message": "Ordered breakfast service"},
        {"user": "Daniel Taylor", "message": "Requested airport transfer"},
        {"user": "Olivia Anderson", "message": "Extended reservation by 2 nights"},
    ]

    with open(NOTIFICATIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_notifications():
    try:
        with open(NOTIFICATIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def topbar(
    page=None,
    go_to_reservations=None,
    change_language=None,
    change_theme=None,
):
    today = datetime.now().strftime("%A, %d %B %Y")

    notifications = load_notifications()
    random.shuffle(notifications)
    notifications = notifications[:5]

    notification_items = []

    for item in notifications:
        user_name = item.get("user", "Unknown User")
        message = item.get("message", "No message")

        notification_items.append(
            ft.PopupMenuItem(
                content=ft.Container(
                    width=320,
                    padding=10,
                    content=ft.Row(
                        [
                            ft.CircleAvatar(
                                radius=18,
                                bgcolor=C("primary"),
                                content=ft.Text(
                                    user_name[0],
                                    color=C("on_primary"),
                                ),
                            ),

                            ft.Column(
                                [
                                    ft.Text(
                                        user_name,
                                        size=14,
                                        weight=ft.FontWeight.BOLD,
                                    ),

                                    ft.Text(
                                        message,
                                        size=12,
                                        color=C("notification_text"),
                                    ),
                                ],

                                spacing=2,
                            ),
                        ],

                        spacing=12,
                    ),
                )
            )
        )

    notification_button = ft.PopupMenuButton(
        icon=ft.Icons.NOTIFICATIONS,
        icon_color=C("notification_icon"),
        tooltip=tr("Notifications"),
        items=notification_items,
    )

    return ft.Container(
        bgcolor=C("surface"),

        padding=ft.Padding(
            left=28,
            right=28,
            top=14,
            bottom=14,
        ),

        border=ft.Border(
            bottom=ft.BorderSide(
                1,
                C("divider"),
            )
        ),

        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            value=tr("Hotel Dashboard"),

                            size=24,

                            weight=ft.FontWeight.BOLD,

                            color=C("topbar_title"),
                        ),

                        ft.Text(
                            today,

                            size=12,

                            color=C("topbar_date"),
                        ),
                    ],

                    spacing=1,
                ),

                ft.Row(
                    [
                        ft.ElevatedButton(
                            tr("+ New Reservation"),

                            bgcolor=C("primary"),

                            color=C("on_primary"),

                            on_click=lambda e:
                            go_to_reservations(),

                            style=ft.ButtonStyle(
                                elevation=8,

                                shadow_color=C("accent_bg"),

                                shape=ft.RoundedRectangleBorder(
                                    radius=14
                                ),
                            ),
                        ),

                        ft.IconButton(
                            icon=ft.Icons.DARK_MODE if not is_dark() else ft.Icons.LIGHT_MODE,
                            icon_color=C("accent"),
                            tooltip="Dark/Light",
                            on_click=lambda e: change_theme() if change_theme else None,
                        ),

                        ft.IconButton(
                            icon=ft.Icons.LANGUAGE,
                            icon_color=C("accent"),
                            tooltip="EN/UA",
                            on_click=lambda e: change_language() if change_language else None,
                        ),

                        notification_button,
                    ],

                    spacing=6,
                ),
            ],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )