def check_user_password():
    student_ID = ['12345', '456781', '23456', '123456']
    student_password = ['password123', 'password', 'passwd', 'PASSWORD']
    ID_attempts = 0
    while True:
        user_input = input(f'Please enter your student ID here: ')
        ID_attempts += 1
        if user_input in student_ID and ID_attempts <3:
            student_pssword = input(f'Please enter your password here: ')
            if student_pssword in student_password:
                print(f'You have been logged in\n Welcome Back!')
                break
            else:
                print(f'You have entered the wrong password please try again')
        elif user_input not in student_ID and ID_attempts < 3:
            continue

        else:
            print(f'You have entered wht wrong student ID please try again')
if __name__ == '__main__':
    check_user_password()