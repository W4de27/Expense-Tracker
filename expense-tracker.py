import os
import csv
import time
import datetime

# ================================
# COLORS + ICONS
# ================================
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

ICON_OK = "✔"
ICON_ERR = "✖"
ICON_INFO = "ℹ"
ICON_ADD = "➕"
ICON_LIST = "📄"
ICON_TOTAL = "📊"
ICON_EXIT = "🚪"


# ================================
# UI HELPERS
# ================================
def pause():
    input("\nPress Enter to continue...")

def success(msg):
    print(f"{GREEN}{ICON_OK} {msg}{RESET}")

def error(msg):
    print(f"{RED}{ICON_ERR} {msg}{RESET}")

def info(msg):
    print(f"{CYAN}{ICON_INFO} {msg}{RESET}")

def animate(text, repeats=3, delay=0.35):
    for i in range(repeats):
        dots = "." * ((i % 3) + 1)
        print(f"\r{text}{dots}", end="", flush=True)
        time.sleep(delay)
    print()


# ================================
# DATA (CSV)
# ================================
def ensure_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Amount", "Category", "Date"])


def add_expense(file_path):
    animate("Loading")

    try:
        amount = float(input("Enter amount ($): "))
        if amount <= 0:
            error("Amount must be greater than 0!")
            pause()
            return

        category = input("Enter category: ").strip().capitalize()
        if not category:
            error("Category cannot be empty!")
            pause()
            return
        if len(category) > 25:
            error("Category must be ≤ 25 characters!")
            pause()
            return

        date = datetime.date.today()

        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([amount, category, date])

        print()
        animate("Saving")
        success("Expense added successfully!")

    except ValueError:
        error("Invalid amount!")

    pause()


def read_expenses(file_path):
    with open(file_path, "r") as f:
        return list(csv.reader(f))[1:]  # skip header


def view_expenses(file_path):
    animate("Loading")

    rows = read_expenses(file_path)

    if not rows:
        error("No expenses found!")
        pause()
        return

    print("\n📄 ALL EXPENSES:\n")
    print(f"{'Amount ($)':<12} | {'Category':<20} | Date")
    print("-" * 50)

    for r in rows:
        print(f"{float(r[0]):<12.2f} | {r[1]:<20} | {r[2]}")
        time.sleep(0.15)

    print()
    success("Done!")
    pause()


def total_spending(file_path):
    animate("Calculating")

    rows = read_expenses(file_path)
    total = sum(float(r[0]) for r in rows) if rows else 0.0

    print()
    info(f"Your total spending: {GREEN}${total:.2f}{RESET}")
    pause()


def exit_program():
    for i in range(3):
        print("Exiting" + "." * (i + 1))
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
    print("🔶 Thank you for choosing our service. Stay prepared. 🏆 \n")


# ================================
# MAIN MENU
# ================================
def main():

    # ========== MY FOLDER DIRECTORY ===========
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "expenses.csv")
    # ==========================================

    ensure_file(file_path)

    while True:
        print()
        print("====================================")
        print("        💰 Expense Tracker")
        print("====================================\n")
        print(f"1. {ICON_ADD} Add Expense")
        print(f"2. {ICON_LIST} View Expenses")
        print(f"3. {ICON_TOTAL} Total Spending")
        print(f"4. {ICON_EXIT} Exit\n")
        print("====================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense(file_path)
        elif choice == "2":
            view_expenses(file_path)
        elif choice == "3":
            total_spending(file_path)
        elif choice == "4":
            exit_program()
            break
        else:
            error("Invalid choice!")
            time.sleep(1.5)


if __name__ == "__main__":
    try:
        # ===== Startup Animation =====
        for i in range(3):
            print(" Starting" + "." * (i + 1))
            time.sleep(0.8)
            os.system("cls" if os.name == "nt" else "clear")
        main()
    except KeyboardInterrupt:
        print("\n \n🔶 Thank you for choosing our service. Stay prepared. 🏆 \n")
