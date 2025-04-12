# ==    __eq__
# !=    __ne__
# >     __gt__
# >=    __ge__
# <     __lt__
# <=    __le__
# len   __len__
# in    __contains__


class Cat:
    """A Class that represent a cat"""

    def __init__(self, name: str, type: str, age: int) -> None:
        self.name = name
        self.type = type
        self.age = age

    def eat(self, food: str) -> str:
        return self.name + ": " + food + '好好吃呀～ 喵喵喵'

    def __str__(self) -> str:
        return self.name + ' ' + self.type + ' ' + str(self.age)

    def __gt__(self, other: 'Cat') -> bool:
        return self.age > other.age


class CatOwner:

    def __init__(self, name: str) -> None:
        self.name = name
        self.cats = []

    def add_cat(self, new_cat: 'Cat') -> bool:
        for cat in self.cats:
            if cat.name == new_cat.name:
                return False

        self.cats.append(new_cat)
        return True

    def __len__(self) -> int:
        return len(self.cats)

    def __contains__(self, cat: 'Cat') -> bool:
        return cat in self.cats

mua = Cat('Mua', '布偶', 3) # Cat.__init__(mua, 'Mua', '布偶', 3)
print(mua.name)

cici = Cat('Cici', '英短', 2)    # Cat.__init__(cici, 'Cici', '英短', 2)
print(cici.name)

print(mua.eat('🐟'))    # Cat.eat(mua, '🐟')
print(cici.eat('💩'))   # Cat.eat(cici, '💩')
print(Cat.eat(cici, '🐭'))

print(mua)      # Cat.__str__(mua)
print(cici)     # Cat.__str__(cici)
# <__main__.Cat object at 0x104833cd0>

print(mua > cici)   # Cat.__gt__(mua, cici) OR mua.__gt__(cici)
print(Cat.__gt__(mua, cici))
print(mua.__gt__(cici))

# --------------------
vc = CatOwner('Vincent')  # CatOwner.__init__(vc, 'Vincent')
print(vc.add_cat(mua))
print(vc.add_cat(cici))

胖胖 = Cat('Mua', '胖橘貓', 5)
print(vc.add_cat(胖胖))

print(len(vc))      # CatOwner.__len__(vc)

print(mua in vc)    # CatOwner.__contains__(vc, mua)
print(胖胖 in vc)