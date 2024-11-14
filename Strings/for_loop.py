def temp_classify():
    """

    :return: temperature classification given user prompt
    """
    user_input_temp = float(input('Please enter the current temperature in degrees: '))
    #Conditions for temperature classes
    if user_input_temp < 10: # for temperature less than 10 degrees
        return 'Cold'

    elif user_input_temp < 25:
        return 'Warm'

    else:
        return 'Hot'

if __name__ = '__main__':
    print(f'the temperature is {user_input_temp}')