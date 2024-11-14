def check_cpu(cpu_usage):
    # I am creating a function using if, else, and elif statements to check the users CPU usage

    if cpu_usage < 40:
        return "Underutilized"
        # If the user enters a value less than 40 the message "underutilized" will be displayed

    elif cpu_usage >= 40 and cpu_usage <= 75:
        return "Optimal"
        # If the user enters a value more than or equal to 40 and less than or equal to 75 the message will say "Optimal"

    else:
        return "Overloaded"
        # For any value over 75 that is entered a message saying "Overloaded" will be displayed


def check_memory(memory_usage):
    # I am creating a function using if, else, and elif statements to check the users memory usage

    if memory_usage < 4:
        return "Underutilized"
        # If the user enters a number less than 4 the message "Underutilised" will be displayed

    elif memory_usage >= 4 and memory_usage <= 8:
        return "Optimal"
        # If the user enters a value more than or equal to 4 and less than or equal to 8 the message will say "Optimal"

    else:
        return "Overloaded"
        # If the user enters a value more than 8 the message "Overloaded" will be displayed


def main():
    # Here I am creating the main user interface which the user will interact with

    print("Welcome to the System Health Monitoring Bot.")
    # I created a string that will appear to allow users to know that they are running the System Health Monitoring Bot program

    cpu = float(input("Please enter you CPU usage in percentage (0-100), eg 72: "))
    # Above I used the float function to convert the users input into floating point value so python can return the correct message

    memory = float(input("Please eneter your memory usage is GB, eg 6GB: "))
    # I created the same function for the memory input as the user should be typing integers into both

    if cpu < 0 or cpu > 100:
        print("You must enter a number between 0-100.")
        return
        # Here I have set boundaries so users can only enter integers between 0 and 100

    if memory < 0:
        print("You must enter a positive number.")
        return
        # Here I have created a boundary so users can only input positive integers

    cpu_call = check_cpu(cpu)
    # This will call the check_cpu function and store the results from this as a variable

    memory_call = check_memory(memory)
    # This will call the check_memory function and store the results from this as a variable

    print(f'Your CPU usage is curretnly at: {cpu}% which means your system is currently: {cpu_call}')
    print(f'Your Memory usage is currently at: {memory}GB which means your system is currently: {memory_call}')
    # These print statements will display to the user what state that their CPU and Memory is currently running at

    if cpu_call == "Underutilized" and memory_call == "Underutilized":
        print("Your entire system is currently being underutilized!")

    elif cpu_call == "Optimal" and memory_call == "Optimal":
        print("Your entire system is optiaml congratulations!")

    elif cpu_call == "Overloaded" and memory_call == "Overloaded":
        print("Your entire system is overloaded. Please contact your IT team!")

    elif cpu_call == "Optimal" and memory_call == "Underutilized":
        print("Your CPU is optimised, but your memory is being underutilized.")

    elif cpu_call == "Optimal" and memory_call == "Overloaded":
        print("Your CPU is optimised, but your memory is being overloaded. Please contact your IT team!")

    elif cpu_call == "Underutilized" and memory_call == "Optimal":
        print("Your memory is optimised, but you CPU is being underutilzsed.")

    elif cpu_call == "Overloaded" and memory_call == "Optimal":
        print("Your memory is optimised, but your CPU is overloaded. Please contact your IT team!")

    elif cpu_call == "Overloaded" and memory_call == "Underutilized":
        print("Your CPU is overloaded, and your memory in underutilized. Please contact your IT team!")

    elif cpu_call == "Underutilized" and memory_call == "Overloaded":
        print("Your CPU is underutilized, and your memory in overloaded. Please contact your IT team!")
        # I used the if, elif, and else and 'and' function to change the displayed method based upon the users feedback


if __name__ == "__main__":
    main()