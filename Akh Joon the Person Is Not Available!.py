_ = input()
first_list = input().split()
_ = input()
second_list = input().split()
_ = input()
third_list = input().split()
days_of_week = ["shanbe","1shanbe","2shanbe","3shanbe","4shanbe","5shanbe","jome"]
c = sum(map(lambda day: day not in first_list and day not in second_list and day not in third_list, days_of_week))
print(c)