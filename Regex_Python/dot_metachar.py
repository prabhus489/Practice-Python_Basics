import re

pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("match found")
