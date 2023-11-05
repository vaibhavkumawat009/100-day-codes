n = int(input("input a number: "))

first = 0
second = 1
print(first,second,end = ' ')
for i in range(0,n-2):
    final =first+second
    first = second
    second = final
    print(final,end = ' ')
