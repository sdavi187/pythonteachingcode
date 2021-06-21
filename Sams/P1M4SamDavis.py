# [ ] create, call and test the str_analysis() function  
max_num = 99
user_input = ""


def str_analysis(user_input):
    if user_input.isnumeric():
        if int(user_input) > max_num:
            return ("That's a pretty big number.")
        else:
            return ("That number is fairly small.")
    elif user_input.isalpha():
        return ("'" + user_input + "' is all alphabetical characters")
    else:
        return ("You're sending mixed messages")

while True:
    
    answer = input ("\nEnter a string for analysis (Return to exit): ")
    
    if answer == "":
        break
    else:
        print (str_analysis(answer))
        