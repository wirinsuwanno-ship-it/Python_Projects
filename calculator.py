n1 = int(input("enter 1st number"))
n2 = int(input("enter 2nd number"))
op = str(input("enter operator"))

def add():
    print(n1 + n2)

def sub():
    print(n1 - n2)

def mul():
    print(n1 * n2)

def div():
    print(n1 / n2)

def mod():
    print(n1 % n2)

def pow():
    print(n1 ** n2)

def unknown():
    print("error: please try again and/or enter valid values")

if op == "+":
    add()
elif op == "-":
    sub()
elif op == "*":
    mul()
elif op == "/":
    div()
elif op == "%":
    mod()
elif op == "**":
    pow()
else:
    unknown()
