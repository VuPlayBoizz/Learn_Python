#C1
file = open("text.txt")
content_1 = file.read()
print(content_1)
file.close()

#C2
with open("text.txt") as file:
    content_2 = file.read()
    print(content_2)