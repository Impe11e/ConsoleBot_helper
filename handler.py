import re

loop = True
USERS_DATA = {}

def decorator(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No such name found. Try again.'
        except ValueError:
            return 'Incorrect data entered. Please, try again.'
        except IndexError:
            return 'You have to enter code!'
        except Exception as e:
            return f"Invalid command {e}. Please try again."
    return inner

@decorator
def add(user_input):
    name, phone_number = user_input.split(' ')
    pattern = r'^\+\d{1,16}$'
    if name not in USERS_DATA.keys():
        if re.match(pattern, phone_number):
            USERS_DATA[name] = phone_number
        else:
            raise ValueError
    else:
        raise ValueError


@decorator
def phone(user_input):
    phone_number = USERS_DATA.get(user_input)
    print(f'{phone_number}')


@decorator
def exit():
    global loop
    loop = False

@decorator
def show_all(params):
    for name, phone_number in USERS_DATA.items():
        return f'{name}: {phone_number}'

@decorator
def change(user_input):
    name, new_phone_number = user_input.split(' ')
    pattern = r'^\+\d{1,16}$'
    if name in USERS_DATA:
        if re.match(pattern, new_phone_number):
            USERS_DATA[name] = new_phone_number
        else:
            raise ValueError
    else:
        raise KeyError
