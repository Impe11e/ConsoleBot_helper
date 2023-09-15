from handler import *

COMMANDS = {
    'change': change,
    'phone': phone,
    'add': add,
    'show': show_all,
    'good': exit,
    'close': exit,
    'exit': exit}

def main():
    while loop:
        user_input = str(input("Enter the command: "))
        command_parts = user_input.split(' ')
        command = command_parts[0].lower()
        params = " ".join(command_parts[1:])
        if '.' in user_input:
            break
        elif user_input.lower() in ["good bye", "close", "exit"]:
            print('Good Bye!')
            return exit()
        elif command in COMMANDS:
            result = handle_command(command, params)
            if result:
                print(result)
        else:
            result = handle_command(command, params)
            print(result)

@decorator
def handle_command(command, params):
    func = COMMANDS.get(command)
    return func(params)

if __name__ == "__main__":
    main()