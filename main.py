"""This project is an account creation & manager program. It checks whether or not you have created an account before, if an account exists it asks for a password. 
If the password is right you are granted access. If not you are denied access. If an account doesn't exist then it asks for a new password, and also confirms the password.
If the password isn't confirmed it loops back and asks you to try again. This program utilizes a database using a csv file to check for existing accounts, and adding new accounts."""

v = 0
print("Please type a username\n")
username = str(input())

# Opens database and appends usernames and passwords into list. 
with open("database.csv") as file:
    data = []
    for i in file:
        data.append(str(i))

# Because each element (except last) ends with '\n', they will have :-1 to get the '\n' taken out (except last).
for x in range(len(data)):
    if data[x] != data[-1]:
        data[x] = data[x][:-1]


if username in data: # if username is in list, then take the index of username, and enters specific password. Or else create a new account.
    index = data.index(username)
    print("Please enter your password\n")
    password = str(input())
    if password == data[index+1]: # passwords are the index after the username
        print("ACCESS GRANTED"), print("\n"), print("Welcome User")
    else:
        print("ACCESS DENIED")
else:
    while v == 0: # resets if password is not confirmed, aka doesn't add 1 to v. If password is appended to database then loop ends, aka adding 1 to v
        print("Please enter a password\n")
        password = str(input())
        print("Confirm password\n")
        password2 = str(input())
        if password == password2:
            with open("database.csv", 'a+') as file:
                file.write(f"\n{username}\n{password}")
            print("Account stored in database, please log in again!\n")
            v += 1
        else:
            print("Passwords do not match, please try again!\n")

input('Press ENTER to exit') # Asks for input so file doesn't close, pressing ENTER closes file