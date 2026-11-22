# ==========================================
# SECTION 1 - IMPORTS AND DATA SETUP
# ==========================================

import csv
from pathlib import Path
from datetime import datetime

# Save CSV files in the same folder as this script
FOLDER = Path(__file__).resolve().parent

BIKE_FILE = FOLDER / "motorcycle.csv"
MAINTENANCE_FILE = FOLDER / "maintenance.csv"
EXPENSE_FILE = FOLDER / "expenses.csv"

BIKE_FIELDS = ["year", "make", "model", "mileage"]
MAINTENANCE_FIELDS = [
    "date", "service", "mileage", "cost", "next_service_mileage"
]
EXPENSE_FIELDS = ["date", "description", "category", "amount"]

# Information stored while the program runs
bike = {}
maintenance = []
expenses = []

# ==========================================
# SECTION 2 - FILES AND USER INPUT
# ==========================================

def load_csv(filename, fields):
    if not filename.exists():
        return []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or not all(
                field in reader.fieldnames for field in fields
            ):
                print("Missing columns in", filename.name)
                return []

            return list(reader)

    except (OSError, csv.Error) as error:
        print("Could not load file:", error)
        return []


def save_csv(filename, fields, records):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(records)
        return True

    except (OSError, csv.Error) as error:
        print("Could not save file:", error)
        return False


def ask_number(question, whole=False):
    while True:
        try:
            answer = input(question).strip()

            if whole:
                number = int(answer)
            else:
                number = float(answer)

            if number < 0 or (
                not whole and number != number
            ) or (
                not whole and number == float("inf")
            ):
                print("Enter a valid number that is zero or greater.")
                continue

            return number

        except ValueError:
            print("That is not a valid number. Try again.")


def ask_date():
    while True:
        date = input(
            "Date (YYYY-MM-DD or Enter for today): "
        ).strip()

        if date == "":
            return datetime.today().strftime("%Y-%m-%d")

        try:
            return datetime.strptime(
                date, "%Y-%m-%d"
            ).strftime("%Y-%m-%d")

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")


# ==========================================
# SECTION 3 - MOTORCYCLE INFORMATION
# ==========================================

def add_motorcycle():
    print("\n--- Add Motorcycle Information ---")

    year = ask_number("Year: ", True)
    make = input("Make: ").strip()
    model = input("Model: ").strip()
    mileage = ask_number("Current mileage: ", True)

    if year < 1885 or make == "" or model == "":
        print("Please enter valid motorcycle information.")
        return

    new_bike = {
        "year": year,
        "make": make,
        "model": model,
        "mileage": mileage
    }

    if save_csv(BIKE_FILE, BIKE_FIELDS, [new_bike]):
        bike.clear()
        bike.update(new_bike)
        print("Motorcycle saved successfully!")


def update_mileage():
    if not bike:
        print("Add a motorcycle first.")
        return

    print("\nCurrent mileage:", bike["mileage"])

    new_mileage = ask_number("New mileage: ", True)

    if new_mileage < int(bike["mileage"]):
        print("Mileage cannot go backwards.")
        return

    updated_bike = dict(bike)
    updated_bike["mileage"] = new_mileage

    if save_csv(BIKE_FILE, BIKE_FIELDS, [updated_bike]):
        bike.update(updated_bike)
        print("Mileage updated!")
        check_maintenance()

# ==========================================
# SECTION 4 - MAINTENANCE TRACKING
# ==========================================

def add_maintenance():
    if not bike:
        print("Add a motorcycle first.")
        return

    print("\n--- Add Maintenance Record ---")

    service = input("Service performed: ").strip()

    if service == "":
        print("Service cannot be blank.")
        return

    date = ask_date()
    mileage = ask_number("Mileage at service: ", True)

    if mileage > int(bike["mileage"]):
        print("Service mileage cannot exceed current mileage.")
        return

    cost = ask_number("Service cost: $")

    interval = ask_number(
        "Miles until next service (0 if none): ", True
    )

    if interval > 0:
        next_service = mileage + interval
    else:
        next_service = ""

    record = {
        "date": date,
        "service": service,
        "mileage": mileage,
        "cost": f"{cost:.2f}",
        "next_service_mileage": next_service
    }

    updated_records = maintenance + [record]

    if save_csv(MAINTENANCE_FILE, MAINTENANCE_FIELDS, updated_records):
        maintenance.append(record)
        print("Maintenance saved!")

        if next_service != "":
            print("Next service due at", next_service, "miles.")


def view_maintenance():
    print("\n--- Maintenance History ---")

    if not maintenance:
        print("No maintenance records found.")
        return

    for number, record in enumerate(maintenance, 1):
        print("\nRecord", number)
        print("Date:", record["date"])
        print("Service:", record["service"])
        print("Mileage:", record["mileage"])
        print("Cost: $" + record["cost"])

        if record["next_service_mileage"] != "":
            print("Next due:", record["next_service_mileage"], "miles")


