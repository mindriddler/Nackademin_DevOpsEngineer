# Exercise 6

## Instructions

### Brainstorm server/client

1. Think about servers you have used before
2. Think about clients you have used before

### Practice on OOP and TDD

Choice a server or client from previous task, start writing code but skip the socket parts for now.
    - The code should be written with tests
    - The code should be object oriented
    - Client and server code should not be in the same file

```python
# Example

class Lobby:

    servers = ["127.0.0.1", "192.168.1.1"]

    def list_servers(self):
        return self.servers


# With tests

from lesson_6.lobby import Lobby


class TestLobby:

    def test_list_servers(self):
        assert isinstance(Lobby().list_servers(), list)

    def test_list_servers_has_ip(self):
        assert Lobby().list_servers()[0] == "127.0.0.1"

```

## Hand in instructions

No hand in this exercise.
