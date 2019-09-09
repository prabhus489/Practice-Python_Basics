import re
#aA1
pattern = r"[a-z][A-Z][0-9]"

if re.match(pattern, "aF2"):
    print("match found")
