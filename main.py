"""
Main. py : Where activation happens
"""
from  modules.expense_manager import expense
from modules.calculation import price_calculation
from modules.storage import expense_storage



def main() : 

    call_manager = expense
    call_calculation = price_calculation()
    call_storage = expense_storage()

    
    while True : 
        print(" \n======= WELCOME TO THE CLI EXPENSE TRACKER ======= ")
        print("\n1. Add expense")
        print("2. view expense")
        print("3. Delete from expense")
        print("4. Summary")
        print("5. Exit")

        choice = input("Choose tasks from options above: ")

        if choice == "1" : 
            call_manager.add_expense()
            call_storage.save_to_file(call_manager.expenses)
        elif choice == "2" : 
            call_manager.expenses = call_storage.read_from_file()
            print(call_manager.expenses)    
        elif choice == "3" : 
            call_manager.delete_expenses()
            call_storage.save_to_file(call_manager.expenses)
        elif choice == "4" : 
            call_manager.expenses = call_storage.read_from_file()
            summary_total = call_calculation.calculate_total_price(call_manager.expenses)
            summary_monthly = call_calculation.calculate_monthly_total(call_manager.expenses)
            print(f"Total amount : {summary_total} \n Monthly Summary : {summary_monthly}")
        elif choice == "5" : 
            print("Exiting ... Goodbye.")   
            break
        else : 
            print("Invalid input.")
            break



if  __name__ == "__main__" :
    main()