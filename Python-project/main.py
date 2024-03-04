#print("This is first code")


calculation_to_second = 24 * 60 * 60
name_of_unit = "seconds"
#print("This is number as String " + str(50) + " Test string")
#print(f"20 days are {30 * calculation_to_second} {name_of_unit}")
#print(f"20 days are {35 * calculation_to_second} {name_of_unit}")
#print(f"20 days are {50 * calculation_to_second} {name_of_unit}")
#print(f"20 days are {110 * calculation_to_second} {name_of_unit}")


def days_of_unit(num_of_days):
    return f"{num_of_days} days are {30 * calculation_to_second} {name_of_unit}"
    print(custom_message)

#def scope_check():
    #print(calculation_to_second)
    #print(num_of_days)

#days_of_unit(30, "this is great")
#days_of_unit(35, "Awesome")
#scope_check()

#value_days_of_unit = days_of_unit(30)
#print(value_days_of_unit)

def validate_and_exectue():
    try:
        user_input_number = int(number_of_days_element)
        if user_input_number > 0:
           calculation_value = days_of_unit(user_input_number)
           print (calculation_value)
        elif user_input_number == 0:
            print("You entered 0, pls enter valid positive number")
        else:
            print("You entered a negative number, no conversion for you")
    except ValueError:
        print("Your input is not a valid number, pls enter valid number")

user_input=""
while user_input.lower()!="exit":
    user_input= input("Please enter valid number for converstion:\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))


    for number_of_days_element in set(user_input.split(", ")):
        user_input = number_of_days_element
        validate_and_exectue()



