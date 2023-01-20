from time import time
from random import randint

observations = []


def parse_agent_observation(data):
    time, temp = data.split(",")
    return {'time': time, "temp": temp}


def main():
    data_from_agent = f"{int(time())},{randint(15,30)}"
    print("------ SERVER RECV DATA -----")
    print(data_from_agent)
    # IN server save recvied data
    observations.append(parse_agent_observation(data_from_agent))
    print("-------------------")

    # in client send more data
    data_from_agent = f"{int(time())},{randint(15,30)}"
    print("------ SERVER RECV DATA -----")
    print(data_from_agent)
    # IN server save recvied data
    observations.append(parse_agent_observation(data_from_agent))
    print("-------------------")

    # If client asks to list send observations to client

    print("------ CLIENT LIST -----")
    print(observations)
    print("-------------------")


if __name__ == '__main__':
    main()
