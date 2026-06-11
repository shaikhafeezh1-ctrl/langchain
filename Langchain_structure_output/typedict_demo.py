from typing import TypedDict

class Person(TypedDict):

    name: str
    age : int

new_name : Person = {"name":"Hafeez","age":25}

print(new_name)