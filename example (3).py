# unit converter
value = float(input("Enter value: "))
choice = input("Type C for Celsius to Fahrenheit or M for meters to feet: ")

if choice == "C":
    result = (value * 9/5) + 32
elif choice == "M":
    result = value * 3.281
else:
    result = "Invalid"

print("Result:", result)

# tax system3:
income = float(input("Enter your income: "))

if income <= 10000:
    tax = income * 0.05
elif income <= 30000:
    tax = income * 0.1
else:
    tax = income * 0.15

net = income - tax

print("Tax:", tax)
print("Net income:", net)
