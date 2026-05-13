# GrandStay Hotel Management System

A Python-based CLI application for managing hotel operations, including room management, guest bookings, service tracking, and financial reporting.

## Project Structure

```
grandstay_hotel/
├── views/
│   ├── dashboard.py     # Reports and analytics views
│   ├── reservations.py  # Guest and booking interaction logic
│   └── rooms.py         # Room management views
├── hotel_data.py        # Core data models and storage logic
├── main.py              # Application entry point
├── requirements.txt     # Dependency list (Standard Library only for now)
└── README.md            # Project documentation
```

## Features

1. **Room Management**: Add, remove, and track statuses of all hotel rooms.
2. **Reservation System**: Handle the full booking lifecycle (Pending -> Checked-In -> Checked-Out).
3. **Guest Management**: Maintain a searchable database of hotel guests and their contact info.
4. **Service Accounting**: Track additional service costs (Spa, Breakfast, etc.) per guest.
5. **Detailed Reports**: View revenue, occupancy rates, and guest activity summaries.

## How to Run

Navigate to the project directory and run:

```bash
python main.py
```

## Future Extensibility

This project is designed as a backend-first logic layer. All data processing functions in `hotel_data.py` return data structures instead of prints, making it easy to swap the current CLI views in the `views/` folder with a **Flet** GUI or a web interface in the future.
