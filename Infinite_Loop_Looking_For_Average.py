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

# the operation of if-else statement for getting the average
if count > 0:  
    average = sum(numbers) / count  
    print("The average is:", average )  
else:  
    print("No valid numbers were entered.")  


