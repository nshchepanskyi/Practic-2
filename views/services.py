import flet as ft

from hotel_data import (
    SERVICES_CATALOG,
    guests,
    service_orders,
    create_service_order,
    update_service_order_status,
)

ACCENT = "#2563EB"
BORDER = "#E2E8F0"
TEXT_PRI = "#1E293B"
TEXT_SEC = "#64748B"

STATUS_COLORS = {
    "Pending": ("#FEF9C3", "#854D0E"),
    "In Progress": ("#DBEAFE", "#1E40AF"),
    "Completed": ("#DCFCE7", "#166534"),
    "Cancelled": ("#FEE2E2", "#991B1B"),
}

SERVICE_ICONS = {
    "Breakfast": ft.Icons.FREE_BREAKFAST,
    "Laundry": ft.Icons.LOCAL_LAUNDRY_SERVICE,
    "Spa": ft.Icons.SPA,
    "Airport Transfer": ft.Icons.AIRPORT_SHUTTLE,
}


def _make_border(color):

    side = ft.BorderSide(2, color)

    return ft.Border(
        top=side,
        bottom=side,
        left=side,
        right=side,
    )


def services_view(page):

    selected_service = {"item": None}

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

    order_message = ft.Text(
        size=13
    )

    selected_label = ft.Text(
        "No service selected",
        size=13,
        color=TEXT_SEC,
        italic=True,
    )

    orders_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Order ID")),
            ft.DataColumn(ft.Text("Guest")),
            ft.DataColumn(ft.Text("Service")),
            ft.DataColumn(ft.Text("Qty")),
            ft.DataColumn(ft.Text("Total")),
            ft.DataColumn(ft.Text("Time")),
            ft.DataColumn(ft.Text("Status")),
            ft.DataColumn(ft.Text("Update")),
        ],

        rows=[],
    )

    # =====================================
    # REFRESH GUESTS
    # =====================================

    def refresh_guests():

        guest_dropdown.options = [
            ft.dropdown.Option(
                key=g.guest_id,
                text=f"{g.name} ({g.guest_id})",
            )
            for g in guests
        ]

    # =====================================
    # STATUS CHANGE
    # =====================================

    def change_status(order_id, status):

        update_service_order_status(
            order_id,
            status,
        )

        refresh_orders()

    # =====================================
    # REFRESH ORDERS
    # =====================================

    def refresh_orders():

        orders_table.rows.clear()

        for order in service_orders:

            bg, fg = STATUS_COLORS.get(
                order.status,
                ("#F1F5F9", "#475569"),
            )

            status_dropdown = ft.Dropdown(
                width=140,

                value=order.status,

                options=[
                    ft.dropdown.Option("Pending"),
                    ft.dropdown.Option("In Progress"),
                    ft.dropdown.Option("Completed"),
                    ft.dropdown.Option("Cancelled"),
                ],
            )

            save_button = ft.ElevatedButton(
                "Save",

                on_click=lambda e,
                oid=order.order_id,
                dd=status_dropdown: change_status(
                    oid,
                    dd.value,
                ),
            )

            orders_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(order.order_id)
                        ),

                        ft.DataCell(
                            ft.Text(order.guest.name)
                        ),

                        ft.DataCell(
                            ft.Text(order.service_name)
                        ),

                        ft.DataCell(
                            ft.Text(str(order.quantity))
                        ),

                        ft.DataCell(
                            ft.Text(
                                f"${order.total:.2f}"
                            )
                        ),

                        ft.DataCell(
                            ft.Text(order.timestamp)
                        ),

                        ft.DataCell(
                            ft.Container(
                                padding=10,

                                border_radius=20,

                                bgcolor=bg,

                                content=ft.Text(
                                    order.status,
                                    color=fg,
                                ),
                            )
                        ),

                        ft.DataCell(
                            ft.Row(
                                [
                                    status_dropdown,
                                    save_button,
                                ]
                            )
                        ),
                    ]
                )
            )

        page.update()

    # =====================================
    # SERVICE CARD
    # =====================================

    def make_service_card(svc):

        icon = SERVICE_ICONS.get(
            svc["name"],
            ft.Icons.ROOM_SERVICE,
        )

        card = ft.Container(
            border_radius=12,

            bgcolor="white",

            padding=14,

            margin=ft.Margin(
                left=0,
                top=0,
                right=0,
                bottom=8,
            ),

            border=_make_border(BORDER),
        )

        def select_service(
            e,
            s=svc,
            c=card,
        ):

            for other in service_cards:

                other.border = _make_border(BORDER)

                other.bgcolor = "white"

            c.border = _make_border(ACCENT)

            c.bgcolor = "#EFF6FF"

            selected_service["item"] = s

            selected_label.value = (
                f"Selected: {s['name']} - ${s['price']}"
            )

            page.update()

        card.on_click = select_service

        card.content = ft.Row(
            [
                ft.Icon(
                    icon,
                    color=ACCENT,
                    size=28,
                ),

                ft.Column(
                    [
                        ft.Text(
                            svc["name"],
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Text(
                            f"${svc['price']}",
                            color=TEXT_SEC,
                        ),
                    ],

                    spacing=2,
                ),
            ]
        )

        return card

    service_cards = [
        make_service_card(s)
        for s in SERVICES_CATALOG
    ]

    # =====================================
    # PLACE ORDER
    # =====================================

    def place_order(e):

        if not selected_service["item"]:

            order_message.value = (
                "Select service"
            )

            order_message.color = "red"

            page.update()

            return

        if not guest_dropdown.value:

            order_message.value = (
                "Select guest"
            )

            order_message.color = "red"

            page.update()

            return

        try:

            qty = int(qty_field.value)

            if qty < 1:
                raise ValueError

        except Exception:

            order_message.value = (
                "Invalid quantity"
            )

            order_message.color = "red"

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
                "Order created"
            )

            order_message.color = "green"

            qty_field.value = "1"

            guest_dropdown.value = None

            selected_service["item"] = None

            selected_label.value = (
                "No service selected"
            )

            refresh_orders()

        else:

            order_message.value = result

            order_message.color = "red"

        page.update()

    refresh_guests()

    refresh_orders()

    # =====================================
    # PANELS
    # =====================================

    def panel(
        content,
        width=None,
        expand=False,
    ):

        return ft.Container(
            width=width,

            expand=expand,

            bgcolor="white",

            border_radius=14,

            padding=22,

            border=_make_border(BORDER),

            content=content,
        )

    left_panel = panel(
        ft.Column(
            [
                ft.Text(
                    "Service Catalog",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Container(height=10),

                ft.Column(
                    service_cards
                ),

                ft.Divider(),

                selected_label,

                guest_dropdown,

                qty_field,

                order_message,

                ft.ElevatedButton(
                    "Place Order",

                    icon=ft.Icons.SHOPPING_CART,

                    bgcolor=ACCENT,

                    color="white",

                    on_click=place_order,
                ),
            ],

            spacing=10,
        ),

        width=350,
    )

    right_panel = panel(
        ft.Column(
            [
                ft.Text(
                    "Service Orders",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Container(height=10),

                orders_table,
            ]
        ),

        expand=True,
    )

    return ft.Column(
        [
            ft.Text(
                "Services",
                size=28,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Container(height=20),

            ft.Row(
                [
                    left_panel,
                    right_panel,
                ],

                expand=True,

                spacing=20,
            ),
        ],

        scroll=ft.ScrollMode.AUTO,

        expand=True,
    )