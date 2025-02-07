
choose_operation=int(input("Enter 1 for addition:\nEnter 2 for subtraction:\nEnter 3 for multiplication:\nEnter 4 for division: \n"))
if choose_operation==1:
    user_input_1= int(input("Enter your first number: "))
    user_input_2= int(input("Enter your first number: "))
    sum= user_input_1 + user_input_2
    print("The sum is: ",sum)
elif choose_operation==2:
    user_input_1= int(input("Enter your first number: "))
    user_input_2= int(input("Enter your first number: "))
    subtraction= user_input_1 - user_input_2
    print("The subtraction is: ",subtraction)

elif choose_operation==3:
    user_input_1= int(input("Enter your first number: "))
    user_input_2= int(input("Enter your first number: "))
    multiplication= user_input_1 * user_input_2
    print("The multiplication is: ",multiplication)

elif choose_operation==4:
    user_input_1= int(input("Enter your first number: "))
    user_input_2= int(input("Enter your first number: "))
    division=user_input_1 / user_input_2
    print("The division is :",division)

else:
    print("Sorry calculater out of service right now")
