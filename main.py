print("Введіть число")
num = int(input("->"))

for i in range(0, num):
    for j in range(0, num):
        print('*', end=" ")
    print()