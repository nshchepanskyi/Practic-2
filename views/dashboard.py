import flet as ft

from hotel_data import (
    rooms,
    reservations,
    guests,
    service_orders,
    calc_total_revenue,
    calc_reservation_revenue,
    calc_service_revenue,
    get_occupancy_rate,
    get_services_summary,
)

from components.room_card import room_card


# ── palette ───────────────────────────────────────────────────────────────────
CARD_BG   = "white"
BORDER    = "#E2E8F0"
TEXT_PRI  = "#1E293B"
TEXT_SEC  = "#64748B"
ACCENT    = "#2563EB"


# ── helpers ───────────────────────────────────────────────────────────────────

def _card(content, padding=20):
    return ft.Container(
        bgcolor=CARD_BG,
        border_radius=14,
        padding=padding,
        border=ft.Border(
            top=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
            left=ft.BorderSide(1, BORDER),
            right=ft.BorderSide(1, BORDER),
        ),
        content=content,
    )


def _kpi_card(label, value, sub_text, sub_color, icon, icon_bg):
    return ft.Container(
        bgcolor=CARD_BG,
        border_radius=14,
        padding=20,
        expand=True,
        border=ft.Border(
            top=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
            left=ft.BorderSide(1, BORDER),
            right=ft.BorderSide(1, BORDER),
        ),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(label, size=12, color=TEXT_SEC,
                                weight=ft.FontWeight.W_500),
                        ft.Container(
                            width=36, height=36,
                            bgcolor=icon_bg,
                            border_radius=10,
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(icon, size=18, color=ACCENT),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=10),
                ft.Text(value, size=28, weight=ft.FontWeight.BOLD, color=TEXT_PRI),
                ft.Container(height=4),
                ft.Text(sub_text, size=11, color=sub_color),
            ],
            spacing=0,
        ),
    )


def _status_badge(text):
    styles = {
        "Pending":     ("#FEF9C3", "#854D0E"),
        "Checked-In":  ("#DCFCE7", "#166534"),
        "Checked-Out": ("#DBEAFE", "#1E40AF"),
        "Arrival Today": ("#FEF3C7", "#92400E"),
        "Reserved":    ("#EDE9FE", "#4C1D95"),
    }
    bg, fg = styles.get(text, ("#F1F5F9", "#475569"))
    return ft.Container(
        padding=ft.Padding(left=10, right=10, top=4, bottom=4),
        border_radius=20,
        bgcolor=bg,
        content=ft.Text(text, size=11, color=fg, weight=ft.FontWeight.W_500),
    )


def _legend(color, label):
    return ft.Row(
        [
            ft.Container(width=10, height=10, bgcolor=color, border_radius=5),
            ft.Text(label, size=12, color=TEXT_SEC),
        ],
        spacing=5,
    )


# ── main view ─────────────────────────────────────────────────────────────────

