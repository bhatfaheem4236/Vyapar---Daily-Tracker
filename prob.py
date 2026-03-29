import csv
import os 
from datetime import date
import matplotlib.pyplot as plt
SALES_FILE = "sales.csv"
EXPENSE_FILE = "expenses.csv"
def setup_files():
    if not os.path.exists(SALES_FILE):
        with open (SALES_FILE, "w", newline= "") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Item", "Qty", "Cost Price", "Sell Price", "Total Revenue", "Total Profit"])
    if not os.path.exists(EXPENSE_FILE):
        with open (EXPENSE_FILE, "w", newline= "") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Description", "Amount"])
def add_sales():
    print("\n ADD SALES ")
    today = str(date.today())
    item = input("  Item Name        :").strip()
    qty = int(input("  Quantity Sold    :"))
    cost = float(input("  Cost Price ($)   :"))
    sell = float(input("  Sell Price ($)   :"))

    total_revenue = qty * sell
    total_profit = (sell - cost) * qty

    with open(SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, item, qty, cost, sell, round(total_revenue, 2), round(total_profit, 2)])
    print(f"\n Saved Revenue: {total_revenue:.2f} | Profit: {total_profit:.2f}")

def add_expense():
    print("\n ADD EXPENSE ")
    today = str(date.today())
    desc = input("  Description       :").strip()
    amount = float(input("  Amount ($)       :"))

    with open(EXPENSE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, desc, round(amount, 2)])
    print(f"\n Saved Expense: {amount:.2f}")

def daily_summary():
    print("\n DAILY SUMMARY ")
    target = input(" Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not target:
        target = str(date.today())
    total_revenue = 0
    total_profit = 0
    sale_items = []
    total_expense = 0
    expenses_item = []
    if os.path.exists(SALES_FILE):
        with open(SALES_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Date"] == target:
                    total_revenue += float(row["Total Revenue"])
                    total_profit += float(row["Total Profit"])
                    sale_items.append(row)
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Date"] == target:
                    total_expense += float(row["Amount"])
                    expenses_item.append(row)

    net_profit = total_profit - total_expense
    print(f"\n Date: {target}")
    print(" "+ "-" * 40)
    if sale_items:
        for S in sale_items:
            print(f" SALE -> {S['Item']} | Qty: {S['Qty']} | Revenue: ${S['Total Revenue']} | Profit: ${S['Total Profit']}")
    else:
        print(" No sales recorded.")
    print(" "+ "-" * 40)
    if expenses_item:
        for E in expenses_item:
            print(f" EXPENSE -> {E['Description']} | Amount: ${E['Amount']}")
    else:       
        print(" No expenses recorded.")
    print(" "+ "-" * 40)
    print(f" Total Revenue: ${total_revenue:.2f}")
    print(f" Total Profit: ${total_profit:.2f}")
    print(f" Total Expenses: ${total_expense:.2f}")
    print(f" Net Profit: ${net_profit:.2f}")

def main():
    setup_files()
    print("\n VYAPAR DAILY TRACKER ")
    while True:
        print("\n 1. Add SALE")
        print(" 2. Add EXPENSE")
        print(" 3. View DAILY SUMMARY")
        print(" 4. show GRAPH")
        print(" 5. Exit")
        choice = input("\n Enter your choice: ").strip()
        if choice == "1":
            add_sales()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            daily_summary()
        elif choice == "4":
            show_graph()
        elif choice == "5":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

def show_graph():
    dates = []
    profits = []
    revenues = []
    if os.path.exists(SALES_FILE):
        with open(SALES_FILE, "r") as f :
            reader = csv.DictReader(f)
            for row in reader:
                dates.append(row["Date"])
                profits.append(float(row["Total Profit"]))
                revenues.append(float(row["Total Revenue"]))
    if not dates:
        print("\n No sales data to show graph.")
        return
    colors= []
    for p in profits:
        if p>0:
            colors.append("green")
        elif p<0:
            colors.append("red")
        else:
            colors.append("gray")

    plt.figure(figsize=(10, 5))
    plt.bar(dates, profits, color=colors, label="Profit/Loss")
    plt.plot(dates, revenues, color="blue", marker="o", label="Revenue")
    plt.title("Daily Profit and Revenue")
    plt.xlabel("Date")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":  
        main()