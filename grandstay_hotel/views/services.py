import flet as ft

from hotel_data import (
    SERVICES_CATALOG,
    guests,
    service_orders,
    create_service_order,
    update_service_order_status,
)
from l10n import tr
from theme import get as C

STATUS_COLORS = {
    "Pending": (ft.Colors.YELLOW_100, ft.Colors.YELLOW_900),
    "In Progress": (ft.Colors.BLUE_100, ft.Colors.BLUE_900),
    "Completed": (ft.Colors.GREEN_100, ft.Colors.GREEN_900),
    "Cancelled": (ft.Colors.RED_100, ft.Colors.RED_900),
}

SERVICE_ICONS = {
    "Breakfast": ft.Icons.FREE_BREAKFAST,
    "Laundry": ft.Icons.LOCAL_LAUNDRY_SERVICE,
    "Spa": ft.Icons.SPA,
    "Airport Transfer": ft.Icons.AIRPORT_SHUTTLE,
    "Gym": ft.Icons.FITNESS_CENTER,
    "Pool": ft.Icons.POOL,
    "Parking": ft.Icons.LOCAL_PARKING,
    "Room Service": ft.Icons.ROOM_SERVICE,
    "Mini Bar": ft.Icons.LOCAL_BAR,
    "Dry Cleaning": ft.Icons.DRY_CLEANING,
    "Conference Room": ft.Icons.MEETING_ROOM,
    "Movie Rental": ft.Icons.MOVIE,
    "Bicycle Rental": ft.Icons.PEDAL_BIKE,
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

    selected_service = []

    guest_dropdown = ft.Dropdown(
        label=tr("Select Guest"),
        width=280,
        options=[],
        border_radius=10,
    )

    order_message = ft.Text(
        size=13
    )

    selected_label = ft.Text(
        tr("No services selected"),
        size=13,
        color=C("text_secondary"),
        italic=True,
    )

    def update_selected_label():
        count = len(selected_service)
        if count == 0:
            selected_label.value = tr("No services selected")
            selected_label.color = C("text_secondary")
        else:
            key = "{count} services selected" if count != 1 else "{count} service selected"
            selected_label.value = tr(key, count=count)
            selected_label.color = C("accent")

    orders_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text(tr("Order ID"))),
            ft.DataColumn(ft.Text(tr("Guest"))),
            ft.DataColumn(ft.Text(tr("Service"))),
            ft.DataColumn(ft.Text(tr("Qty"))),
            ft.DataColumn(ft.Text(tr("Total"))),
            ft.DataColumn(ft.Text(tr("Time"))),
            ft.DataColumn(ft.Text(tr("Status"))),
            ft.DataColumn(ft.Text(tr("Update"))),
        ],

        rows=[],
    )





    def refresh_guests():

        guest_dropdown.options = [
            ft.dropdown.Option(
                key=g.guest_id,
                text=f"{g.name} ({g.guest_id})",
            )
            for g in guests
        ]





    def change_status(order_id, status):

        update_service_order_status(
            order_id,
            status,
        )

        refresh_orders()





    def refresh_orders():

        orders_table.rows.clear()

        for order in service_orders:

            bg, fg = STATUS_COLORS.get(
                order.status,
                (ft.Colors.BLUE_GREY_100, ft.Colors.BLUE_GREY_700),
            )

            status_dropdown = ft.Dropdown(
                width=140,

                value=order.status,

                options=[
                    ft.dropdown.Option(text=tr("Pending"), key="Pending"),
                    ft.dropdown.Option(text=tr("In Progress"), key="In Progress"),
                    ft.dropdown.Option(text=tr("Completed"), key="Completed"),
                    ft.dropdown.Option(text=tr("Cancelled"), key="Cancelled"),
                ],
            )

            save_button = ft.ElevatedButton(
                tr("Save"),

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
                            ft.Text(tr(order.service_name))
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
                                    tr(order.status),
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





    def make_service_card(svc):

        localized_name = tr(svc["name"])

        icon = SERVICE_ICONS.get(
            svc["name"],
            ft.Icons.ROOM_SERVICE,
        )

        qty_field = ft.TextField(
            value="1",
            width=55,
            height=40,
            border_radius=8,
            text_align=ft.TextAlign.CENTER,
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        card = ft.Container(
            border_radius=12,

            bgcolor=C("surface"),

            padding=14,

            margin=ft.Margin(
                left=0,
                top=0,
                right=0,
                bottom=8,
            ),

            border=_make_border(C("border")),
        )

        def select_service(
            e,
            s=svc,
            c=card,
            q=qty_field,
        ):

            idx = next(
                (i for i, entry in enumerate(selected_service) if entry[0] is s),
                None,
            )

            if idx is not None:
                selected_service.pop(idx)
                c.border = _make_border(C("border"))
                c.bgcolor = ft.Colors.WHITE
            else:
                selected_service.append((s, c, q))
                c.border = _make_border(C("accent"))
                c.bgcolor = ft.Colors.BLUE_50

            update_selected_label()
            page.update()

        card.on_click = select_service

        card.content = ft.Row(
            [
                ft.Icon(
                    icon,
                    color=C("accent"),
                    size=28,
                ),

                ft.Column(
                    [
                        ft.Text(
                            localized_name,
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Text(
                            f"${svc['price']}",
                            color=C("text_secondary"),
                        ),
                    ],

                    spacing=2,
                    expand=True,
                ),

                qty_field,
            ],

            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        return card

    service_cards = [
        make_service_card(s)
        for s in SERVICES_CATALOG
    ]





    def place_order(e):

        if not selected_service:

            order_message.value = tr(
                "Select at least one service"
            )

            order_message.color = "red"

            page.update()

            return

        if not guest_dropdown.value:

            order_message.value = tr(
                "Select guest"
            )

            order_message.color = "red"

            page.update()

            return

        qtys = []

        for svc, _, qty_field in selected_service:

            try:

                qty = int(qty_field.value)

                if qty < 1:
                    raise ValueError

                qtys.append(qty)

            except Exception:

                order_message.value = tr(
                    "Invalid quantity for {name}", name=tr(svc["name"])
                )

                order_message.color = "red"

                page.update()

                return

        created = 0

        for (svc, _, qty_field), qty in zip(selected_service, qtys):

            ok, _ = create_service_order(
                guest_id=guest_dropdown.value,

                service_name=svc["name"],

                service_price=svc["price"],

                quantity=qty,
            )

            if ok:
                created += 1

        if created > 0:

            key = "{count} orders created" if created != 1 else "{count} order created"
            order_message.value = tr(key, count=created)

            order_message.color = "green"

            guest_dropdown.value = None

            for _, card, qty_field in selected_service:
                card.border = _make_border(C("border"))
                card.bgcolor = "white"
                qty_field.value = "1"

            selected_service.clear()

            update_selected_label()

            refresh_orders()

        else:

            order_message.value = tr("Failed to create orders")

            order_message.color = "red"

        page.update()

    refresh_guests()

    refresh_orders()





    def panel(
        content,
        width=None,
        expand=False,
    ):

        return ft.Container(
            width=width,

            expand=expand,

            bgcolor=C("surface"),

            border_radius=14,

            padding=22,

            border=_make_border(C("border")),

            content=content,
        )

    left_panel = panel(
        ft.Column(
            [
                ft.Text(
                    tr("Service Catalog"),
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

                order_message,

                ft.ElevatedButton(
                    tr("Place Order"),

                    icon=ft.Icons.SHOPPING_CART,

                    bgcolor=C("accent"),

                    color=ft.Colors.WHITE,

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
                    tr("Service Orders"),
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
                tr("Services"),
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