def dashboard_view(page):

    total_rev  = calc_total_revenue()
    res_rev    = calc_reservation_revenue()
    svc_rev    = calc_service_revenue()
    occupancy  = get_occupancy_rate()
    avail      = sum(1 for r in rooms if r.status == "Available")

    arrivals_today = sum(
        1 for r in reservations
        if r.status in ("Pending", "Checked-In")
    )

    # ── KPI row ───────────────────────────────────────────────────────────────
    kpi_row = ft.Row(
        [
            _kpi_card(
                "OCCUPANCY", f"{occupancy}%",
                f"{len(rooms) - avail} of {len(rooms)} rooms occupied",
                TEXT_SEC, ft.Icons.HOTEL_OUTLINED, "#EFF6FF",
            ),
            _kpi_card(
                "AVAILABLE ROOMS", str(avail),
                "+2 Ready for cleaning",
                "#16A34A", ft.Icons.MEETING_ROOM_OUTLINED, "#F0FDF4",
            ),
            _kpi_card(
                "ARRIVALS TODAY", str(arrivals_today),
                f"{sum(1 for r in reservations if r.status == 'Checked-In')} Checked-in so far",
                "#2563EB", ft.Icons.LOGIN_OUTLINED, "#EFF6FF",
            ),
            _kpi_card(
                "TOTAL REVENUE", f"${total_rev:,.0f}",
                f"Rooms ${res_rev:,.0f}  ·  Services ${svc_rev:,.0f}",
                "#16A34A", ft.Icons.ATTACH_MONEY, "#F0FDF4",
            ),
        ],
        spacing=14,
    )

    # ── recent reservations table ─────────────────────────────────────────────
    AVATAR_COLORS = ["#DBEAFE", "#DCFCE7", "#FEF9C3", "#FCE7F3", "#EDE9FE"]
    TEXT_COLORS   = ["#1E40AF", "#166534", "#854D0E", "#831843", "#4C1D95"]

    rows = []
    for i, r in enumerate(list(reversed(reservations))[:6]):
        idx = i % len(AVATAR_COLORS)
        initial = r.guest.name[0].upper()

        try:
            from datetime import datetime
            ci = datetime.strptime(r.check_in, "%Y-%m-%d").strftime("%d %b %Y")
        except Exception:
            ci = r.check_in

        try:
            nights = max(
                (
                    __import__("datetime").datetime.strptime(r.check_out, "%Y-%m-%d")
                    - __import__("datetime").datetime.strptime(r.check_in, "%Y-%m-%d")
                ).days, 1
            )
        except Exception:
            nights = 1
        amount = r.room.price * nights

        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Row(
                            [
                                ft.Container(
                                    width=32, height=32,
                                    bgcolor=AVATAR_COLORS[idx],
                                    border_radius=16,
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Text(
                                        initial,
                                        size=13,
                                        weight=ft.FontWeight.BOLD,
                                        color=TEXT_COLORS[idx],
                                    ),
                                ),
                                ft.Text(r.guest.name, size=13, color=TEXT_PRI),
                            ],
                            spacing=10,
                        )
                    ),
                    ft.DataCell(
                        ft.Container(
                            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                            border_radius=8,
                            bgcolor="#F1F5F9",
                            content=ft.Text(r.room.room_number, size=12, color=TEXT_SEC),
                        )
                    ),
                    ft.DataCell(ft.Text(ci, size=13, color=TEXT_SEC)),
                    ft.DataCell(_status_badge(r.status)),
                    ft.DataCell(
                        ft.Text(
                            f"${amount:,.2f}",
                            size=13,
                            weight=ft.FontWeight.W_600,
                            color=TEXT_PRI,
                        )
                    ),
                ]
            )
        )

    if not rows:
        rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("No reservations yet", color=TEXT_SEC)),
                ft.DataCell(ft.Text("")),
                ft.DataCell(ft.Text("")),
                ft.DataCell(ft.Text("")),
                ft.DataCell(ft.Text("")),
            ])
        ]

    reservations_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("GUEST NAME",  size=11, color=TEXT_SEC, weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text("ROOM",         size=11, color=TEXT_SEC, weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text("CHECK IN",     size=11, color=TEXT_SEC, weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text("STATUS",       size=11, color=TEXT_SEC, weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text("AMOUNT",       size=11, color=TEXT_SEC, weight=ft.FontWeight.W_500)),
        ],
        rows=rows,
        heading_row_color="#F8FAFC",
        heading_row_height=44,
        data_row_min_height=56,
        column_spacing=24,
        divider_thickness=1,
    )

    reservations_panel = _card(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Recent Reservations", size=16,
                                weight=ft.FontWeight.BOLD, color=TEXT_PRI),
                        ft.TextButton(
                            "VIEW ALL RECORDS",
                            style=ft.ButtonStyle(color={"": ACCENT}),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=8),
                ft.Container(
                    content=reservations_table,
                    expand=True,
                ),
            ],
            expand=True,
        ),
        padding=22,
    )

    # ── room grid ─────────────────────────────────────────────────────────────
    room_grid = ft.GridView(
        runs_count=8,
        spacing=10,
        run_spacing=10,
        height=160,
    )
    for room in rooms:
        room_grid.controls.append(room_card(room))

    rooms_panel = _card(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Room Status", size=16,
                                weight=ft.FontWeight.BOLD, color=TEXT_PRI),
                        ft.Row(
                            [
                                _legend("#22C55E", "Available"),
                                _legend("#2563EB", "Occupied"),
                                _legend("#F59E0B", "Cleaning"),
                                _legend("#EF4444", "Maintenance"),
                            ],
                            spacing=16,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=14),
                room_grid,
            ]
        ),
        padding=22,
    )

    # ── services summary ──────────────────────────────────────────────────────
    svc_summary = get_services_summary()
    max_rev = max((s["revenue"] for s in svc_summary), default=1)

    svc_rows = []
    for s in svc_summary[:5]:
        pct = s["revenue"] / max_rev if max_rev else 0
        svc_rows.append(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(s["name"], size=12, color=TEXT_PRI, expand=True),
                            ft.Text(f"{s['count']} orders", size=11, color=TEXT_SEC),
                            ft.Text(
                                f"${s['revenue']:.0f}",
                                size=12,
                                weight=ft.FontWeight.W_600,
                                color=TEXT_PRI,
                            ),
                        ],
                    ),
                    ft.ProgressBar(
                        value=pct,
                        bgcolor="#F1F5F9",
                        color=ACCENT,
                        height=6,
                        border_radius=3,
                    ),
                ],
                spacing=4,
            )
        )

    if not svc_rows:
        svc_rows = [ft.Text("No service orders yet.", size=13, color=TEXT_SEC)]

    services_panel = _card(
        ft.Column(
            [
                ft.Text("Services Revenue", size=16,
                        weight=ft.FontWeight.BOLD, color=TEXT_PRI),
                ft.Container(height=14),
                ft.Column(svc_rows, spacing=12),
            ]
        ),
        padding=22,
    )

    # ── assemble ──────────────────────────────────────────────────────────────
    return ft.Column(
        [
            kpi_row,
            ft.Container(height=16),
            reservations_panel,
            ft.Container(height=16),
            ft.Row(
                [
                    ft.Container(content=rooms_panel, expand=2),
                    ft.Container(content=services_panel, expand=1),
                ],
                spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Container(height=16),
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
