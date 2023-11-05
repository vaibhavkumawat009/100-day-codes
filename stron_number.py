def facto(number):
    if (number==0):
        return 1 
    else:
        return number*facto(number-1)

def is_strong(number):
    final = 0
    while(number>0):
        l = number%10
        final = facto(l)+final
        number //=10
    return final




n = int(input("give a number: "))
a = is_strong(n)

if(n==a):
    print("its a strong number")
else:
    print("not a stong number")