def check_maintenance():
    print("\n--- Upcoming Maintenance ---")

    if not bike:
        print("Add a motorcycle first.")
        return

    current_mileage = int(bike["mileage"])
    latest_services = {}

    for record in maintenance:
        service_name = record["service"].strip().lower()

        if service_name not in latest_services:
            latest_services[service_name] = record

        elif int(record["mileage"]) >= int(
            latest_services[service_name]["mileage"]
        ):
            latest_services[service_name] = record

    scheduled = [
        record for record in latest_services.values()
        if record["next_service_mileage"] != ""
    ]

    if not scheduled:
        print("No scheduled maintenance found.")
        return

    for record in scheduled:
        due = int(record["next_service_mileage"])
        remaining = due - current_mileage

        print("\nService:", record["service"])
        print("Due at:", due, "miles")

        if remaining < 0:
            print("OVERDUE by", abs(remaining), "miles!")

        elif remaining == 0:
            print("Maintenance is DUE NOW!")

        elif remaining <= 500:
            print("COMING UP:", remaining, "miles remaining.")

        else:
            print(remaining, "miles remaining.")

# ==========================================
# SECTION 5 - EXPENSE TRACKING
# ==========================================

def record_expense():
    print("\n--- Record Riding Expense ---")

    description = input("What did you buy? ").strip()

    if description == "":
        print("Description cannot be blank.")
        return

    date = ask_date()

    category = input(
        "Category (fuel, parts, accessories, other): "
    ).strip()

    if category == "":
        category = "other"

    amount = ask_number("Amount spent: $")

    record = {
        "date": date,
        "description": description,
        "category": category,
        "amount": f"{amount:.2f}"
    }

    updated_expenses = expenses + [record]

    if save_csv(EXPENSE_FILE, EXPENSE_FIELDS, updated_expenses):
        expenses.append(record)
        print("Expense saved!")


def calculate_expenses():
    print("\n--- Total Motorcycle Expenses ---")

    maintenance_total = 0
    riding_total = 0

    for record in maintenance:
        maintenance_total += float(record["cost"])

    for record in expenses:
        riding_total += float(record["amount"])

    total = maintenance_total + riding_total

    print(f"Maintenance: ${maintenance_total:.2f}")
    print(f"Other expenses: ${riding_total:.2f}")
    print(f"Total spent: ${total:.2f}")

    print("Do not record the same purchase twice.")

# ==========================================
# SECTION 6 - SAVE INFORMATION
# ==========================================

def save_all():
    success = True

    if bike:
        if not save_csv(BIKE_FILE, BIKE_FIELDS, [bike]):
            success = False

    if not save_csv(
        MAINTENANCE_FILE, MAINTENANCE_FIELDS, maintenance
    ):
        success = False

    if not save_csv(
        EXPENSE_FILE, EXPENSE_FIELDS, expenses
    ):
        success = False

    if success:
        print("All information saved successfully!")
    else:
        print("Some information could not be saved.")

# ==========================================
# SECTION 7 - MAIN MENU
# ==========================================

def show_menu():
    print("\n====================================")
    print(" MOTORCYCLE MAINTENANCE & RIDE TRACKER")
    print("====================================")

    if bike:
        print(
            "Bike:",
            bike["year"],
            bike["make"],
            bike["model"]
        )
        print("Mileage:", bike["mileage"])

    print("\n1. Add Motorcycle Information")
    print("2. Update Motorcycle Mileage")
    print("3. Add Maintenance Record")
    print("4. View Maintenance History")
    print("5. Check Upcoming Maintenance")
    print("6. Record Riding Expenses")
    print("7. Calculate Total Expenses")
    print("8. Save Information")
    print("9. Exit")


def main():
    print("Welcome to Motorcycle Tracker!")

    while True:
        show_menu()

        choice = input("\nChoose an option (1-9): ").strip()

        if choice == "1":
            add_motorcycle()

        elif choice == "2":
            update_mileage()

        elif choice == "3":
            add_maintenance()

        elif choice == "4":
            view_maintenance()

        elif choice == "5":
            check_maintenance()

        elif choice == "6":
            record_expense()

        elif choice == "7":
            calculate_expenses()

        elif choice == "8":
            save_all()

        elif choice == "9":
            save_all()
            print("Thanks for using Motorcycle Tracker!")
            break

        else:
            print("Invalid option. Choose 1-9.")

# ==========================================
# SECTION 8 - START THE PROGRAM
# ==========================================

def load_all():
    global bike, maintenance, expenses

    saved_bikes = load_csv(BIKE_FILE, BIKE_FIELDS)

    if saved_bikes:
        bike = saved_bikes[0]
    else:
        bike = {}

    maintenance = load_csv(
        MAINTENANCE_FILE, MAINTENANCE_FIELDS
    )

    expenses = load_csv(
        EXPENSE_FILE, EXPENSE_FIELDS
    )


if __name__ == "__main__":
    load_all()
    main()