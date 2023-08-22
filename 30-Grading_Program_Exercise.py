student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key,value in student_scores.items():

    student_grades[key] = "Outstanding" if value > 90 else "Exceeds Expectations" if  value > 80 else "Acceptable" if value > 70 else "Fail" 

# 🚨 Don't change the code below 👇
print(student_grades)