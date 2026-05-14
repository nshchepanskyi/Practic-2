import flet as ft

from hotel_data import (
    SERVICES_CATALOG,
    guests,
    service_orders,
    create_service_order,
    update_service_order_status,
)

ACCENT   = "#2563EB"
BORDER   = "#E2E8F0"
TEXT_PRI = "#1E293B"
TEXT_SEC = "#64748B"

STATUS_COLORS = {
    "Pending":     ("#FEF9C3", "#854D0E"),
    "In Progress": ("#DBEAFE", "#1E40AF"),
    "Completed":   ("#DCFCE7", "#166534"),
    "Cancelled":   ("#FEE2E2", "#991B1B"),
}

SERVICE_ICONS = {
    "Breakfast":        ft.Icons.FREE_BREAKFAST,
    "Laundry":          ft.Icons.LOCAL_LAUNDRY_SERVICE,
    "Spa":              ft.Icons.SPA,
    "Airport Transfer": ft.Icons.AIRPORT_SHUTTLE,
    "Room Cleaning":    ft.Icons.CLEANING_SERVICES,
    "Mini Bar Restock": ft.Icons.LOCAL_BAR,
}


def _make_border(color):
    """Return a full Border object — ft.border.all() is unavailable in this Flet version."""
    side = ft.BorderSide(2, color)
    return ft.Border(top=side, bottom=side, left=side, right=side)


