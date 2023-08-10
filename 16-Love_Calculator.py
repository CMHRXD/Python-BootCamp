# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combinedName = (name1 + name2).lower()

trueCountercombinedName = combinedName.lower().count("t")+ combinedName.lower().count("r")+combinedName.lower().count("u")+combinedName.lower().count("e")

loveCountercombinedName = combinedName.lower().count("l")+ combinedName.lower().count("o")+combinedName.lower().count("v")+combinedName.lower().count("e")

total = int(str(trueCountercombinedName)+str(loveCountercombinedName))

if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
