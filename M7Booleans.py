#khateeja khatoon
# nov 14 2024 
#problem 1,2,3,4,6
#this program contains functions to demonstrate the use of booleans in python.

#problem1
def check_equal():
     #function to check if two inputs from the user are equal.
    
     input1 = input("enter the first value: ")
     input2 = input("enter the second value: ")

     #check if the inputs are equal
     if input1 == input2:
          print("the values are equal.")
     else:
          print("the values are not equal.")
#test the function 
if __name__ == "__main__":
     check_equal()
    
#problem2
def check_sum():
     #funtion to check if the sum of two inputs is greater, less,or equal to 10.
     num1 = float(input("enter the first number:"))
     num2 = float(input("enter the second number:"))
     total = num1+ num2
     if total > 10:
          print("the sum is greater than 10.")
     elif total< 10:
          print("the sum is less than 10.")
     else:
          print("the sum is equal to 10.")
  #test the function:
     check_sum()   

def check_value_in_list(value_list):
     #function to determine if a year is a leap year.
    if 5 in value_list:
         print("the value 5 is in the list.")
    else:
         print("the value 5 is not in trhe list.")
#test the function:
test_list =[1,2,3,4,5]
check_value_in_list(test_list)

def is_leap_year(year):
     #function to determine if a year is a leap year.
     if (year% 4 == 0 and year % 100 == 0) or (year % 400 == 0):
          return True
     else:
       return False
#test the function:
print("check if a year is a leap year")
year = int(input("enter a year to check if it's a leap year"))
if is_leap_year(year):
     
     print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")

 #problem 6
 #funtion to check if the game character has the required items and no weakness for the given task
def check_task_requirements(task_number):
    items =["pan","paper","idea","rope","groceries"]
    weaknessess = ["slow"]

        #define task requirements and weakness
    tasks ={
            1:{
                "required_items": ["rope", "coat","first aid kit"],
                "weakness": "slow"
            },
            2: {
                "required_items": ["pan", "groceries"],
                "weakness": "slow"
            },
            3: {
                "required_items": ["pen", "paper","idea"],
                "weakness": "confusion"
            }
        }
        
    if task_number not in tasks:
            print("invalid task number.please entera number between 1 and 3.")
            return
    #get the requirements for the selected task
    required_items =tasks[task_number ]["required_items"]
    weakness =tasks[task_number]["weakness"]

    #check for required items 
    items_found = all(items in items for item in required_items)
    #check for weakness
    has_weakness = weakness in weaknessess
    #confirm checks with print statements
    if items_found and not has_weakness:
     print(f"task {task_number} can be performed: all required iytems are present and there are no weaknesses.")
    else:
     if not items_found:
            missing_items = [item for item in required_items if item not in items]
            print(f"task {task_number} cannot be performed: missing items -{','.join (missing_items)}.")
     if has_weakness:
            print(f"task {task_number} cannot be performed: character has a weakness - {weakness}.")   

    # test the function 
    if __name__ == "__main__":
     print("checking task 1:")
    check_task_requirements(1)
    print("\nchecking task 2:")
    check_task_requirements(2)
    print("\nchecking task 3:")  
    check_task_requirements(3)       







            
            
        