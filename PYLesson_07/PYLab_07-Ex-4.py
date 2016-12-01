def replace():
    global sentence
    while sentence.count("a")>0:
        sentence = sentence[0:sentence.index("a")] + "@" + sentence[sentence.index("a")+1: len(sentence)]
        replace()
        
sentence = input("Write a sentence containing an a: ")
replace()
print(sentence)
