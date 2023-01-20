# Exercise 8

## Thread basics

When you start your program you start a [process](https://en.wikipedia.org/wiki/Process_(computing)) it contains at least one [thread](https://en.wikipedia.org/wiki/Thread_(computing)). But you can also start your own threads within your process. The thread is a OS feature and is lightweight compared to processes. In python we will use the high-level module [threading](https://docs.python.org/3/library/threading.html#module-threading).

Threads are used to run code in parallel, an example is your chat client. After your socket `accept` the incoming client connection, it will loop and read that single socket, but with threads your program can `recv` and `send` to multiple clients.

### Create your first thread

A [Thread](https://docs.python.org/3/library/threading.html#threading.Thread) in python has multiple keyword arguments, what we will use is:

| keyword |       usage       |
| ------- | :---------------: |
| target  |  function to run  |
| name    |    thread name    |
| args    | a tuple with args |
| daemon  | Stop with process |

1. Create a function `my_func` that has one argument `name`
   1. The function should print the name
2. add `import threading`
3. Create a Thread with target=my_func, args=("your_name",), daemon=True) assign it to a variable
4. Start your Thread with the method [.start()](https://docs.python.org/3/library/threading.html#threading.Thread.start) on your variable.
5. The program should now print "your_name"
6. We will modify the `my_func` with a [sleep](https://docs.python.org/3/library/time.html#time.sleep). Add `import time` and on the row above print(name) you should add `time.sleep(5)`
7. When you run the program it will now print nothing
8. Try to change the daemon to False when you create the Thread
9. You should now see that the program waits and prints your name. Why?
10. If we change back to daemon=True, we can use [.join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) so the main thread will wait for it to finish.
11. If you run the program now it should sleep and then print the name

### Create threads that compete

1. Create a function random_add that has two arguments `name` and `goal`
   1. The function should randomize a integer number between 1 and 10
   2. The function should sum the random numbers in a loop
   3. The loop should exit and print the name and sum, when the sum is equal or above the goal.
2. Create two Threads and name them differently
3. Start your threads
4. Add a join for each thread so the program wait
5. Run your program multiple times! Which thread wins?

## Improve your echo server

Until now your echo server has only managed one client, we will now use threads so it can handle multiple clients. You may need to refactor some code, the Thread target requires a function to run. The code run as target has to contain all the necessary code to recv and send data to the client. It also needs a loop so it don't close down the thread.

### Multiple clients

1. Create a function with a loop that can be targeted in the Thread
2. Add a loop in your main program that allows socket `accept` to run multiple times.
3. Also check the [`listen`](https://docs.python.org/3/library/socket.html#socket.socket.listen) method in docs, you may need to increase this number to allow more clients.
4. When a client has been accepted it should start a new Thread that listens to the new connection
5. Add prints so it's easy to see when a client was accepted and a new thread created
6. Try your new code, you can start multiple terminals and run 1 server and 3 clients.
7. Make sure your print out are informative, you should be able to understand which client the text shown in terminal belongs to.

### Broadcasting

1. Add a new command i.e "b" to your server, that sends a echo back to all connected clients (broadcast).
   1. To accomplish this you can save all client connection sockets to a list when created or you can use [enemurate](https://docs.python.org/3/library/threading.html#threading.enumerate).
   2. Loop over the list and send the message to all clients.
2. When using your client, you can i.e send the letter b as the command to broadcast
3. Test that all your clients get the message

## Hand in instructions

No hand in this exercise.
