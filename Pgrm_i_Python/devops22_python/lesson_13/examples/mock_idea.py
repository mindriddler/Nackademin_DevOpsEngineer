
# A fake conn that just ignore calls
class fake_conn:
    def sendall(self, text):
        pass


# A function we want to verify the return, and ignore the conn sendall
def do_someting(conn):
    text = "wadawdaw"
    conn.sendall(text)
    return text


# This would be in the pytest file
assert "wadawdaw" == do_someting(fake_conn())
