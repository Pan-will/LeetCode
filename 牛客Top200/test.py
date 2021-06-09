string = "0000"
for ch in string:
    if ch.islower():
        print(ch >= "f")
    elif ch.isupper():
        print(ch >= "F")


a = set(string)
print(len(a))
print(a)