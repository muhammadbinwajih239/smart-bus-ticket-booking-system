# Smart Bus Ticket Booking and Reservation System
# Python 3 - Built-in functionality only

# --------------------------------------------------
# 1. ROUTE DATA
# --------------------------------------------------

routes = [
    {
        "route_id": "R101",
        "departure_city": "Karachi",
        "destination_city": "Hyderabad",
        "departure_time": "08:00 AM",
        "ticket_price": 1200,
        "total_seats": 40,
        "available_seats": 40
    },
    {
        "route_id": "R102",
        "departure_city": "Karachi",
        "destination_city": "Sukkur",
        "departure_time": "09:30 AM",
        "ticket_price": 2000,
        "total_seats": 36,
        "available_seats": 36
    },
    {
        "route_id": "R103",
        "departure_city": "Hyderabad",
        "destination_city": "Mirpur Khas",
        "departure_time": "11:00 AM",
        "ticket_price": 800,
        "total_seats": 32,
        "available_seats": 32
    },
    {
        "route_id": "R104",
        "departure_city": "Karachi",
        "destination_city": "Lahore",
        "departure_time": "07:00 PM",
        "ticket_price": 5000,
        "total_seats": 45,
        "available_seats": 45
    },
    {
        "route_id": "R105",
        "departure_city": "Sukkur",
        "destination_city": "Hyderabad",
        "departure_time": "02:00 PM",
        "ticket_price": 1500,
        "total_seats": 30,
        "available_seats": 30
    }
]

# Tuple: cities supported by the system
supported_cities = (
    "Karachi",
    "Hyderabad",
    "Sukkur",
    "Mirpur Khas",
    "Lahore"
)

# List: stores all booking records
bookings = []

# Set: prevents duplicate booking IDs
issued_booking_ids = set()

# Booking IDs start from B1001
next_booking_number = 1001


# --------------------------------------------------
# 2. ROUTE HELPER FUNCTIONS
# --------------------------------------------------

def get_route_status(route):
    if route["available_seats"] == 0:
        return "Fully Booked"

    elif route["available_seats"] == route["total_seats"]:
        return "Available"

    else:
        return "Partially Booked"


def find_route_by_id(route_id):
    for route in routes:
        if route["route_id"].lower() == route_id.lower():
            return route
    else:
        return None


def show_route_details(route, number=None):
    prefix = f"{number}. " if number is not None else ""

    print(
        f"{prefix}{route['route_id']} | "
        f"{route['departure_city']} -> "
        f"{route['destination_city']} | "
        f"Depart: {route['departure_time']} | "
        f"Fare: Rs. {route['ticket_price']} | "
        f"Seats: {route['available_seats']}/"
        f"{route['total_seats']} | "
        f"Status: {get_route_status(route)}"
    )


# --------------------------------------------------
# 3. VIEW AVAILABLE ROUTES
# --------------------------------------------------

def view_routes():
    choice = input(
        "Show only routes with available seats? (y/n): "
    ).strip().lower()

    available_only = choice == "y"
    shown = 0

    print("\nAVAILABLE BUS ROUTES")
    print("-" * 70)

    for number, route in enumerate(routes, start=1):

        # Skip fully booked routes when filtering
        if available_only and route["available_seats"] == 0:
            continue

        show_route_details(route, number)
        shown += 1

    if shown == 0:
        print("No routes match your filter.")


# --------------------------------------------------
# 4. SEARCH ROUTES
# --------------------------------------------------

def search_route():
    query = input(
        "Enter route ID or departure/destination city: "
    ).strip()

    if not query:
        print("Search input cannot be empty.")
        return

    matched = False

    for route in routes:

        # Exact route ID search
        if query.lower() == route["route_id"].lower():
            show_route_details(route)
            matched = True
            break

        # Partial, case-insensitive city search
        elif (
            query.lower() in route["departure_city"].lower()
            or query.lower() in route["destination_city"].lower()
        ):
            show_route_details(route)
            matched = True

    else:
        if not matched:
            print("No matching routes found.")


