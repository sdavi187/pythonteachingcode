import os
os.system("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements.txt")
guesses = []
correct = []
incorrect = []
elements = []
elements_file = open("elements.txt","r")

    
def get_names():
    guesses = []
    i = 0
    
    while i < 5:
        temp_guess = input("Name one of the first 20 elements of the Periodic Table of Elements: ").lower()
        
        if temp_guess in guesses:
            print ("You have already guessed that element. No duplicate guesses allowed.")
        elif temp_guess == "":
            print ("Emtpy answers are not allowed")
        else:
            guesses.append(temp_guess)
            i += 1
            
    return guesses

index = 0

while True:
    
    temp = elements_file.readline().strip("\n ").lower()
    if temp == "":
        break
    else:
        elements.append(temp)
    
guess = get_names()

index = 0

for index in guess:
    if index in elements:
        correct.append(index)
    else:
        incorrect.append(index)

print ("Score: " + str((len(correct)/5)*100) + "%")

print ("Found: ", end="")
for x in correct: 
    print (x, end=" ")
print ("")
    
print ("Not Found: ", end="")
for x in incorrect:
    print (x, end=" ")
print ("")



        
elements_file.close()