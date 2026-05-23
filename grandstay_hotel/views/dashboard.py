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
from l10n import tr
from theme import get as C


def _card(content, padding=20):
    return ft.Container(
        bgcolor=C("surface"),
        border_radius=14,
        padding=padding,
        border=ft.Border(
            top=ft.BorderSide(1, C("border")),
            bottom=ft.BorderSide(1, C("border")),
            left=ft.BorderSide(1, C("border")),
            right=ft.BorderSide(1, C("border")),
        ),
        content=content,
    )


def _kpi_card(label, value, sub_text, sub_color, icon, icon_bg):
    return ft.Container(
        bgcolor=C("surface"),
        border_radius=14,
        padding=20,
        expand=True,
        border=ft.Border(
            top=ft.BorderSide(1, C("border")),
            bottom=ft.BorderSide(1, C("border")),
            left=ft.BorderSide(1, C("border")),
            right=ft.BorderSide(1, C("border")),
        ),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(label, size=12, color=C("text_secondary"),
                                weight=ft.FontWeight.W_500),
                        ft.Container(
                            width=36, height=36,
                            bgcolor=icon_bg,
                            border_radius=10,
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(icon, size=18, color=C("accent")),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=10),
                ft.Text(value, size=28, weight=ft.FontWeight.BOLD, color=C("text_primary")),
                ft.Container(height=4),
                ft.Text(sub_text, size=11, color=sub_color),
            ],
            spacing=0,
        ),
    )


def _status_badge(text):
    styles = {
        "Pending":       (ft.Colors.YELLOW_100, ft.Colors.YELLOW_900),
        "Checked-In":    (ft.Colors.GREEN_100, ft.Colors.GREEN_900),
        "Checked-Out":   (ft.Colors.BLUE_100, ft.Colors.BLUE_900),
        "Arrival Today": (ft.Colors.AMBER_100, ft.Colors.AMBER_900),
        "Reserved":      (ft.Colors.PURPLE_100, ft.Colors.PURPLE_900),
    }
    bg, fg = styles.get(text, (ft.Colors.BLUE_GREY_100, ft.Colors.BLUE_GREY_700))
    return ft.Container(
        padding=ft.Padding(left=10, right=10, top=4, bottom=4),
        border_radius=20,
        bgcolor=bg,
        content=ft.Text(tr(text), size=11, color=fg, weight=ft.FontWeight.W_500),
    )


