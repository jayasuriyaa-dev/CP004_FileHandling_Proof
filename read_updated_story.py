with open("story.txt", "r") as file:
    print("📚 Updated story:\n", 
file.read())
file.close()

#step 5
with open("story.txt", "r") as file:
    for line in file:
        print("🔸", line.strip())

#step 6
try:
    with open("story.txt", "a") as file:
        file.write("This Family never forget's to hold each other.\n")
except Exception as e:
    print("Something went wrong:", e)