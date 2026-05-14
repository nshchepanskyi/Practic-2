import flet as ft

from datetime import datetime

PRIMARY   = "#1E3A5F"
ACCENT    = "#2563EB"
ACTIVE_BG = "#EFF6FF"
INACTIVE  = "#64748B"


def navbar(change_page):
    selected_index = 0
    nav_items = []
    container = ft.Container()

    nav_data = [
        (ft.Icons.DASHBOARD_OUTLINED,   "Dashboard"),
        (ft.Icons.MEETING_ROOM_OUTLINED, "Rooms"),
        (ft.Icons.BOOK_OUTLINED,         "Reservations"),
        (ft.Icons.PEOPLE_OUTLINED,       "Guests"),
        (ft.Icons.ROOM_SERVICE_OUTLINED, "Services"),
    ]

    def update_active():
        for i, item in enumerate(nav_items):
            row = item.content
            icon_ctrl = row.controls[0]
            label_ctrl = row.controls[1]
            if i == selected_index:
                item.bgcolor = ACTIVE_BG
                icon_ctrl.color = ACCENT
                label_ctrl.color = ACCENT
                label_ctrl.weight = ft.FontWeight.W_600
            else:
                item.bgcolor = "transparent"
                icon_ctrl.color = INACTIVE
                label_ctrl.color = INACTIVE
                label_ctrl.weight = ft.FontWeight.W_400
        try:
            container.update()
        except Exception:
            pass

    def navigate(index):
        nonlocal selected_index
        selected_index = index
        update_active()
        change_page(index)

    def nav_button(icon_name, label, index):
        icon_ctrl  = ft.Icon(icon_name, size=22, color=INACTIVE)
        label_ctrl = ft.Text(label, size=13, color=INACTIVE)

        btn = ft.Container(
            width=190,
            height=46,
            border_radius=10,
            bgcolor="transparent",
            padding=ft.Padding(left=16, right=16, top=0, bottom=0),
            animate=200,
            content=ft.Row(
                [icon_ctrl, label_ctrl],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        btn.on_click = lambda e: navigate(index)
        nav_items.append(btn)
        return btn

    # ── date ──────────────────────────────────────────────────────────────────
    today = datetime.now().strftime("%A, %d %b %Y")

    item_column = ft.Column(
        [
            # Logo block
            ft.Container(
                padding=ft.Padding(left=6, right=0, top=8, bottom=28),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    width=36, height=36,
                                    bgcolor=ACCENT,
                                    border_radius=10,
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Text(
                                        "GS",
                                        color="white",
                                        size=13,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                                ft.Column(
                                    [
                                        ft.Text(
                                            "GrandStay",
                                            size=15,
                                            weight=ft.FontWeight.BOLD,
                                            color=PRIMARY,
                                        ),
                                        ft.Text(
                                            "HOTEL MANAGEMENT",
                                            size=8,
                                            color=INACTIVE,
                                            weight=ft.FontWeight.W_500,
                                        ),
                                    ],
                                    spacing=0,
                                ),
                            ],
                            spacing=10,
                        ),
                    ]
                ),
            ),

            # Nav items
            *[nav_button(icon, label, i) for i, (icon, label) in enumerate(nav_data)],

            ft.Container(expand=True),

            # System status footer
            ft.Container(
                padding=ft.Padding(left=6, right=6, top=12, bottom=12),
                content=ft.Column(
                    [
                        ft.Divider(height=1, color="#E2E8F0"),
                        ft.Container(height=10),
                        ft.Row(
                            [
                                ft.Container(
                                    width=8, height=8,
                                    bgcolor="#22C55E",
                                    border_radius=4,
                                ),
                                ft.Text("v1.2.0 Stable", size=11, color=INACTIVE),
                            ],
                            spacing=6,
                        ),
                        ft.Text(today, size=10, color="#94A3B8"),
                    ],
                    spacing=4,
                ),
            ),
        ],
        spacing=4,
        expand=True,
    )

    container.content = item_column
    container.width = 220
    container.bgcolor = "white"
    container.padding = ft.Padding(left=14, right=14, top=16, bottom=16)
    container.border = ft.Border(
        right=ft.BorderSide(1, "#E2E8F0")
    )

    update_active()
    return container
