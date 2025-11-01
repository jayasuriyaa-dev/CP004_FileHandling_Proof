def get_emoji(word_count):
    if word_count <= 4:
        return "🐣"
    elif word_count <= 6:
        return "💡"
    elif word_count <= 8:
        return "🕊"
    else:
        return "🎯"

total_lines = 0
total_words = 0

with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("🔸 Stylish File Reader Output 🔸\n")

for i, line in enumerate(lines, start=1):
    clean_line = line.strip()
    words = clean_line.split()
    word_count = len(words)
    emoji = get_emoji(word_count)
    title_line = clean_line.title()
    
    print(f"📘 Line {i} ({emoji} – {word_count} words): {title_line}")

    total_lines += 1
    total_words += word_count

print("\n🧾 Summary:")
print(f"Total Lines: {total_lines}")
print(f"Total Words: {total_words}")