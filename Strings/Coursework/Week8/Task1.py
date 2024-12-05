dam = {True:[1234,1121],False:{'s':[12,22,12,9]},'Colleges':['BelfastMet', 'QUB', 'Ulster Uni'],0.245: 'This is a Float'}

print(dam['Colleges'][2])
print(dam[False]['s'][1])
print()

ep1 = {
    'EmployeeID':50075688,
    'EmployeeName': 'Edward Howlett',
    'Number of Experience': 5,
    'Current Position': 'Apprentice'
}

list_1 = [1,2,3,7,9,10]
list_1_empty = []
print(f'List before addition: {list_1}')

for list_item in list_1:
    list_item +=2
    list_1_empty.append(list_item)
print(f'List after addition {list_1_empty}')
print()

for emp_data in ep1:
    print(f'Employee data key: {emp_data}')
    print(f'Employee data values: {ep1[emp_data]}')

    if emp_data == 'EmployeeName':
        ep1[emp_data] = 'Eddie'
    elif emp_data == 'EmployeeID':
        ep1[emp_data] = '50075699'
    elif emp_data == 'Current Position':
        ep1[emp_data] = 'Teacher'
    else:
        ep1[emp_data] = 6
    print(f'Employee data after the change {ep1}')