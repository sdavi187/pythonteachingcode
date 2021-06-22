# [ ] create, call and test the adding_report() function

def adding_report(report = "T"):
    total = 0
    items = ""
    
    while True:
        value = input ('Enter an integer, or "Q" to quit: ')
        if value.isnumeric():
            total = total + int(value)
            if report == "A":
                items = items + "\n" + value
        elif value.startswith("Q"):
            if report == "A":
                print ("\nItems Entered:" + items)
                print ("\nTotal:\n" + str(total))
                break
            elif report == "T":
                print ("\nTotal:\n" + str(total))
                break
            else:
                print ("Invalid Report Type")
                break
        else:
            print ("Invalid Entry, try again. \n")
            
adding_report("T")