def services_view(page):

    selected_service = {"item": None}

    # ── form fields ───────────────────────────────────────────────────────────
    guest_dropdown = ft.Dropdown(
        label="Select Guest",
        width=280,
        options=[],
        border_radius=10,
    )

    qty_field = ft.TextField(
        label="Quantity",
        value="1",
        width=110,
        border_radius=10,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    order_message = ft.Text(size=13)

    selected_label = ft.Text(
        "No service selected",
        size=13,
        color=TEXT_SEC,
        italic=True,
    )

    # ── orders table ──────────────────────────────────────────────────────────
    orders_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Order ID",  size=11, color=TEXT_SEC)),
            ft.DataColumn(ft.Text("Guest",     size=11, color=TEXT_SEC)),
            ft.DataColumn(ft.Text("Service",   size=11, color=TEXT_SEC)),
            ft.DataColumn(ft.Text("Qty",       size=11, color=TEXT_SEC)),
            ft.DataColumn(ft.Text("Total",     size=11, color=TEXT_SEC)),
            ft.DataColumn(ft.Text("Time",      size=11, color=TEXT_SEC)),
            ft.DataColumn(ft.Text("Status",    size=11, color=TEXT_SEC)),
            ft.DataColumn(ft.Text("Update",    size=11, color=TEXT_SEC)),
        ],
        rows=[],
        heading_row_color="#F8FAFC",
        heading_row_height=44,
        data_row_min_height=52,
        column_spacing=18,
        divider_thickness=1,
    )

    # ── helpers ───────────────────────────────────────────────────────────────

    def refresh_guests():
        guest_dropdown.options = [
            ft.dropdown.Option(key=g.guest_id, text=f"{g.name} ({g.guest_id})")
            for g in guests
        ]

    def refresh_orders():
        orders_table.rows.clear()
        for order in service_orders:
            bg, fg = STATUS_COLORS.get(order.status, ("#F1F5F9", "#475569"))

            status_dd = ft.Dropdown(
                value=order.status,
                width=130,
                border_radius=8,
                options=[
                    ft.dropdown.Option("Pending"),
                    ft.dropdown.Option("In Progress"),
                    ft.dropdown.Option("Completed"),
                    ft.dropdown.Option("Cancelled"),
                ],
                on_change=lambda e, oid=order.order_id: (
                    update_service_order_status(oid, e.control.value),
                    refresh_orders(),
                    page.update(),
                ),
            )

            orders_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(order.order_id, size=13,
                                            weight=ft.FontWeight.W_600, color=TEXT_PRI)),
                        ft.DataCell(ft.Text(order.guest.name, size=13, color=TEXT_PRI)),
                        ft.DataCell(ft.Text(order.service_name, size=13, color=TEXT_PRI)),
                        ft.DataCell(ft.Text(str(order.quantity), size=13, color=TEXT_SEC)),
                        ft.DataCell(ft.Text(f"${order.total:.2f}", size=13,
                                            weight=ft.FontWeight.W_600, color=TEXT_PRI)),
                        ft.DataCell(ft.Text(order.timestamp, size=11, color=TEXT_SEC)),
                        ft.DataCell(
                            ft.Container(
                                padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                                border_radius=20,
                                bgcolor=bg,
                                content=ft.Text(order.status, color=fg, size=11,
                                                weight=ft.FontWeight.W_500),
                            )
                        ),
                        ft.DataCell(status_dd),
                    ]
                )
            )
        page.update()

    # ── service card builder ──────────────────────────────────────────────────

    def make_service_card(svc):
        icon = SERVICE_ICONS.get(svc["name"], ft.Icons.ROOM_SERVICE)

        card = ft.Container(
            border_radius=12,
            bgcolor="white",
            padding=14,
            margin=ft.margin.only(bottom=8),
            border=_make_border(BORDER),
            animate=150,
        )

        def select_service(e, s=svc, c=card):
            for other in service_cards:
                other.border = _make_border(BORDER)
                other.bgcolor = "white"
            c.border  = _make_border(ACCENT)
            c.bgcolor = "#EFF6FF"
            selected_service["item"] = s
            selected_label.value = f"Selected: {s['name']}  —  ${s['price']} / unit"
            order_message.value = ""
            page.update()

        card.on_click = select_service
        card.content = ft.Row(
            [
                ft.Container(
                    width=40, height=40,
                    bgcolor="#EFF6FF",
                    border_radius=10,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(icon, color=ACCENT, size=20),
                ),
                ft.Column(
                    [
                        ft.Text(svc["name"], size=14, weight=ft.FontWeight.W_600,
                                color=TEXT_PRI),
                        ft.Text(f"${svc['price']} / unit", size=12, color=TEXT_SEC),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, color="#CBD5E1", size=18),
            ],
            spacing=12,
        )
        return card

    service_cards = [make_service_card(s) for s in SERVICES_CATALOG]

    # ── submit ────────────────────────────────────────────────────────────────

    def place_order(e):
        order_message.value = ""
        if not selected_service["item"]:
            order_message.value = "⚠ Select a service first."
            order_message.color = "#F59E0B"
            page.update()
            return
        if not guest_dropdown.value:
            order_message.value = "⚠ Select a guest."
            order_message.color = "#F59E0B"
            page.update()
            return
        try:
            qty = int(qty_field.value or "1")
            if qty < 1:
                raise ValueError
        except ValueError:
            order_message.value = "⚠ Quantity must be a positive integer."
            order_message.color = "#F59E0B"
            page.update()
            return

        svc = selected_service["item"]
        ok, result = create_service_order(
            guest_id=guest_dropdown.value,
            service_name=svc["name"],
            service_price=svc["price"],
            quantity=qty,
        )

        if ok:
            order_message.value = (
                f"✓ {result.order_id}: {svc['name']} × {qty} = ${result.total:.2f}"
            )
            order_message.color = "#16A34A"
            qty_field.value = "1"
            guest_dropdown.value = None
            for c in service_cards:
                c.border  = _make_border(BORDER)
                c.bgcolor = "white"
            selected_service["item"] = None
            selected_label.value = "No service selected"
            refresh_orders()
        else:
            order_message.value = f"✗ {result}"
            order_message.color = "#DC2626"

        page.update()

    # ── initial load ──────────────────────────────────────────────────────────
    refresh_guests()
    refresh_orders()

    # ── layout ────────────────────────────────────────────────────────────────

    def _panel(content, width=None, expand=False):
        return ft.Container(
            width=width,
            expand=expand,
            bgcolor="white",
            border_radius=14,
            padding=22,
            border=_make_border(BORDER),
            content=content,
        )

    left_panel = _panel(
        ft.Column(
            [
                ft.Text("Service Catalog", size=16,
                        weight=ft.FontWeight.BOLD, color=TEXT_PRI),
                ft.Text("Select a service, choose a guest, then place the order.",
                        size=12, color=TEXT_SEC),
                ft.Container(height=6),
                ft.Column(service_cards, spacing=0),
                ft.Divider(color=BORDER),
                ft.Text("Order Details", size=14,
                        weight=ft.FontWeight.W_600, color=TEXT_PRI),
                selected_label,
                ft.Container(height=4),
                guest_dropdown,
                qty_field,
                ft.Container(height=4),
                order_message,
                ft.Container(height=4),
                ft.ElevatedButton(
                    "Place Order",
                    icon=ft.Icons.SHOPPING_CART_OUTLINED,
                    height=44,
                    width=280,
                    style=ft.ButtonStyle(
                        bgcolor={"": ACCENT},
                        color={"": "white"},
                        elevation={"": 0},
                        shape={"": ft.RoundedRectangleBorder(radius=10)},
                    ),
                    on_click=place_order,
                ),
            ],
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
        ),
        width=340,
    )

    right_panel = _panel(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Service Orders", size=16,
                                weight=ft.FontWeight.BOLD, color=TEXT_PRI),
                        ft.ElevatedButton(
                            "Refresh",
                            icon=ft.Icons.REFRESH,
                            height=36,
                            style=ft.ButtonStyle(
                                bgcolor={"": "#F8FAFC"},
                                color={"": TEXT_SEC},
                                elevation={"": 0},
                                shape={"": ft.RoundedRectangleBorder(radius=8)},
                            ),
                            on_click=lambda e: (refresh_guests(), refresh_orders()),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=10),
                orders_table,
            ],
            expand=True,
        ),
        expand=True,
    )

    return ft.Column(
        [
            ft.Text("Services", size=24, weight=ft.FontWeight.BOLD, color=TEXT_PRI),
            ft.Container(height=16),
            ft.Row(
                [left_panel, right_panel],
                spacing=16,
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
