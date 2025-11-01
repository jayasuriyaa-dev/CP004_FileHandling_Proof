with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("📋 All Lines (As List):")
print(lines)

print("\n🪄 Printing One by One with Line Number:")
for i, line in enumerate(lines, start=1):
    print(f"{i}: {line.strip()}")