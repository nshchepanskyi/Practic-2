import flet as ft


services_data = [
    {
        "name": "Breakfast",
        "price": "$10",
    },

    {
        "name": "Laundry",
        "price": "$15",
    },

    {
        "name": "Spa",
        "price": "$50",
    },

    {
        "name": "Airport Transfer",
        "price": "$25",
    },
]


def services_view(page):
    services_column = ft.Column()

    for service in services_data:
        services_column.controls.append(
            ft.Container(
                bgcolor="white",

                border_radius=18,

                padding=20,

                margin=5,

                content=ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    service["name"],
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Text(
                                    service["price"],
                                    color="grey",
                                ),
                            ]
                        ),

                        ft.ElevatedButton(
                            "Order",
                            icon=ft.Icons.ADD,
                        ),
                    ],

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            )
        )

    return ft.Column(
        [
            ft.Text(
                "Services",
                size=34,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Container(height=20),

            services_column,
        ],

        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )