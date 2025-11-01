#destructive_tool_test
with open("demo.txt", "w", encoding="utf-8") as file:
    file.write("⚠️ Warning:All previous content is now gone.\n")
    file.write("This was a test to verify 'w' mode.\n")

with open("demo.txt", "r",encoding="utf-8") as file:
    content = file.read()
print("📁 File Content:")
print(content)