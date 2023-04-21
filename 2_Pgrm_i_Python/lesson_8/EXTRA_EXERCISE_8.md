# EXTRA Exercise 8

## Instructions

### EXTRA file transfer

When you send more than the byte buffer allows you face a new problem. You will need to split the bytes and send multiple times. The method `sendall` will help you with this, but you still need to `recv` and puzzle the binary back together.

1. Add the feature to read a text file
2. Add the feature to send a file that the server saves on disk
3. If the file contains the word "sandwich" the server response with "yummy!"
4. If the file contains the word "devops" the server response with "of course!"
5. If the file contains the word "Coffee" the server response with "hot please"
6. If the file contains more than one of words (sandwich, devops, coffee) it should send a combined response to the client.
7. Test to send a bigger file (1MB), i.e a wordlist or a generated file.

### EXTRA Struct

To be able to send different type of data i.e negative numbers, it helps with the struct module.

1. Try to send a negative numbers without struct, how would you solve it?
2. Adapt your server and client to use [struct](https://docs.python.org/3/library/struct.html)

## Hand in instructions

No hand in this exercise.
