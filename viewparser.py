import json
import os
import sys
from jsonviewparser import JSONViewParser

USAGE = """Enter a selector:
           class - e.g. 'StackView'
           classNames - e.g. '.container'
           identifier - e.g. '#videoMode'

To quit, enter 'q'"""

# Main Program
parser = JSONViewParser("viewhierarchy.json")

print(f"{USAGE}")

while True:
    selector = input("Enter selector: ")
    if selector == "q":
        break

    type = "class"
    if selector[0] == '.':
        type = "classNames"
        selector = selector[1:]
    elif selector[0] == "#":
        type = "identifier"
        selector = selector[1:]

    items = parser.find(type, selector)
    if (len(items) == 0):
        print("No matches found.")
    else:
        for i in items:
            print(f"{json.dumps(i, indent=2)}")
