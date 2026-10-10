a = float(input("First number: "))
operator = input("Operator (+ - * /): ").strip()
b = float(input("Second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero.")
        raise SystemExit
    result = a / b
else:
    print("Invalid operator.")
    raise SystemExit

print("Result:", result)
