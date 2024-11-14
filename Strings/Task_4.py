s = "eddie howlett"
s = s.capitalize()
print(s)
if s.startswith("eddie"):
    print("The string starts with 'eddie'.")
else:
    print("The string does not start with 'eddie'.")
    if s.endswith("howlett"):
        print("The string ends with 'howlett'.")
    else:
        print("The string does not end with 'howlett'.")