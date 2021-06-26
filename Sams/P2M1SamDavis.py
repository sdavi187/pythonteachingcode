# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [] copy and paste in edX assignment page

phrase = input ("Enter a phase: ")
phrase = phrase.lower()
index = ""
char = ""
word =""

for char in phrase:
 #   print (char)
    if char.isalpha():
        word = word + char
    elif word >= "h":
        print (word.upper())
        word = ""
    else:
        word = ""

if word.lower() >= "h":
    print(word.upper())