# --------------------------------------------------
# 5. BOOK A TICKET
# --------------------------------------------------

def book_ticket():
    global next_booking_number

    passenger_name = input("Enter passenger name: ").strip()

    if not passenger_name:
        print("Passenger name cannot be empty.")
        return

    age_input = input("Enter passenger age: ").strip()

    try:
        passenger_age = int(age_input)
    except ValueError:
        print("Age must be a positive integer.")
        return

    if passenger_age <= 0:
        print("Age must be greater than zero.")
        return

    route_id = input("Enter route ID: ").strip().upper()

    route = find_route_by_id(route_id)

    if route is None:
        print("Invalid route ID.")
        return

    seats_input = input("Enter number of seats: ").strip()

    try:
        seats = int(seats_input)
    except ValueError:
        print("Seat quantity must be an integer.")
        return

    if seats <= 0:
        print("Seat quantity must be greater than zero.")
        return

    if seats > route["available_seats"]:
        print(
            f"Not enough seats available. "
            f"Only {route['available_seats']} seats remain."
        )
        return

    # Generate a unique booking ID
    while f"B{next_booking_number}" in issued_booking_ids:
        next_booking_number += 1

    booking_id = f"B{next_booking_number}"
    next_booking_number += 1

    # Calculate total fare
    total_fare = route["ticket_price"] * seats

    # Create the booking record
    booking = {
        "booking_id": booking_id,
        "passenger_name": passenger_name,
        "passenger_age": passenger_age,
        "route_id": route["route_id"],
        "seats": seats,
        "total_fare": total_fare,
        "status": "Confirmed"
    }

    # Save booking and update seat availability
    bookings.append(booking)
    issued_booking_ids.add(booking_id)
    route["available_seats"] -= seats

    print("\nBOOKING CONFIRMED!")
    print(f"Booking ID: {booking_id}")
    print(f"Passenger: {passenger_name}")
    print(f"Age: {passenger_age}")
    print(
        f"Route: {route['departure_city']} -> "
        f"{route['destination_city']}"
    )
    print(f"Seats booked: {seats}")
    print(f"Fare per seat: Rs. {route['ticket_price']}")
    print(f"Total fare: Rs. {total_fare}")
    print(f"Status: {booking['status']}")


# --------------------------------------------------
# 6. VIEW ALL BOOKINGS
# --------------------------------------------------

def view_bookings():
    if not bookings:
        print("No bookings found.")
        return

    print("\nBOOKING HISTORY")
    print("-" * 50)

    for number, booking in enumerate(bookings, start=1):
        route = find_route_by_id(booking["route_id"])

        if route is not None:
            journey = (
                f"{route['departure_city']} -> "
                f"{route['destination_city']}"
            )
        else:
            journey = "Route unavailable"

        print(f"\nBooking #{number}")
        print(f"Booking ID: {booking['booking_id']}")
        print(f"Passenger: {booking['passenger_name']}")
        print(f"Age: {booking['passenger_age']}")
        print(f"Route: {journey}")
        print(f"Seats: {booking['seats']}")
        print(f"Total fare: Rs. {booking['total_fare']}")
        print(f"Status: {booking['status']}")


# --------------------------------------------------
# 7. CANCEL A BOOKING
# --------------------------------------------------

def cancel_booking():
    booking_id = input(
        "Enter booking ID to cancel: "
    ).strip().upper()

    if not booking_id:
        print("Booking ID cannot be empty.")
        return

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            # Prevent cancelling the same booking twice
            if booking["status"] != "Confirmed":
                print("This booking has already been cancelled.")
                return

            route = find_route_by_id(booking["route_id"])

            if route is None:
                print("The associated route could not be found.")
                return

            # Restore seats and change the booking status
            route["available_seats"] += booking["seats"]
            booking["status"] = "Cancelled"

            print(f"Booking {booking_id} has been cancelled.")
            print(f"Seats restored: {booking['seats']}")
            print(
                f"Available seats on route "
                f"{route['route_id']}: "
                f"{route['available_seats']}"
            )
            return

    else:
        print("Booking ID not found.")


