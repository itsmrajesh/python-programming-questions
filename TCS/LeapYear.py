def is_leap_year(year):
    year=int(year)
    if year % 4 == 0 and (year%400 == 0 or year % 100 !=0):
        print("Leap Year")
    else:
        print("Not Leap year")


is_leap_year(input())
