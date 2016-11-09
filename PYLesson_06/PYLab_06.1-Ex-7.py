word=input("please enter a word")
def printTri():
    for i in range (len(word),-1,-1):
        print(word[i:len(word)])

printTri()
