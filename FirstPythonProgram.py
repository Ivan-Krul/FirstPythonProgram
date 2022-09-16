# Calculator
a = float(input("A:"))
sym = input("operator:")
b = float(input("B:"))

if sym == "+":
    print(a+b)
elif sym == "-":
    print(a-b)
elif sym == "*":
    print(a*b)
elif sym == "/":
    if b == 0:
        print("B mustn't be 0")
    else:
        print(a/b)
else:
    print("operator is not defined")
