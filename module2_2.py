first = int(input("Введит первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третие число: "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)