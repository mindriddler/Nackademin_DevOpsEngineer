from time import sleep


def add(x, y):
    return x + y


def greet_user(name):
    return f"hello {name}"


def calculate_user_input(values):
    x, y = values
    return add(x, y)


def get_user_input(input=input):
    try:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        return x, y
    except Exception:
        print("Failed to retrieve x, y")
        return 0, 0


def main():
    while True:
        sleep(0.1)
        print(greet_user("Mr Smith"))
        print(calculate_user_input(get_user_input()))


if __name__ == '__main__':
    main()