# --------------------------------------------------
# 8. VIEW SEAT AVAILABILITY
# --------------------------------------------------

def view_seat_availability():
    choice = input(
        "Show only routes with available seats? (y/n): "
    ).strip().lower()

    available_only = choice == "y"
    shown = 0

    print("\nSEAT AVAILABILITY")
    print("-" * 50)

    for number, route in enumerate(routes, start=1):

        if available_only and route["available_seats"] == 0:
            continue

        print(
            f"{number}. {route['route_id']} | "
            f"Available: {route['available_seats']} | "
            f"Total: {route['total_seats']} | "
            f"{get_route_status(route)}"
        )

        shown += 1

    if shown == 0:
        print("No routes match the selected filter.")


# --------------------------------------------------
# 9. GENERATE BOOKING REPORT
# --------------------------------------------------

def generate_booking_report():
    total_bookings = len(bookings)
    confirmed_bookings = 0
    cancelled_bookings = 0

    reserved_seats = 0
    confirmed_revenue = 0
    fully_booked_routes = 0

    # Count booking statuses
    for booking in bookings:
        if booking["status"] == "Confirmed":
            confirmed_bookings += 1

        elif booking["status"] == "Cancelled":
            cancelled_bookings += 1

    # Nested loops: calculate confirmed seats and revenue
    # route by route
    for route in routes:

        if route["available_seats"] == 0:
            fully_booked_routes += 1

        for booking in bookings:

            if (
                booking["route_id"] == route["route_id"]
                and booking["status"] == "Confirmed"
            ):
                reserved_seats += booking["seats"]
                confirmed_revenue += booking["total_fare"]

    print("\nBOOKING REPORT")
    print("-" * 40)
    print(f"Total bookings created: {total_bookings}")
    print(f"Confirmed bookings: {confirmed_bookings}")
    print(f"Cancelled bookings: {cancelled_bookings}")
    print(f"Seats currently reserved: {reserved_seats}")
    print(f"Confirmed revenue: Rs. {confirmed_revenue}")
    print(f"Fully booked routes: {fully_booked_routes}")


# --------------------------------------------------
# 10. ROUTE SCHEDULE BY DEPARTURE CITY
# --------------------------------------------------

def show_route_schedule():
    print("\nROUTE SCHEDULE BY DEPARTURE CITY")
    print("-" * 40)

    # Outer loop: visit every supported city
    for city in supported_cities:
        print(f"\n{city}")
        found = False

        # Inner loop: find routes departing from this city
        for route in routes:

            if route["departure_city"].lower() == city.lower():
                print(
                    f"  {route['route_id']} -> "
                    f"{route['destination_city']} | "
                    f"{route['departure_time']}"
                )
                found = True

        if not found:
            print("  No scheduled departures.")


# --------------------------------------------------
# 11. MAIN MENU
# --------------------------------------------------

def main():
    while True:
        print("\n" + "=" * 40)
        print("SMART BUS RESERVATION SYSTEM")
        print("=" * 40)
        print("1. View Available Routes")
        print("2. Search for a Route")
        print("3. Book a Ticket")
        print("4. View My Bookings")
        print("5. Cancel a Booking")
        print("6. View Seat Availability")
        print("7. Generate Booking Report")
        print("8. View Route Schedule")
        print("9. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_routes()

        elif choice == "2":
            search_route()

        elif choice == "3":
            book_ticket()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            cancel_booking()

        elif choice == "6":
            view_seat_availability()

        elif choice == "7":
            generate_booking_report()

        elif choice == "8":
            show_route_schedule()

        elif choice == "9":
            print("Thank you for using Smart Bus Reservation System.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 9.")


# Run the program
if __name__ == "__main__":
    main()