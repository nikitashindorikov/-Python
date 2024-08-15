immutable_var = 1, "nikita", True
print( immutable_var)
#immutable_var[0] = False Нельзя изменить так как он является не изменяемым из за отсутствия скобок в строке
mutable_list = ([3, "name", False])
print(mutable_list)
mutable_list[2] = "nikita"
mutable_list.append("bit")
print(mutable_list)