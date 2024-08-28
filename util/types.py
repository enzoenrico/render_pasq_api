from typing import List

class Part:
    def __init__(self, parent:str, code:str, ref:str, size: str, quantity:str):
        self.parent = parent
        self.code = code
        self.ref = ref
        self.size = size
        self.quantity = quantity

    def __str__(self):
        return f"{self.parent} {self.code} {self.ref} {self.size} {self.quantity}"

    def to_json(self):
        return {
            "parent": self.parent,
            "code": self.code,
            "ref": self.ref,
            "size": self.size,
            "quantity": self.quantity
        }

class PartsList:
    def __init__(self, name: str, parts: List[Part]):
        self.name = name
        self.parts = parts
    def to_json(self):
        return {
            "name": self.name,
            #makes a list of parts in json format
            "parts": [part.to_json() for part in self.parts]
        }
