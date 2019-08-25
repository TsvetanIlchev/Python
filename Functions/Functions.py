def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width -len(text)) // 2
    print(" " * left_margin, text)

def center_text(*args, sep = " "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 -len(text)) // 2
    return " " * left_margin + text


print(center_text("Spam and eggs"))
print(center_text("Spam and eggs2"))
print(center_text("Spam and eggs3"))
print(center_text(7477))
print(center_text("first", "second", "three", 3, 4, sep = ":"))

print("=" + str(12 * 3))
print(sorted(["b", "d", "c", "a"]))