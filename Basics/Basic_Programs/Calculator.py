# calculator program -

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = mun1 - num2
    print(result)

elif operator == "*":
    result = mun1 * num2
    print(result)

elif operator == "/":
    result = mun1 / num2
    print(result)
    # print(round(result))

else :
    print(f"{operator} is not valid operator")