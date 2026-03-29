import csv
import os
from datetime import date
#file name 
SALES_FILES = "sales.csv"
EXPENSES_FILE = "expenses.csv"
# setup csv files if not exist 
def setup_files():
    if not os.path.exists(SALES_FILES):
        with open(SALES_FILES, "w", newline="" )as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Item", "Qty", "Cost of Price", "Sell Price", "Total Revenue", "Total Profit"])


    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Description", "Amount"])

#ADD SALE ENTRY 
def add_sales():
    print("\n ADD SALES ")
    today= str(date.today())
    item = input("    Item Name        :").strip()
    qty = int(input("  Quantity Sold    :"))
    cost = float(input(" Cost Price ($)" ))
    sell = float(input(" Sell Price ($)"))

    total_revenue = qty * sell
    total_profit = (sell - cost) * qty


    with open(SALES_FILES, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, item, qty, cost, sell, round(total_revenue, 2), round(total_profit, 2)])
    print(f"\n Saved Revenue: {total_revenue:.2f} | Profit: {total_profit:.2f}")

    # ADD EXPENSE ENTRY
def add_expense():
    print("\n ADD EXPENSE ")
    today = str(date.today())
    desc = input("  Description       :").strip()
    amount = float(input("  Amount ($)       :"))

    with open(EXPENSES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, desc, round(amount, 2)])
    print(f"\n Saved Expense: {amount:.2f}")

# DAILY SUMMARY
def daily_summary():
    print("\n DAILY SUMMARY ")
    target = input(" Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not target:
        target = str(date.today())
    total_revenue = 0
    total_profit = 0
    sale_items = []

    # Calculate total revenue and profit from sales
    if os.path.exists(SALES_FILES):
     with open(SALES_FILES, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == target:
              total_revenue += float(row["Total Revenue"])
              total_profit += float(row["Total Profit"])
              sale_items.append(row)

    # Calculate total expenses
        total_expense = 0
        expense_items= []
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Date"] == target:
                    total_expense += float(row["Amount"])
                    expense_items.append(row)

    net_profit = total_profit - total_expense

    print(f"\n Date              : {target}")
    print("  "+ "-" * 40)
    if sale_items:
        print(" Sales:")
        for s in sale_items:
            print(f"  - {s['Item']} | Qty: {s['Qty']} | Revenue: ${s['Total Revenue']} | Profit: ${s['Total Profit']}")
    else:
        print("Sales       : No sales recorded.")

    print("  "+ "-" * 40)
    if expense_items:
        print(" Expenses:")
        for e in expense_items:
            print(f"  - {e['Description']} | Amount: ${e['Amount']}")
        
    else:
        print("Expenses     : No expenses recorded.")
    print("  "+ "-" * 40)
    print(f" Total Revenue: ${total_revenue:.2f}")
    print(f" Gross Profit: ${total_profit:.2f}")
    print(f" Total Expenses: ${total_expense:.2f}")
    print(f" Net Profit    : ${net_profit:.2f}" if net_profit >= 0 else f" Net Loss      : ${abs(net_profit):.2f}")
    print("  "+ "-" * 40)
  #MAIN MENU
    def view_all_sales():
        print("\n ALL SALES RECORDS ")
        if not os.path.exists(SALES_FILES):
            print("No sales data found.")
            return
        with open(SALES_FILES, "r") as f:
            reader = csv.DictReader(f)
            sales = list(reader)
            if not sales:
                print("No sales recorded.")
                return
            print(f"\n {'Date':<20} {'Item':<20} {'Qty':<5} {'Revenue':<10} {'Profit':<10}")
            print("-" * 70)
            for r in sales:
                print(f"{r['Date']:<20} {r['Item']:<20} {r['Qty']:<5} ${r['Total Revenue']:<10} ${r['Total Profit']:<10}")
    def main():
        setup_files()
        print("\n" + "=" * 45)
        print(" WELCOME TO VYAPAR DAILY TRACKER ")
        print("=" * 45)
        while True:
    
            print("\n  1. Add SALE")
            print("   2. Add EXPENSE")
            print("   3. View DAILY SUMMARY")
            print("   4. View ALL SALES")
            print("   5. Exit")

            choice = input("\n Enter your choice (1-5): ").strip()
            if choice == "1":
                add_sales()
            elif choice == "2":
                add_expense()
            elif choice == "3":
                daily_summary()
            elif choice == "4":
                view_all_sales()
            elif choice == "5":
                print("\n Thank you for using Vyapar Daily Tracker. Goodbye!")
                break
            else:
                print("\n Invalid choice. Please enter a number between 1 and 5.")

            if __name__ == "__main__":  
                main()