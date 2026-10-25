# Smart Bus Ticket Booking and Reservation System

## 1. Project Overview

The Smart Bus Ticket Booking and Reservation System is a beginner-friendly, text-based Python 3 console application. It manages fictional bus routes, passenger bookings, cancellations, seat availability, route schedules, and booking reports.

## 2. Features

- View the five sample bus routes.
- Search for a route by route ID or city name.
- Book tickets after validating passenger details, route ID, seat quantity, and availability.
- Generate a unique booking ID for each successful booking.
- View booking history, including cancelled bookings.
- Cancel a confirmed booking and restore its seats exactly once.
- View seat availability and route status.
- Generate booking and confirmed-revenue reports.
- View route schedules grouped by departure city.
- Handle invalid menu choices and invalid booking inputs.

## 3. Requirements

- Python 3
- No third-party Python packages are required.
- A terminal or command prompt to run the application.

## 4. Project Files

```text
Smart_Bus_Project/
├── main.py
├── README.md
├── test_cases.txt
└── screenshots/
    ├── 01_routes.png
    ├── 02_successful_booking.png
    ├── 03_cancellation.png
    └── 04_booking_report.png
```

## 5. How to Run

1. Place `main.py`, `README.md`, and `test_cases.txt` in the same project folder.
2. Open a terminal in that folder.
3. Run one of these commands:

```bash
python main.py
```

If the `python` command is not recognized on Windows, try:

```bash
py main.py
```

## 6. Main Menu

The current implementation uses this menu:

1. View Available Routes
2. Search for a Route
3. Book a Ticket
4. View My Bookings
5. Cancel a Booking
6. View Seat Availability
7. Generate Booking Report
8. View Route Schedule
9. Exit

The route schedule is included as a required feature, so it has its own menu option and Exit is option 9.

## 7. Sample Workflow

1. Select **3. Book a Ticket**.
2. Enter passenger name `Ahmed`.
3. Enter age `24`.
4. Enter route ID `R101`.
5. Enter `2` seats.
6. In a fresh run, the first booking should normally receive ID `B1001`.
7. Route `R101` fare is Rs. 1,200 per seat, so two seats cost Rs. 2,400.
8. The available seats on `R101` should decrease from 40 to 38.
9. Select **5. Cancel a Booking** and enter `B1001`.
10. The booking status should become `Cancelled` and the route's available seats should return to 40.
11. Generate the report. The cancelled booking should remain in the history but should not count toward confirmed revenue.

## 8. Data Structures and Python Concepts

- **List:** stores route dictionaries and booking dictionaries.
- **Dictionary:** stores named fields for a route or booking.
- **Tuple:** stores the supported cities.
- **Set:** tracks issued booking IDs.
- **Loops and conditions:** process routes, bookings, schedules, reports, and validation.
- **`enumerate()`:** numbers displayed records.
- **`for-else`:** handles searches where no match is found.
- **Nested loops:** build city schedules and calculate report totals by route.

## 9. Validation and Business Rules

- Passenger name cannot be empty or whitespace only.
- Age must be a positive integer.
- The selected route must exist.
- Seat quantity must be a positive integer and cannot exceed availability.
- A failed booking must not create a confirmed record or change seat counts.
- Only a confirmed booking can be cancelled.
- Cancelling the same booking more than once must not restore seats again.
- Cancelled booking records remain visible in history.
- Confirmed revenue and currently reserved seats include confirmed bookings only.
- Available seats must remain between zero and the route's total capacity.

## 10. Storage Limitation

Routes and bookings are stored in memory while the program runs. When the program closes, booking changes are lost and the sample route data resets on the next run. Permanent storage, databases, online payments, APIs, and graphical interfaces are outside the required project scope.

## 11. Testing

Run all test scenarios listed in `test_cases.txt`. Fill in the actual result and mark each test PASS or FAIL only after checking the program output and resulting data. Use a fresh program run for tests that require an empty booking list.
