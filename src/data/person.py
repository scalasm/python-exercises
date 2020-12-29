import json
from typing import Any

# class Person(object):
#     def __init__(self, first: str, last: str, age: int) -> None:
#         super().__init__()
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def speak(self):
#         return f"Hello, I'm {self.first} {self.last} and I'm {self.age} years old"

from dataclasses import dataclass

@dataclass
class Person(object):
    first: str
    last: str
    age: str
 
    # Additional validation here
    def __post_init__(self) -> None:
        pass

    def speak(self):
        return f"Hello, I'm {self.first} {self.last} and I'm {self.age} years old"
