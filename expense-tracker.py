import time, os, sys, datetime, csv

def animated_starting(word="Starting", repeats=3, delay=0.5):
    """
    Displays animated 'word', like:
    Starting.
    Starting..
    Starting...
    All in one line, updating dynamically.
    """
    for i in range(repeats):
        dots = '.' * ((i % 3) + 1)  # cycles through 1,2,3 dots
        print(f"\r{word}{dots}  ", end='', flush=True)  # end='' keeps it on same line
        time.sleep(delay)
    print()  # final newline after animation

def animated_loading(word="Loading", repeats=3, delay=0.5):
    """
    Displays animated 'word', like:
    Loading.
    Loading..
    Loading...
    All in one line, updating dynamically.
    """
    for i in range(repeats):
        dots = '.' * ((i % 3) + 1)  # cycles through 1,2,3 dots
        print(f"\r{word}{dots}  ", end='', flush=True)  # end='' keeps it on same line
        time.sleep(delay)
    print()  # final newline after animation

def animated_progress(word="In Progress", repeats=3, delay=0.5):
    """
    Displays animated 'word', like:
    In Progress.
    In Progress..
    In Progress...
    All in one line, updating dynamically.
    """
    for i in range(repeats):
        dots = '.' * ((i % 3) + 1)  # cycles through 1,2,3 dots
        print(f"\r{word}{dots}  ", end='', flush=True)  # end='' keeps it on same line
        time.sleep(delay)
    print()  # final newline after animation

def animated_exiting(word="Exiting", repeats=3, delay=0.5):
    """
    Displays animated 'word', like:
    Exiting.
    Exiting..
    Exiting...
    All in one line, updating dynamically.
    """
    for i in range(repeats):
        dots = '.' * ((i % 3) + 1)  # cycles through 1,2,3 dots
        print(f"\r{word}{dots}  ", end='', flush=True)  # end='' keeps it on same line
        time.sleep(delay)
    print()  # final newline after animation

def pause():
    print()
    input("Press Enter to continue...")
    time.sleep(1)

def error(msg):
    print()
    print(f"[x] {msg}")
    time.sleep(2)
    pause()


def add_expense(file_path):
    animated_loading("Loading", repeats=3, delay=0.5)
    print()

    try:

        amount = float(input("Enter amount: $"))
        if amount <= 0 :
            error("Amount should not be less than or equal 0!")
            return
        else:
            category = input("Enter category: ").strip().capitalize()
            if category == "":
                error("Category should not be empty!")
                return
            elif len(category) > 25:
                error("Maximum 25 characters!")
                return
            else:
                date = datetime.date.today()
                row = [amount, category, date]

                if os.path.exists(file_path):
                    with open(file_path, "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(row)
                else:
                    with open(file_path, "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(row)
                print()
                animated_progress("In Progress", repeats=3, delay=0.5)
                print("[OK] Expense Added Successfully!")
                time.sleep(2)
                
    except ValueError:
        print()
        print("ERROR! Invalid Expense!")
        time.sleep(2)

    print(f"Writing CSV file to: {file_path}")
    pause()


def view_expenses(file_path):
    animated_loading("Loading", repeats=3, delay=0.5)
    print()

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            rows = [row for row in csv.reader(file) if len(row) == 3]


            if len(rows) == 0:
                print("[!!] No expenses found. Your expense list is empty.")
                time.sleep(2)
                print()
            else:
                col1 = "Amount"
                col2 = "Category"
                col3 = "Date"

                print(f"{col1:<8} | {col2:<25} | {col3}")
                print("-------------------------------------------------")
                time.sleep(1)
                for row in rows:
                    print(f"{float(row[0]):<8.2f} | {row[1]:<25} | {row[2]}")
                    time.sleep(0.5)
                
                time.sleep(1)
                print()
                print("[OK] Done! All your expenses have been listed.")
                time.sleep(2)
            
    else:
        print("[!!] No expenses found. Your expense list is empty.")
        time.sleep(2)
        print()

    pause()


def total_spending(file_path):
    animated_loading("Loading", repeats=3, delay=0.5)
    print()

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            rows = [row for row in csv.reader(file) if len(row) == 3]

            if len(rows) == 0:
                print("Total Spending: $0.00")
                time.sleep(2)
            else:
                total = 0
                for row in rows:
                    total += float(row[0])
                
                print(f"Total Spending: ${total:.2f}")
                time.sleep(2)
    else:
        print("Total Spending: $0.00")
        time.sleep(2)

    pause() 



def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "expenses.csv")
    is_running = True

    while is_running:
        print()
        print("====== Expense Tracker ======")
        print()
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. Exit")
        print()
        print("=============================")

        choice = input("Enter Your Choice (1-4): ")

        if choice == "1":
            add_expense(file_path)
        elif choice == "2":
            view_expenses(file_path)
        elif choice == "3":
            total_spending(file_path)
        elif choice == "4":
            for i in range(3):
                print("Exiting" + "." * (i + 1))
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
            print("* Program closed successfully. Bye! * \n")
            is_running = False
        else:
            error("Invalid Choice!")


if __name__ == "__main__":
    try:
        for i in range(3):
            print(" Starting" + "." * (i + 1))
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
        main()
    except KeyboardInterrupt:
        print("\n \n * Program closed successfully. Bye! * \n")