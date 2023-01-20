from threading import Thread


def numbers(to_number, name):
    result = 0
    for i in range(to_number):
        result += i
    print(f"{name} calculating, sum: {result}")


x = Thread(target=numbers, args=(100, 1), daemon=True)
y = Thread(target=numbers, args=(100, 2), daemon=True)


x.start()
y.start()
x.join()
y.join()
print("main program ended.")
