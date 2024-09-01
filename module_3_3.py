#def print_params(a=1, b='строка', c=True):
#   print(a, b, c)
#values_list = [5, "lit", False]
#values_dict = {"a": 2, "b": "finish", "c": (9, 10, 11)}
#for key, value in values_dict.items():
#   print(key, value)
#print_params(b=25)
#print_params(c=[1, 2, 3])
#print_params(**values_dict)
#def print_prams(a, b, c, d, f, r):
 #   print(a, b, c, d, f, r)
  #  for value in values_dict.items():
   #     print(*value)


#values_list = [5, "lit", False]
#values_dict = {'a': 2, 'b': "finish", 'c': (9, 10, 11)}
#print_prams(*values_list, *values_dict)

def print_params(a=1, b='строка', c=True):
    print(a, b, c)
values_list_2 = [2, False]
print_params(*values_list_2, 42)
