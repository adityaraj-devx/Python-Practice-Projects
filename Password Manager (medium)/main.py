import base64


def encode_password(password):
    return base64.b64encode(password.encode()).decode()


def decode_password(encoded_password):
    return base64.b64decode(encoded_password.encode()).decode()
    

def view():
    with open("Password Manager (medium)/password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"User: {user} \n Password: {decode_password(pwd)}")


def add():
    name = input("Account name or number: ")
    password = input("Password: ")

    with open("Password Manager (medium)/password.txt", "a") as f:
        f.write(name + "|" + encode_password(password) + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? "
    ).lower()

    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
