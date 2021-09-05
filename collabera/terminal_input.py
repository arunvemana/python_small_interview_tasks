from termcolor import colored, cprint

print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
input_red = lambda x: input(colored(x, 'red'))
input_green = lambda x: input(colored(x, 'green'))

input_validation = {'name': lambda x: x,
                    'email': lambda x: email(x),
                    'password': lambda x: password(x),
                    'user_type': lambda x: user_type(x),
                    'Age': lambda x: Age(x),
                    'cofmarks': lambda x: x,
                    'department': lambda x: x}


def email(x):
    if '@' in x:
        return x
    return False, "email should contain 'a'"


def password(x):
    if len(x) > 6:
        return x
    return False, "no of chars have to greater than 6"


def user_type(x):
    if x in ['student', 'admin']:
        return x
    return False, "user have to be in student or admin"


def Age(x):
    x = int(x)
    if x >= 18:
        return str(x)
    return False, "Age has to be >=18"


def cofmarks(x):
    pass
    # have to write.

def enter_your_choice():
    choice = input_red("Enter your choice:")
    return int(choice)
