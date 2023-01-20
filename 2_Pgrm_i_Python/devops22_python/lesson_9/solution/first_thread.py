# ### Create your first thread

# A [Thread](https://docs.python.org/3/library/threading.html#threading.Thread) in python has multiple keyword arguments, what we will use is:

# | keyword |       usage       |
# | ------- | :---------------: |
# | target  |  function to run  |
# | name    |    thread name    |
# | args    | a tuple with args |
# | daemon  | Stop with process |

# 1. Create a function `my_func` that has one argument `name`
#    1. The function should print the name
# 2. add `import threading`
# 3. Create a Thread with target=my_func, args=("your_name",), daemon=True) assign it to a variable
# 4. Start your Thread with the method [.start()](https://docs.python.org/3/library/threading.html#threading.Thread.start) on your variable.
# 5. The program should now print "your_name"
# 6. We will modify the `my_func` with a [sleep](https://docs.python.org/3/library/time.html#time.sleep). Add `import time` and on the row above print(name) you should add `time.sleep(5)`
# 7. When you run the program it will now print nothing
# 8. Try to change the daemon to False when you create the Thread
# 9. You should now see that the program waits and prints your name. Why?
# 10. If we change back to daemon=True, we can use [.join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) so the main thread will wait for it to finish.
# 11. If you run the program now it should sleep and then print the name


import threading
from time import sleep


def my_func(name):
    sleep(5)
    print(name)


# Don't forget the , after your name string to create a tuple
a_thread = threading.Thread(target=my_func, args=("Robert",), daemon=True)
a_thread.start()
a_thread.join()
