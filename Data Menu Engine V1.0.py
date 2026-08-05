# AIRTIME BALANCE HANDLING FUNCTIONS
def load_balance():
    try:
        with open("balance.txt", "r") as file:
            return float(file.read())
    except FileNotFoundError:
        with open("balance.txt", "w") as file:
            file.write("2000")
        return 2000.0

airtime_balance = load_balance()

def save_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))

def save_history(plan, price):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"Purchased {plan} - N{price}\n")

def show_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            print("\n=== PURCHASE HISTORY ===")
            for purchase in file:
                print(purchase.strip())
    except FileNotFoundError:
        print("No purchase history found.\n")

# MENU FUNCTIONS
def show_menu():
    print("=== DATA MENU ENGINE ===")
    print("1. Daily Plans")
    print("2. Weekly Plans")
    print("3. Monthly Plans")
    print("4. Check Balance")
    print("5. View Purchase History")
    print("6. Exit")

# DAILY MENU
def show_daily_menu():
    print("-- Daily Plans --")
    print("1. 1GB = N500")
    print("2. 2GB = N750")

# WEEKLY MENU
def show_weekly_menu():
    print("-- Weekly Plans --")
    print("1. 2.5GB = N1000")
    print("2. 3GB = N1500")

# MONTHLY MENU
def show_monthly_menu():
    print("-- Monthly Plans --")
    print("1. 5GB = N2000")
    print("2. 10GB = N3000")

# CHECK BALANCE
def check_balance(balance):
    print(f"Balance: ₦{balance:.2f}")

def deduct_balance(balance, amount):
    return balance - amount

def transaction_success(plan, balance):
    print("Transaction Successful!")
    print(f"You have successfully purchased {plan}.")
    print(f"Remaining Balance: ₦{balance:.2f}")

def buy_plan(balance, plan, price):
    if balance >= price:
        balance = deduct_balance(balance, price)
        save_balance(balance)
        save_history(plan, price)
        transaction_success(plan, balance)
    else:
        print("Insufficient Balance")
    return balance

# PURCHASING FUNCTION
def purchase_plan(balance, plan_type, user_choice):
    selected_plan = plans.get(plan_type)
    if selected_plan:
        plan = selected_plan.get(user_choice)
        if plan:
            return buy_plan(
                balance,
                plan["plan"],
                plan["price"]
            )
        print("Invalid plan selected")
    return balance

# PLANS
plans = {"daily_plans": {1: {"plan": "1GB", "price": 500}, 2: {"plan": "2GB", "price": 750}},
         "weekly_plans": {1: {"plan": "2.5GB", "price": 1000}, 2: {"plan": "3GB", "price": 1500}},
         "monthly_plans": {1: {"plan": "5GB", "price": 2000}, 2: {"plan": "10GB", "price": 3000}}
         }

# MENU SYSTEMS TO PERFORMS ALL FUNCTIONS
while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!, please enter a valid number")
            continue
        if choice == 1:
            show_daily_menu()
            try:
                daily_choice = int(input("Select a plan: "))
            except ValueError:
                print("Invalid input!, please enter a valid number")
                continue
            airtime_balance = purchase_plan(airtime_balance, "daily_plans", daily_choice)
        elif choice == 2:
            show_weekly_menu()
            try:
                weekly_choice = int(input("Select a plan: "))
            except ValueError:
                print("Invalid input!, please enter a valid number")
                continue
            airtime_balance = purchase_plan(airtime_balance, "weekly_plans", weekly_choice)
        elif choice == 3:
            show_monthly_menu()
            try:
                monthly_choice = int(input("Select a plan: "))
            except ValueError:
                print("Invalid input!, please enter a valid number")
                continue
            airtime_balance = purchase_plan(airtime_balance, "monthly_plans", monthly_choice)
        elif choice == 4:
            check_balance(airtime_balance)
        elif choice == 5:
            show_history()
        elif choice == 6:
            print("Thanks for using the data menu engine")
            break
        else:
            print("Invalid Option")