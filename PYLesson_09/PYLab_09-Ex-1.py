words = ["hey", "hi", "hello", "sup", "greetings"]
print("in order...")

print(words)
print("")
print("Reversed...")


def reverse():
    out = ""
    for i in range(len(words)-1,-1,-1):
        out += words[i] + " "
    print(out)

reverse()
