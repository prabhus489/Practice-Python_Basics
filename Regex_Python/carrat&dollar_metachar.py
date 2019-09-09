import re

pattern = r"^gr.y$"

if re.search(pattern, "gray"):
    print("matching")
