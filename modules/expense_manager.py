"""
Handles : 
Adding expenses , deleting expenses and returning the full expenses list
"""
from datetime import datetime

class expense_manager : 

    def __init__(self ) : 

        self.expenses = []
        self.last_action =  None

    def add_expense( self ) : 

        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        date = input("Enter date (YYYY - MM - DD): ")

        try:
            date_string = datetime.strptime( date , "%Y-%m-%d").date()
                
        except ValueError : 
            print("Invalid date format!")    
            
        opt_des = input("Enter description (optional): ")

        expense = {
            "Category" : category , 
            "Price" : price , 
            "Date": date,
            "Description" : opt_des
        }
            
        self.expenses.append(expense)
        self.last_action = "add"
        return self.expenses 
    
    def delete_expenses(self ) : 
        name_to_delete = input("Enter the category you want to delete: ")
        self.expenses =[
            record for record in self.expenses
            if  record["Category"] != name_to_delete
        ]
        self.last_action = "delete"
        return self.expenses

expense = expense_manager()






        

        
    


