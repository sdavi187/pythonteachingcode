# Allergy check 

# 1[ ] get input for test
input_test = input("Enter categories of food eaten in the last 24 hours:")
input_test_lower = input_test.lower()

# 2/3[ ] print True if "dairy" is in the input or False if not
print ("It is","dairy" in input_test_lower,'that "' + input_test +'" contains "dairy"')

# 4[ ] Check if "nuts" are in the input
print ("It is","nuts" in input_test_lower,'that "' + input_test +'" contains "nuts"')

# 4+[ ] Challenge: Check if "seafood" is in the input
print ("It is","seafood" in input_test_lower,'that "' + input_test +'" contains "seafood"')

# 4+[ ] Challenge: Check if "chocolate" is in the input
print ("It is","chocolate" in input_test_lower,'that "' + input_test +'" contains "chocolate"')