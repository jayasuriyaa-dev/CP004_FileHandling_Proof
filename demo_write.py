'''#write
file = open("Sample.txt", "w",encoding="utf-8")
file.write("Hello from Clementine and Jayasuriyaa!\n")
file.write("You are learning file Handling 🔥")
file.close()

#Read Method 1
file = open("Sample.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

#Read Method 2
file = open("Sample.txt", "r", encoding="utf-8")
lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()'''

#Bonus Method
with open("Sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


