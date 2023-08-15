# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

student_heights= [78, 65, 89, 86, 55, 91, 64, 89]
student_heights2 = [-78, -65, -89, -86, -55, -91, -64, -89]

highest_number = 0
index = 0

for height in student_heights:
    if index == 0:
        highest_number = height
        index+=1
    if height > highest_number:
        highest_number = height
        
print(f"The highest score in the class is: {highest_number}")

highest_number = 0
index = 0
     
for height in student_heights2:
    if index == 0:
        highest_number = height
        index+=1
    if height > highest_number:
        highest_number = height

print(f"The highest score in the class is: {highest_number}")
