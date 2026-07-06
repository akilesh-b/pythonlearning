import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Employee_Name": ["Ravi", "rathina", "lavanya", "ramu",
                      "eswaran", "kova", "harini", "dharshini"],
    "Department": ["Sales", "Procurement", "Warehouse", "Finance",
                   "Logistics", "Sales", "Warehouse", "Finance"],
    "Salary": [45000, 55000, 40000, 70000,
               50000, 48000, 42000, 75000]
}

df = pd.DataFrame(data)

print("\nWHOLESALE COMPANY EMPLOYEE DATA")
print(df)

avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAVERAGE SALARY BY DEPARTMENT")
print(avg_salary)


total_salary = df.groupby("Department")["Salary"].sum()

print("\nTOTAL SALARY EXPENDITURE BY DEPARTMENT")
print(total_salary)

employee_count = df.groupby("Department")["Employee_ID"].count()

print("\nNUMBER OF EMPLOYEES IN EACH DEPARTMENT")
print(employee_count)

max_salary = df["Salary"].max()

highest_paid_employee = df[df["Salary"] == max_salary]

print("\nHIGHEST-PAID EMPLOYEE")
print(highest_paid_employee)


highest_payroll_dept = total_salary.idxmax()

print("\nDEPARTMENT WITH HIGHEST PAYROLL COST")
print(highest_payroll_dept)