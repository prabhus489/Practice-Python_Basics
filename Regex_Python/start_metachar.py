import re

pattern = r"eggs(bacon)*"

if re.match(pattern, "eggs bacon"):
    print("match found")
