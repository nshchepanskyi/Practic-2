GrandStay Hotel Management System

A Flet-based desktop application for managing hotel operations, including room management, guest bookings, service tracking, multi-language support, and dark/light theme.

Project Structure

```
grandstay_hotel/
├── components/
│   ├── topbar.py          # App bar with theme & language toggles
│   ├── navbar.py          # Side navigation
│   ├── room_card.py       # Room status card widget
│   ├── stat_card.py       # KPI stat card widget
│   └── activity_card.py   # Activity timeline card
├── views/
│   ├── dashboard.py       # Main dashboard with KPIs & tables
│   ├── reservations.py    # Reservation CRUD & booking forms
│   ├── rooms.py           # Room management (add/remove/status)
│   ├── services.py        # Multi-service ordering with quantities
│   ├── guests.py          # Guest directory
│   ├── login.py           # Authentication login
│   └── register.py        # User registration
├── storage/               # JSON data files (rooms, reservations, guests, etc.)
├── hotel_data.py          # Core data models, storage logic, business logic
├── l10n.py                # Localization (EN/UK) with tr() function
├── theme.py               # Dark/light color palettes via ft.Colors
├── auth.py                # Simple password-based authentication
├── main.py                # Application entry point
└── users.json             # User credentials storage
```

Features

1. Room Management: Add, remove, and track statuses (Available, Occupied, Cleaning, Maintenance).
2. Reservation System: Full booking lifecycle (Pending -> Checked-In -> Checked-Out) with calendar date picker.
3. Guest Management: Searchable database of hotel guests and their contact info.
4. Service Accounting: Multi-select service ordering with per-item quantities (Spa, Breakfast, Gym, Pool, Parking, Room Service, Mini Bar, Dry Cleaning, Conference Room, Movie Rental, Bicycle Rental).
5. Dashboard: KPI cards (occupancy, revenue, arrivals), recent reservations table, room status grid, services revenue summary.
6. Dark/Light Theme: Toggle via button in top bar, persistent color scheme using ft.Colors constants.
7. Language Toggle: Switch between English and Ukrainian, all UI strings translated via tr().
8. Authentication: Login/register with password protection.

How to Run

```bash
pip install flet
python grandstay_hotel/main.py
```

Storage

All data is persisted to JSON files in grandstay_hotel/storage/:
- rooms.json, reservations.json, guests.json, service_orders.json, notifications.json, users.json
