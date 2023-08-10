#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator")
bill = int(input("What is the bill? "))
people = int(input("How many people dined? "))
tip_percentage = int(input("What tip procentaje would you like to pay 10, 12 or 15 ?"))

result = round((bill/people) * (1+tip_percentage/100), 2) 

print(result)