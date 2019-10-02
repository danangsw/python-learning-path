import re

find_member = []

for member in dir(re):
    if "find" in member:
        find_member.append(member)
        pass
    pass

print(find_member)