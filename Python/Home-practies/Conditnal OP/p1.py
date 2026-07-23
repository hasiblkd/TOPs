salary=int(input("Enter your Salary:-"))
bounse=0
new_salary=0
if salary>=50000:
    bounse=salary*0.10
    new_salary=salary+bounse
    print("Your Bounes is ",bounse)
    print("salary is ",new_salary)
else:
    bounse=salary*0.05
    new_salary=salary+bounse
    print("Your Bounes is ",bounse)
    print("salary is ",new_salary)