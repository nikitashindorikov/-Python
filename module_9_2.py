first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
third_result = {}
result = [x for x in first_strings if len(x) >= 5 ]
print(result)
result_1 = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y) ]
print(result_1)
combined_string = first_strings + second_strings
result_2 = {x : len(x) for x in combined_string if len(x) % 2 == 0}
print(result_2)