

grades_class_a = [6, 2, 3, 3, 1, 4, 5, 5, 8, 9, 9]
grades_class_b = [7, 8, 9, 9, 10]




grades_set_a = set(grades_class_a)
grades_set_b = set(grades_class_b)
print(grades_set_a)


print("common grades in both class are", grades_set_a.intersection(grades_set_b))
print("grades only in a class", grades_set_a.difference(grades_set_b))
print("grades only in b class", grades_set_b.difference(grades_set_a))
