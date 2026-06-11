from pydantic import BaseModel

class Student(BaseModel):

    name : str

new_student ={'name': 'nitesh'}

student=Student(**new_student)


print(type(student))