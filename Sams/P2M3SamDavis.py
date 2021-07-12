# [] create poem mixer
# [] copy and paste in edX assignment page
# Test Phrase: Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?

def word_mixer(word_list):
    
    word_list.sort()
    new_list = []
    
    while len(word_list) > 5:
        new_list.append(word_list.pop(-5))
        new_list.append(word_list.pop(0))
        new_list.append(word_list.pop(-1))
        new_list.append("\n")
    
    
    return(new_list)
    


in_string = input ("Enter a phrase, such as a poem, verse, or saying: ")


in_list = in_string.split(" ")

# i = 0

for i in range(0,len(in_list)):
    word = in_list[i]
    if len(word) <= 3:
        in_list[i] = word.lower()
    elif len(word) >= 7:
        in_list[i] = word.upper()
    else:
        in_list[i] = word
    
print(" ".join(word_mixer(in_list)))