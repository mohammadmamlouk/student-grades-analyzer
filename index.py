##Write a python program to enter students' names and grades (out of 100) (the number of students should be decided by the user) and the program will do the following:
# - Prints students names and grades
# 2- Prints the average grade of the class
# 3- Prints the highest grade earned (Student name and grade)
# 4- Prints the count of students who passed (grade >= 60)

# You have to use loops, lists and functions.
# Your code should have the following functions `display_student_summary`, `get_avg_grade`, `get_heighest_grade`, `count_passed`###

def display_student_summary(names, grades):
    print("\n====== Summary =========")
    for i in range(len(names)):
        print(f"{names[i]}: {grades[i]}")
    print()

def get_avg_grade(grades):
    return sum(grades) / len(grades)

def get_heighest_grade(names, grades):
    max_grade = max(grades)
    index = grades.index(max_grade)
    return names[index], max_grade

def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count


names = []
grades = []

n = int(input("enter the number of student "))

for i in range(n):
    name = input(f"Enter name of student {i + 1}: ")
    grade = float(input(f"Enter grade of {name}: "))
    names.append(name)
    grades.append(grade)

display_student_summary(names, grades)

avg = get_avg_grade(grades)
print(f"Average grade of the class: {avg:.2f}")

student, grade = get_heighest_grade(names, grades)
print(f"Highest grade earned by: {student} with {grade}")

passed_count = count_passed(grades)
print(f"Number of students who passed (grade >= 60): {passed_count}")
