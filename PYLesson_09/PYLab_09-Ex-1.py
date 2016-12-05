words = ["hey", "hi", "hello", "sup", "greetings"]
print("in order...")

print(words)
print("")
print("Reversed...")


def reverse():
    out = ""
    for i in words:
        out += i + " "
    print(out)

reverse()
