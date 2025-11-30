print("Привет.Я твой калькулятор.Начнем считать.")
res = int(input())
answer = "да"
while (answer != "нет"):
    x1 = res
    z = input()
    if z == "+":
        x2 = int(input())
        res = x1 + x2
    elif z == "-":
        x2 = int(input())
        res = x1 - x2
    elif z == "/":
        x2 = int(input())
        if x2 == 0:
            print("не дели на ноль дурак")
        else:
            res = x1 / x2
    elif z == "//":
        x2 = int(input())
        if x2 == 0:
            print("не дели на ноль дурак")
        else:
            res = x1 // x2
    elif z == "%":
        x2 = int(input())
        if x2 == 0:
            print("не дели на ноль дурак")
        else:
            res = x1 % x2
    elif z == "*":
        x2 = int(input())
        res = x1 * x2
    elif z == "**":
        x2 = int(input())
        res = x1 ** x2
    elif z == "sqrt":
        res = x1 ** 0.5
    print(f"Промежуточный результат = {res}.Хотите ли вы продолжить?")
    answer = input()
print(f"Итоговыйй результат! {res}")
print("количество цифр", len(str(res)))  
