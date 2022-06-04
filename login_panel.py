# python3
import json
import os

import getpass

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


class Users():

    def __init__(self):
        self.load_data(os.path.join(SCRIPT_DIR, "users_data.json"))

    def load_data(self, file_name):
        self.data = {'User': []}
        if os.path.isfile(file_name):
            with open(os.path.join(SCRIPT_DIR, file_name), "r") as file:
                self.data = json.load(file)

    # checking does input is correct
    def input_validation(self):
        if user_name in self.data["Users"]:
            return ("This user name alredy exists!")

    def password(self):
        try:
            password = getpass.getpass(prompt="Password")
            password_hash = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        except Exception as error:
            print('Incorect password', error)
            password()
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        is_num = [True for char in password if char not in numbers and True for char in password if not isupper(char)]
        if all(is_num):
            print("Password requirements: 1 number and one big letter.")
            password()

    def user_name(self):
        user_name = input("Username\t")
        if user_name in data:
            print("This login is in use")
            user_name

    def name(self):
        name = input("First name\t")

    def newuser(self):

        new_user = {"Username": user_name, "Password": password, "Name": name}
        data['User'].append(new_user)
        json.loads(data)
        with open(os.path.join(SCRIPT_DIR, "/users_data.json"), 'a') as outfile:
            json.dump(new_user, outfile)
        return "User was created"

    def sign_in(self):
        user = getpass.getuser()
        pwd = getpass.getpass("User Name : %s" % user)
        user_status = False
        for user in self.date["User_name"]:
            if user == user["User_name"]:
                user_status = True
                if pwd == user["Password"]:
                    print("Welcome")
                    return True
        if not user_status:
            print("Account was not found")
            self.sign_in()


if __name__ == "__maine__":
    main = Users()

    main.newuser()
