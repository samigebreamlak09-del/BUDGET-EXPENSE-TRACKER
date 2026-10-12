file="expenses.txt"
def welcome():
    print("personal expenses tracker")
    print("------------------")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Remove expenses")
    print("5. Exit")
    print("--------------------")
    print()
    
    
def load_expenses():
    expenses = []
    
    try:
        with open(file, "r") as f:
            for line in f:
                category, amount = line.strip().split(",")
                expenses.append({"category":category,"amount" : amount})
     
    except FileNotFoundError:
        print("file doesnt exist.")
    
    except Exception as e:
        print(e)
    return expenses
  
      
def save_expenses(expenses):
     with open(file, "w") as f:
        for e in expenses:
           f.write(f"{e["category"]},{e["amount"]}\n")

def add_expense(expenses):
      try:
          category=input("enter your category: ")
          amount=float(input("enter your amount: "))
          expenses.append({"category" : category, "amount": amount})
          save_expenses(expenses)
          print("expense added successfully")
   
      except ValueError:
          print("invalid amount input.")
  
      except Exception as e:
          print(e)
     
     
     
def view_expense(expenses):
    if not expenses:
        print("there are no expenses to view")
        return 
    
    print("\nexpense: ")
    i =1
    for e in expenses:
        print(f"{i}. {e["category"]} = {e["amount"]}")
        i +=1
    print()
      
def total_expense(expenses):
   total= 0
   for e in expenses:
       total += float(e["amount"])
   
   print(f"your total expenditure is: {total}£")

def remove_expense(expenses):
    if not expenses:
        print("\n there are no expenses to remove,")
        return
     
    view_expense(expenses)
    try:
        number=int(input("enter your number: "))
        if number >= 1 and number <= len(expenses):
            removed=expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"removed: {removed["category"]} - {removed["amount"]}")
        
        else: 
            print("inavlid number\n")
     
    except valueerror:
        print("enter a valid number.\n")
         
         
         
def main():
    welcome()
    expenses = load_expenses()
    while True:
        choice=input("choose?:")
        if choice=="1":
            add_expense(expenses)
        
        elif choice=="2":
           view_expense(expenses)
        
        elif choice=="3":
           total_expense(expenses)
        
        elif choice=="4":
           remove_expense(expenses)
        
        elif choice=="5":
           print("thank you for using our program!")
           return
        else:
            print("invalid input")
             
           
main()
        
        
          
           
         
             
        
   



  
  
  
     
             
            
    
    