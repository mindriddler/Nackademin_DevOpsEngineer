import json


def create_meeting(name, time, location):
    return {"name": name, "time": time, "location": location}


def meeting_to_bytes(meeting):
    # Convert string to bytes
    to_send = json.dumps(meeting).encode()
    print(f"meeting_to_bytes: {to_send}")
    return to_send


def bytes_to_meeting(bytes):
    data = json.loads(bytes)
    print(f"bytes_to_meeting: {data}")
    return data


def main():
    my_meetings = []
    meeting = create_meeting("Läkaren", "12:00", "Vårdcentralen")
    my_meetings.append(meeting)
    print(f"Meeting as python object: {my_meetings}")

    # Send bytes over network
    bytes_to_send = meeting_to_bytes(my_meetings)

    # FAKE transfer
    received_over_network = bytes_to_send

    # The receiver can convert back to a python object with
    bytes_to_meeting(received_over_network)


if __name__ == '__main__':
    main()
