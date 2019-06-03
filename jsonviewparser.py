import json

class JSONViewParser:

    def __init__(self, jsonFile):
        with open(jsonFile) as f:
            self.view = json.load(f)

    def recursiveFind(self, type, selector, tree, items):
        if isinstance(tree, dict):
            for k,v in tree.items():
                if k == type and type == "classNames":
                    for name in v:
                        if name == selector:
                            items.append(tree)
                            return
                elif k == type and v == selector:
                    items.append(tree)
                    return
                elif k == "subviews":
                    for obj in v:
                        self.recursiveFind(type, selector, obj, items)
                else:
                    self.recursiveFind(type, selector, v, items)

    def find(self, type, selector):
        items = []
        self.recursiveFind(type, selector, self.view, items)
        return items
