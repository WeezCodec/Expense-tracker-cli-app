"""
Calculates total expenses.
Calculates monthly breakdown.
"""

class price_calculation : 

    def calculate_total_price(self , expense_list) : 
        extract_price = [price["Price"] for price in expense_list]
        total_price = sum(extract_price)
        return total_price
    

    def calculate_monthly_total(self , expense_list) : 
        monthly_totals = {}
        for expense in expense_list : 
            month = expense["Date"][:7]
            monthly_totals[month] = monthly_totals.get(month , 0)  + expense [ "Price"]

        return  monthly_totals







