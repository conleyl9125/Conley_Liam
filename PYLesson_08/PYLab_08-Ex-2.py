word1=input("enter a word")
word2=input("enter another word")
word3=input("enter another word")

def makeCenter(whichWord):
    if len(whichWord)>20 or len(whichWord)==20:
        return whichWord
    else:

        return makeCenter((" " + whichWord + " "))

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))
