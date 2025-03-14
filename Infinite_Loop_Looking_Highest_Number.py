# ask the user to input numbers that is valid
print("Please Enter numbers: ")

numbers = []  

while True:  # Loop continuing until the input is invalid
    user_input = input("Enter a number: ")

    if user_input.isdigit():  
        number = int(user_input)
        numbers += [number]  
    else:
        print("That is Invalid!!!!") 
        break # stopping when the input is invalid    

if numbers:  
    highest = max(numbers)  
    print("Highest number entered:", highest)  
else:  
    print("No valid numbers were entered.")  


