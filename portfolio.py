import csv
import os

FILENAME = "portfolio.csv"


def calculate_investment(buy_price, quantity):
    return buy_price * quantity


def calculate_current_value(current_price, quantity):
    return current_price * quantity


def calculate_gain_loss(invested, current_value):
    gain_loss = current_value - invested
    percentage = (gain_loss / invested) * 100 if invested > 0 else 0
    return gain_loss, percentage


def add_investment():
    try:
        ticker = input("\nEnter stock ticker: ").strip().upper()

        if not ticker:
            print("Ticker cannot be empty.")
            return

        buy_price = float(input("Enter buying price per share: "))
        quantity = int(input("Enter quantity: "))
        current_price = float(input("Enter current market price per share: "))

        if buy_price <= 0 or quantity <= 0 or current_price < 0:
            print("Please enter valid positive values.")
            return

        invested = calculate_investment(buy_price, quantity)
        current_value = calculate_current_value(current_price, quantity)
        gain_loss, percentage = calculate_gain_loss(
            invested, current_value
        )

        file_exists = os.path.exists(FILENAME)

        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(FILENAME) == 0:
                writer.writerow([
                    "Ticker", "Buy Price", "Quantity",
                    "Current Price", "Invested Value",
                    "Current Value", "Gain/Loss", "Percentage"
                ])

            writer.writerow([
                ticker, buy_price, quantity, current_price,
                invested, current_value, gain_loss, percentage
            ])

        print("\nInvestment saved successfully!")
        print(f"Total invested: ₹{invested:.2f}")
        print(f"Current value: ₹{current_value:.2f}")
        print(f"Gain/Loss: ₹{gain_loss:.2f}")
        print(f"Percentage: {percentage:.2f}%")

    except ValueError:
        print("Invalid input. Please enter numbers correctly.")


def view_portfolio():
    if not os.path.exists(FILENAME):
        print("\nNo investments recorded yet.")
        return

    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("\nYour portfolio is empty.")
        return

    print("\n========== YOUR PORTFOLIO ==========")

    for row in rows[1:]:
        print(f"\nTicker: {row[0]}")
        print(f"Buy Price: ₹{float(row[1]):.2f}")
        print(f"Quantity: {row[2]}")
        print(f"Current Price: ₹{float(row[3]):.2f}")
        print(f"Invested Value: ₹{float(row[4]):.2f}")
        print(f"Current Value: ₹{float(row[5]):.2f}")
        print(f"Gain/Loss: ₹{float(row[6]):.2f}")
        print(f"Percentage: {float(row[7]):.2f}%")


def main():
    while True:
        print("\n===== INVESTMENT PORTFOLIO TRACKER =====")
        print("1. Add Investment")
        print("2. View Portfolio")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_investment()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            print("Thank you for using Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()