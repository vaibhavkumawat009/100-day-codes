n = int(input("enter a number: "))

rev = 0
while(n>0):
    l_digit = n%10
    rev = rev*10+l_digit
    n //=10
print(rev)

