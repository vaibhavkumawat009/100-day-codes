def facto(number):
    if (number == 0):
        return 1
    else:
        return number*facto(number-1)

n = int(input("give a number: "))

print(facto(n))
