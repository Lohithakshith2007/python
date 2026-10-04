username=input("enter your username: ")
password=input("enter your password: ")

correct_username = "lohith"
correct_password = "lohith123"
is_admin=True

login_message=f"login successful.\nwelcome {username}"
access="admin" if is_admin else "user"

if username == correct_username and password == correct_password:
    print(login_message)
    print(f'{access} access granted')
elif username != correct_username:
    print("incorrect username")
else:
    print("incorrect password")
