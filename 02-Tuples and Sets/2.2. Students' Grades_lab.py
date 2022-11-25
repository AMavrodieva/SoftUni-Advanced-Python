number_of_students = int(input())
students_list = {}
for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students_list:
        students_list[name] = []
    grade = float(grade)
    students_list[name].append(grade)
for name, value in students_list.items():
    average_grade = sum(value) / len(value)
    grades = " ".join(f'{grade:.2f}' for grade in value)
    print(f'{name} -> {grades} (avg: {average_grade:.2f})')
