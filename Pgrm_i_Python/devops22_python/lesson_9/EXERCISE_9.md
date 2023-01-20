# Exercise 9

## Thread

### Client improvement

Until now your client has been waiting for input then sending it to the server, afterwards it assume you get a recv. We will use threads to improve the client so it can read and write simultaneously. If you want a perfect user experience [EXTRA] you should probably use your TK GUI, since the terminal doesn't play well when waiting for a input and printing at the same time.

1. If you don't have a loop yet in the client. Add a loop so it will:
   1. Ask for input (with command)
   2. Send the input to the server
   3. recv the echo from server
   4. print the recv message

2. Create a function that handles:
   - recv messages from the server
   - it prints the message from the server
   - [Extra] refactor your function into functions with a single responsibility

3. Start the recv & print function as a thread.
4. [Extra] what happens when the server connection is closed? Does the thread stop without errors?
5. [Extra] what happens when you close down your client, does the thread stop?
6. Manually test your client:
   1. Does it work to send message to the server?
   2. Does it work to recv message from the server?
   3. Does it work to recv broadcast messages from the server?
   4. What happens if you recv a message while typing?

### Server improvement

The server must be available so clients can connect and send messages. So it's important the server doesn't crash. We will improve the error handling and thread handling.

1. Connect multiple client to your server
2. Send a broadcast message
3. Close down one client, wait 1 minute and send a broadcast message again
   - Does the server crash or handles the broken connection?
4. Make sure your server:
   - Client errors are handled, WARNING if you catch exceptions the thread may continue to run.
   - Old client threads are closed down
   - Add a command quit that allows the client to by them self shutdown

5. [EXTRA] Add a possibility as a client to close down the server and all clients
   - A client sends the command "self destruction"
   - The server will start the countdown 10, 9, 8 ..
   - All Clients are disconnected
   - All threads are joined
   - [EXTRA EXTRA] if a client can guess the defuse number 1-100. The shutdown is aborted.

## Hand in instructions

No hand in this exercise.
