# __author:jiaojiejie
# date:2019/3/24

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit(): #判断长得像不像数字，比如“200d”长得就不像数据，“200”像数据
    salary = int(salary)
else:
    #print()
    exit("must input digit") #退出程序

msg = '''
-------info of %s-------
Name:%s
Age:%s
Job:%s
Salary:%s
You will be retired in %s years 
-----------endd-----------
''' %(name, name, age, job, salary, 60-age)

print(msg)
