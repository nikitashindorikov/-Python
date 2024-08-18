grades = ([5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5])
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
my_list = list(students)
n = (sum(grades[0]) / len(grades[0]))
n1 = (sum(grades[1]) / len(grades[1]))
n2 = (sum(grades[2]) / len(grades[2]))
n3 = (sum(grades[3]) / len(grades[3]))
n4 = (sum(grades[4]) / len(grades[4]))
new_list = ["Johnny:(n)", "Bilbo:(n1)", "Steve:(2)", "Khendrik:(3)", "Aaron:(4)"]
dictionari = {new_list[0]:(n), new_list[1]:(n1), new_list[2]:(n2), new_list[3]:(n3), new_list[4]:(n4)}
print(dictionari)

