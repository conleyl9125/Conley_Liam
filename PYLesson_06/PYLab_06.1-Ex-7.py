word=input("please enter a word")
def printTri():
    for i in range (0, len(word)):
        print(word[len(word):i])

printTri()
