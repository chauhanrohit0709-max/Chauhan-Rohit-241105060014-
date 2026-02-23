print("Recharge System");

number = int(input("Enter mobile number: "));
plan = int(input("Enter plan amount: "));

if plan == 199:
 validity = 28
elif plan == 399:
 validity = 56
else:
 validity = 0
print("Number:", number)
print("Validity:", validity)

for i in range(3):
 print("Recharge Done")
print("Exit")