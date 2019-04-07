import json
import sys
import operator
#ToDos
#   1.Limit the grades
#   2.Order the list
#   3.Grade should be a number


with open('gc_setup.json') as data_file:
    course = json.load(data_file)

grades = course["course_setup"]["grade_breakdown"]

current_grades = {"mygrades": {}}

for key in grades:
    print(grades[key])
    current_grades["mygrades"][key] = input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
    if (int(current_grades["mygrades"][key]) > 100 or int(current_grades["mygrades"][key])< -1):
        print("The number is larger than 100 or smaller than -1")
        sys.exit()

print (json.dumps(current_grades))
file = open("gc_grades.json", "w")
file.write(json.dumps(current_grades))
file.close()

curr_grade = 0
for key in current_grades["mygrades"]:
    if current_grades["mygrades"][key] != -1:
        calc_grade = int(current_grades["mygrades"][key]) * grades[key] / 100
        curr_grade = curr_grade + calc_grade

grades_str= (" - ".join(current_grades))
print(grades_str)

print (curr_grade)

