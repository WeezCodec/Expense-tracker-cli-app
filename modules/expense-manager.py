"""
Handles : 
Adding expenses , deleting expenses and returning the full expenses list
"""
from datetime import datetime

class expense_manager : 

    def __init__(self ) : 

        self.view_expenses = []


    def add_expenses( self ) : 

        for i in range ( 2 ) : 

            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            date = input("Enter date (YYYY - MM - DD): ")
            try:
                date_string = datetime.strptime( date , "%Y-%m-%d").date()
                # return date_string
            except ValueError : 
                print("Invalid date format!")    
            opt_des = input("Enter description (optional): ")

            view_expense = {
                "Category" : category , 
                "Price" : price , 
                "Date": date ,
                "Description" : opt_des
            }
            
            self.view_expenses.append(view_expense)
        return self.view_expenses
    
    def delete_expenses(self) : 
        name_to_delete = input("Enter the category you want to delete: ")
        self.view_expenses =[
            record for record in self.view_expenses
            if  record["Category"] != name_to_delete
        ]
        return self.view_expenses



expenses = expense_manager()
print(expenses.add_expenses())
print(expenses.delete_expenses())
    





        

        
    


