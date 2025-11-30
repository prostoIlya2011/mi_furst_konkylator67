print("Привет.Я твой калькулятор.Начнем считать.)

answer = "да"
while (answer != "нет"):
    x1 = int(input())
    z = input()
    if z == "+":
        x2 = int(input())
        res = x1 + x2
    elif z == "-":
        x2 = int(input())
        res = x1 - x2
    elif z == "/":
        x2 = int(input())
        res = x1 / x2
    elif z == "//":
        x2 = int(input())
        res = x1 // x2
    elif z == "%":
        x2 = int(input())
        res = x1 % x2
    elif z == "*":
        x2 = int(input())
        res = x1 * x2
    elif z == "**":
        x2 = int(input())
        res = x1 ** x2
    elif z == "sqrt":
        res = x1 ** 0.5
