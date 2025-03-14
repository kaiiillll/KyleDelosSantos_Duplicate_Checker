# ask the user to input numbers that is valid
print("Please Enter numbers: ")

numbers = []  
count = 0

while True:  # Loop continuing until the input is invalid
    user_input = input("Enter a number: ")
    count += 0
    
    try:
        number = int(user_input)  
        numbers.append(number)  
        count += 1  
    except:
        print("That is Invalid!!!!") 
        break # stopping when the input is invali

sorted_numbers = sorted(numbers, reverse=True)  
print("Numbers sorted from highest to lowest:", sorted_numbers)