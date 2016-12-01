word=input("Plesae enter a word")
stop=len(word)
start=0
def tree(word, start, stop):
    if start<stop or start==stop:
        print("{:>10}".format(word[0:start]))
        start+=1
        tree(word, start, stop)
        
tree(word, start, stop)
