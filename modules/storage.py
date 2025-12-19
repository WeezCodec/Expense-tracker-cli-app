"""
Stores the informations collected from both expense_manager.py and calculation.py
"""
import json
from pathlib import Path
from  expense_manager import expense_manager

class expense_storage:

    def __init__ ( self , file_name) : 
         self.file_name = file_name

    def  save_to_file(self , expense_list ) :

        # self.file_name = input("Enter file name : ")

        file = Path ( self.file_name )

        if file.exists() :  #Checks of file_name exists

            with open ( self.file_name , "r") as file : 
                data = json.load(file)
                for expense in expense_list : 
                    data.extend ( expense_list) # Using EXTEND here instead of APPEND 
                print("File updated successfully.")    

            with open(self.file_name , "w") as file :
                json.dump ( data , file , indent= 3 )    


        else : 
                with open ( self.file_name , "w") as file : 
                    for expense in expense_list : 
                        json.dump(expense_list , file , indent= 3 )
                            
                    print("File saved successfully.")    
           

    def read_from_file(self) : 
         
        file = Path( self.file_name)

        if file.exists() : 
            try : 
                with open ( self.file_name , "r") as file : 
                    data = json.load(file)
                    print(data)
            except FileNotFoundError : 
                print("File not found..")
        else : 
            print(f"{self.file_name} does not exist.")         

                           
         

           
         

file_saver = expense_storage (input("Enter file name : ")) 
show_file = expense_manager()
per_expense = show_file.delete_expenses()
file_saver.save_to_file(per_expense)




