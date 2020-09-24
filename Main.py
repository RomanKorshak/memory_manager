from functions import allocate, free, display
from functions import HELP


def main():
    while True:
        user_input = input('>').split(' ')
        if user_input[0].lower() == 'print':
            display()
        elif user_input[0].lower() == 'allocate':
            a = allocate(int(user_input[1]))
            print(a)
        elif user_input[0].lower() == 'free':
            free(int(user_input[1]))
        elif user_input[0].lower() == 'help':
            print(HELP)
        elif user_input[0].lower() == 'exit':
            break
        else:
            print("Type 'help' for additional info.")
         

if __name__ == "__main__":
    main()