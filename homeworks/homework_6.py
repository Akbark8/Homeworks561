colors = {
    "red": "\033[31m",
    "yellow": "\033[33m",
    "orange": "\033[38;5;208m",
    "purple": "\033[35m",
    "gold": "\033[38;5;220m",
    "blue": "\033[34m",
    "green": "\033[32m",
    "reset": "\033[0m"
}

fruits = [
    ("Apple", "red"),
    ("Banana", "yellow"),
    ("Orange", "orange"),
    ("Grapes", "purple"),
    ("Mango", "gold"),
    ("Blueberry", "blue"),
    ("Kiwi", "green")
]

for fruit, color in fruits:
    print(colors[color] + fruit + colors["reset"])
