EmployeeData = {
    'A':{
        'EmployeeID':123232,
        'EmployeeName': 'Robert Williams',
        'Number of Experience': 16,
        'Current Position': 'IT Manager',
        'Salary': 75000,
         },
    'B': {
        'EmployeeID':219836,
        'EmployeeName': 'Ramon Kapur',
        'Number of Experience': 27,
        'Current Position': 'Plant Manager',
        'Salary': 95212
        },
    'C': {
        'EmployeeID': 100212,
        'EmployeeName': 'Philie Torres',
        'Number of Experience': 32,
        'Current Position': 'CEO',
        'Salary': 923123
        },
    'D': {
        'EmployeeID': 311231,
        'EmployeeName': 'Gail Munes',
        'Number of Experience': 0,
        'Current Position': 'Machine Learning Intern',
        'Salary': 45419
         },
    'E': {
        'EmployeeID': 221092,
        'EmployeeName': 'Fedrick Zocco',
        'Number of Experience': 2,
        'Current Position': 'Research Scientist',
        'Salary': 118910
        }
}


for key, value in EmployeeData.items():
    name = value['EmployeeName']
    annual_salary = value['Salary']
    monthly_salary = annual_salary/12
    print(f"{name}'s monthly salary is £{monthly_salary:.2f}")

print()

for emp_data in EmployeeData:

    annual_salary = EmployeeData[emp_data]['Salary']
    employee_names = EmployeeData[emp_data]['EmployeeName']
    monthly_salary = annual_salary/12
    print(f'The monthly salary of {employee_names} is {monthly_salary:.2f}')