def Calculator():
    a = int(input("Enter nubmer 1 : "))
    operator = input("Enter operator (+,-,*,/) : ")
    b = int(input("Enter number 2 : "))

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if operator != 0:
            result = a / b
        else:
            print("Error! Division by Zero")
    else:
        print("Invalid operator")

    print(f"The result of num1: {a} operator: ({operator}) and num2: {b} is: {result}")

Calculator()