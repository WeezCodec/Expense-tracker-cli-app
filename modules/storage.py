# """
# Stores the informations collected from both expense_manager.py and calculation.py
# """
import json
from pathlib import Path
from  expense_manager import expense



class expense_storage:

    def __init__ ( self , file_name) :
         
         self.file_name = file_name



    def  save_to_file(self , expense_list ) :

        # file_name = input("Enter file name : ")
        action = expense.last_action
        file = Path ( self.file_name )

        if action == "add" and  file.exists()  :  #Checks if file_name exists

            with open ( self.file_name , "r") as file : 
                data = json.load(file)
                
                data.extend (expense_list) # Using EXTEND here instead of APPEND 
                # print("File updated successfully.")    

            with open(self.file_name , "w") as file :
                json.dump ( data , file , indent= 3 )    
                print("File updated successfully.")


        else : 
                with open ( self.file_name , "w") as file : 
                    json.dump(expense_list , file , indent= 3 )
                            
                    print("File saved successfully.")    
           

    def read_from_file(self ) : 

        file = Path( self.file_name)

        if file.exists() : 
            try : 
                with open ( self.file_name , "r") as file : 
                    data = json.load(file)
                    return data
            except FileNotFoundError : 
                print("File not found..")
        else : 
            print(f"{self.file_name} does not exist.")         



call_manager = expense
call_storage = expense_storage(input("File name is required: "))

# call_manager.expenses = call_storage.read_from_file()
# print(call_manager.expenses)
print(call_manager.add_expense())

print(call_storage.save_to_file(call_manager.expenses))


