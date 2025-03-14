
while True:  # Loop continuing until the input is invalid
    user_input = input("Enter a number: ")

    if user_input.isdigit():  
        numbers.append(int(user_input))  
    else:
        print("That is Invalid!!!!") # stopping when the input is invalid
        break



