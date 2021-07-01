# [] create list-o-matic

def list_o_matic (istring, ilist):
    
    if istring == "":
        return "'" + ilist.pop() + "' was poped from the list."
    elif istring in ilist:
        ilist.remove(istring)
        return "'" + istring + "' was removed from the list."
    else:
        ilist.append(istring)
        return "'" + istring + "' was appended to the list."
        
    
# [] copy and paste in edX assignment page
animals = ["dog", "cat", "bird", "fish"]
print ("Initial list: \n", animals)

while animals:
    answer = input ("Enter an animal, an empty string, or 'quit' to exit: ")
    
    if answer == "quit":
        break
    else:
        print (list_o_matic (answer, animals))
        print ("Current list: \n", animals)
    
        
if animals:
    print ("Here is the final list: \n", animals)
else:
    print ("List empty, exiting.")