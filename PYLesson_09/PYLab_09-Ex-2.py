word1=input("Enter a word")
word2=input("Enter another word")
word3=input("Enter another word")
word4=input("Enter another word")
word5=input("Enter another word")

words=[word1, word2, word3, word4, word5]

def first(words):
    for i in words:
        print(i[0])

first(words)
