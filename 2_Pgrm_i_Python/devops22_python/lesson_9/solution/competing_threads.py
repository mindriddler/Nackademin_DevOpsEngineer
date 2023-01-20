# ### Create threads that compete

# 1. Create a function random_add that has two arguments `name` and `goal`
#    1. The function should randomize a integer number between 1 and 10
#    2. The function should sum the random numbers in a loop
#    3. The loop should exit and print the name and sum, when the sum is equal or above the goal.
# 2. Create two Threads and name them differently
# 3. Start your threads
# 4. Add a join for each thread so the program wait
# 5. Run your program multiple times! Which thread wins?


from random import randint
from threading import Thread


def random_add(name, goal):
    result = 0
    while result < goal:
        random_value = randint(1, 10)
        result += random_value
    print(f"Thread [{name}] has finished with the result {result}")


thread_1 = Thread(target=random_add, args=("Thread1", 100000))
thread_2 = Thread(target=random_add, args=("Thread2", 100000))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