def _legend(color, label):
    return ft.Row(
        [
            ft.Container(width=10, height=10, bgcolor=color, border_radius=5),
            ft.Text(label, size=12, color=C("text_secondary")),
        ],
        spacing=5,
    )


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

    checked_in = sum(1 for r in reservations if r.status == 'Checked-In')


    kpi_row = ft.Row(
        [
            _kpi_card(
                tr("OCCUPANCY"), f"{occupancy}%",
                tr("{occupied} of {total} rooms occupied", occupied=len(rooms) - avail, total=len(rooms)),
                C("text_secondary"), ft.Icons.HOTEL_OUTLINED, C("accent_bg"),
            ),
            _kpi_card(
                tr("AVAILABLE ROOMS"), str(avail),
                tr("+2 Ready for cleaning"),
                ft.Colors.GREEN_600, ft.Icons.MEETING_ROOM_OUTLINED, ft.Colors.GREEN_100,
            ),
            _kpi_card(
                tr("ARRIVALS TODAY"), str(arrivals_today),
                tr("{count} Checked-in so far", count=checked_in),
                ft.Colors.BLUE_600, ft.Icons.LOGIN_OUTLINED, ft.Colors.BLUE_100,
            ),
            _kpi_card(
                tr("TOTAL REVENUE"), f"${total_rev:,.0f}",
                tr("Rooms ${res_rev:,.0f}  ·  Services ${svc_rev:,.0f}", res_rev=res_rev, svc_rev=svc_rev),
                ft.Colors.GREEN_600, ft.Icons.ATTACH_MONEY, ft.Colors.GREEN_100,
            ),
        ],
        spacing=14,
    )


    AVATAR_COLORS = [
        ft.Colors.BLUE_100, ft.Colors.GREEN_100, ft.Colors.YELLOW_100,
        ft.Colors.PINK_100, ft.Colors.PURPLE_100,
    ]
    TEXT_COLORS = [
        ft.Colors.BLUE_900, ft.Colors.GREEN_900, ft.Colors.YELLOW_900,
        ft.Colors.PINK_900, ft.Colors.PURPLE_900,
    ]

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
                                ft.Text(r.guest.name, size=13, color=C("text_primary")),
                            ],
                            spacing=10,
                        )
                    ),
                    ft.DataCell(
                        ft.Container(
                            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                            border_radius=8,
                            bgcolor=C("accent_bg"),
                            content=ft.Text(r.room.room_number, size=12, color=C("accent")),
                        )
                    ),
                    ft.DataCell(ft.Text(ci, size=13, color=C("text_secondary"))),
                    ft.DataCell(_status_badge(r.status)),
                    ft.DataCell(
                        ft.Text(
                            f"${amount:,.2f}",
                            size=13,
                            weight=ft.FontWeight.W_600,
                            color=C("text_primary"),
                        )
                    ),
                ]
            )
        )

    if not rows:
        rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(tr("No reservations yet"), color=C("text_secondary"))),
                ft.DataCell(ft.Text("")),
                ft.DataCell(ft.Text("")),
                ft.DataCell(ft.Text("")),
                ft.DataCell(ft.Text("")),
            ])
        ]

    reservations_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text(tr("GUEST NAME"),  size=11, color=C("text_secondary"), weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text(tr("ROOM"),         size=11, color=C("text_secondary"), weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text(tr("CHECK IN"),     size=11, color=C("text_secondary"), weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text(tr("STATUS"),       size=11, color=C("text_secondary"), weight=ft.FontWeight.W_500)),
            ft.DataColumn(ft.Text(tr("AMOUNT"),       size=11, color=C("text_secondary"), weight=ft.FontWeight.W_500)),
        ],
        rows=rows,
        heading_row_color=C("table_heading"),
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
                        ft.Text(tr("Recent Reservations"), size=16,
                                weight=ft.FontWeight.BOLD, color=C("text_primary")),
                        ft.TextButton(
                            tr("VIEW ALL RECORDS"),
                            style=ft.ButtonStyle(color={"": C("accent")}),
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
                        ft.Text(tr("Room Status"), size=16,
                                weight=ft.FontWeight.BOLD, color=C("text_primary")),
                        ft.Row(
                            [
                                _legend(ft.Colors.GREEN_500, tr("Available")),
                                _legend(ft.Colors.BLUE_600, tr("Occupied")),
                                _legend(ft.Colors.AMBER_500, tr("Cleaning")),
                                _legend(ft.Colors.RED_500, tr("Maintenance")),
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
                            ft.Text(s["name"], size=12, color=C("text_primary"), expand=True),
                            ft.Text(tr("{count} orders", count=s["count"]), size=11, color=C("text_secondary")),
                            ft.Text(
                                f"${s['revenue']:.0f}",
                                size=12,
                                weight=ft.FontWeight.W_600,
                                color=C("text_primary"),
                            ),
                        ],
                    ),
                    ft.ProgressBar(
                        value=pct,
                        bgcolor=C("accent_bg"),
                        color=C("accent"),
                        height=6,
                        border_radius=3,
                    ),
                ],
                spacing=4,
            )
        )

    if not svc_rows:
        svc_rows = [ft.Text(tr("No service orders yet."), size=13, color=C("text_secondary"))]

    services_panel = _card(
        ft.Column(
            [
                ft.Text(tr("Services Revenue"), size=16,
                        weight=ft.FontWeight.BOLD, color=C("text_primary")),
                ft.Container(height=14),
                ft.Column(svc_rows, spacing=12),
            ]
        ),
        padding=22,
    )


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
