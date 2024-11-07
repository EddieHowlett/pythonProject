def employee_pay():
    hourly_rate = float(input(f'Please enter your hourly rate, eg 10.59: '))
    num_hours_worked = float(input(f'Please enter your number of hours worked, eg 40: '))
    emp_pay = hourly_rate * num_hours_worked
    emp_pay = f'£{emp_pay}'
    return emp_pay

#given a list of ages write a function to find the average#
# list_of_ages = [20, 21, 24, 13,15, 19, 22]
def average_age(ages_list:list):
    """
    :param ages_list: should a list of ages, expecting the data type to be a list
    :return: average age in float
    """
    sum_ages = sum(ages_list) #This will give us a sum of the ages#
    num_ages = len(ages_list) #Get the number of ages in the list#
    avg_list = sum_ages / num_ages # This is the average age#
    return avg_list

list_ages_1 = [20, 21, 24, 13,15, 19, 22]
ave_age = average_age(list_ages_1)
print(f'The average age is {ave_age} years')

#1. Ask the user for their hourly rate
#2. Ask the user for the number of hours worked
#3. Multiply 1 and 2 to gt the pay of the employee
#4. Return value in 3

empy_pay = employee_pay()
print(f'Employee pay is {empy_pay}')
