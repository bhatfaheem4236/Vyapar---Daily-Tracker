'''VYAPAR DAILY TRACKER  '''

expense = []
print("THANKS FOR CHOOSING EXPENSE TRACKER ")

while True:
    print("=======MENU========")
    print("1. Add SALE ")
    print("2. View ALL SALES  ")
    print("3. View Total SALE ")
    print("4. View Total profit")
    
    choice = int(input("ENTER TYPE OF ITEM :"))
    

    if choice == 1:
        date = input("ENTER DATE :")
        category = input("ENTER TYPE OF CATEGORY :")
        description = input("WHAT YOU HAD BUYED : ")
        amount = float(input("ENTER AMOUNT : "))

    expense= {
        "Date":date,
        "Category ":category,
        "Description":description,
        "Amount":amount
    }

    expense.append(expense)
    print("\n DONE . EXPENSES ARE ADDED SUCCESFULLY")

    if(choice ==2 ):
        if(len(expense)==0):
            print("NO EXPENSE YET : ")
        else:
            print("TOTAL EXPENSE : ")
            count= 1
            for eachexpenses in expense:
                print(f"EXPENSE NUMBER {count} -> {eachexpenses["DATE"]} , {eachexpenses["D"]} ")
                
                