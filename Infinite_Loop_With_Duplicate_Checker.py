# ask the user to input ten numbers
print("Please Enter numbers: ")

numbers = []  
duplicates = set()  
seen = set()  

while True:  # Loop continuing until the input is invalid
    user_input = input("Enter a number: ")

    if user_input.isdigit():  
        number = int(user_input)
        numbers += [number]  
    
        if number  in seen: # use if else statement 
            duplicates.add(number)  
        else:
            seen.add(number)  
    else:
        print("That is Invalid!!!!") 
        break # stopping when the input is invalid

print("You entered:", numbers)

if duplicates: # print the numbers with duplication
    print("Duplicate numbers:", duplicates)
else:
    print("There is no Duplicates")
