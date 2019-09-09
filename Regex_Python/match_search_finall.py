import re

pattern = r"eggs"
if re.match(pattern,"eggsbbseggseggsbacon"):
    print("Match Found")
else:
    print("No Match Found")

if re.search(pattern,"eggsbbseggseggsbacon"):
    print("Match Found")
else:
    print("No Match Found")


print(re.findall(pattern,"eggsbbseggseggsbacon"))
print(len(re.findall(pattern,"eggsbbseggseggsbacon")))
