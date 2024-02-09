from dataclasses import dataclass,field
@dataclass

class Xodim:
    name: str
    age: int

    emp_id: str
    city: str = field(init=True,default="tashkent")

obj = Xodim("Diyorbek",15,"123di")
print(obj)

