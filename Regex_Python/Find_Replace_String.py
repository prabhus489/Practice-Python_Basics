import re

string = "My name is jonarth. Hi I am jonarth."
pattern = r"jonarth"
newstring = re.sub(pattern, "prabhu", string)
print(newstring)
