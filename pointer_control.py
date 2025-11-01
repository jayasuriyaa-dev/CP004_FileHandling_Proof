# pointer_control.py

file = open("Sample.txt", "r", encoding="utf-8")

print("📍Initial Pointer Position:", file.tell())  # should be 0

content = file.read(10)  # read first 10 characters
print("📖 Read Content:", content)

print("📍Pointer After Reading 10 chars:", file.tell())

file.seek(0)  # Move pointer back to start
print("🔄 Pointer Reset to:", file.tell())

content2 = file.read()  # Read full content now
print("📖 Full File Content:\n", content2)

file.close()