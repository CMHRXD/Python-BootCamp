# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 15 if size == "S" else 20 if size == "M"  else 25

if add_pepperoni == "Y":
    total += 2 if size == "S" else 3
if extra_cheese  == "Y":
    total+=1

print(f"Your final bill is: {total}.")


