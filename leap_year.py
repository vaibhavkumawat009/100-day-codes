def leap_year(number):
    if(number%4==0):
      return "its leap year"
    else:
        return "not a leap year"

n = int(input("give a number: "))

print(leap_year(n))
