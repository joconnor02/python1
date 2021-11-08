import os
import re

name = os.name
path = os.defpath

os_drive = re.search(r"[A-Z]", path)

print(name)
print(path)

print(os_drive.group())


# never used regex before so I couldn't get too technical with my pattern

