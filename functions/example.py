month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year): 
      return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_count_func(month, year=0):
      if not 1 <= month <= 12:
            return -1
      if month == 2 and is_leap(year): # if month is 2 and is_leap returns true
            return 29
      return month_days[month]


leap_check = is_leap(2024)
days_count = days_count_func(2,2024)

print(leap_check)
print(days_count)
