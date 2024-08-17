my_dict = {"Nikita": 1997, "Lera": 2002, "Nastia": 2001}
print(my_dict)
print(my_dict["Nikita"])
my_dict["Max"] = 1995
print(my_dict)
my_dict.update({"Anton": 1980,
                "Stas": 1973})
print(my_dict)
my_dict.pop("Max")
print(my_dict.get("Max", "Такого обьекта не существует"))
print(my_dict)
my_set = {1, 3, 7, "Nikita", False, 1, 3, 7, 9}
print(my_set)
my_set.update({2, 4})
print(my_set.discard(False))
print(my_set)
