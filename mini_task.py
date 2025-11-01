with open("story.txt", "r") as file:
    lines = file.readlines()
print("Total lines:", len(lines))
for index, line in enumerate(lines, start=1):
    print(f"{index}, {line.strip()}")
file.close()