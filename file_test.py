'''f = open("demo.txt", "w")
f.write("Welcome to our Developer Classroom \nPython file reading is awesome! \nlearning never stops.")
f.close

print("File created and written successfully.")'''

#Method 3_read
f = open("demo.txt", "r")

lines = f.readlines()

for line in lines:
    print(line.strip())

f.close()
