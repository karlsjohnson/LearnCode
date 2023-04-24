file = open("books.txt", "r")

#your code goes here

lines = file.readlines()

for line in lines:
    x = line.split(" ")
    title = ""
    for i in x:
        title += i[0]
    print(title)

file.close()
