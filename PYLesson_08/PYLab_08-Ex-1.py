def recur(senten):
    global sentence
    if sentence.count(" ")==0:
        return sentence
    else:
        while sentence.count(" ")>0:
            sentence = sentence[0:sentence.index(" ")] + "_" + sentence[sentence.index(" ")+1: len(sentence)]
            recur(sentence)
sentence = input("Write a sentence")
recur(sentence)
print(sentence)
