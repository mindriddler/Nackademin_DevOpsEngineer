from selectors import EVENT_READ, EVENT_WRITE

LINE = "---------------------------\n"

print("---------------------------")
print(f'EVENT_READ:  {EVENT_READ:08b}')
print(f'EVENT_WRITE: {EVENT_WRITE:08b}')
print(LINE)

print("----------- & 1 -----------")
print(f"1 - {1:08b}")
print(f"EVENT_READ & 1:  {EVENT_READ & 1:08b}")
print(f"EVENT_WRITE & 1: {EVENT_WRITE & 1:08b}")
print(LINE)

print("----------- & 2 -----------")
print(f"2 - {2:08b}")
print(f"EVENT_READ & 2:  {EVENT_READ & 2:08b}")
print(f"EVENT_WRITE & 2: {EVENT_WRITE & 2:08b}")
print(LINE)

print("----------- & 3 -----------")
print(f"3 - {3:08b}")
print(f"EVENT_READ & 3:  {EVENT_READ & 3:08b}")
print(f"EVENT_WRITE & 3: {EVENT_WRITE & 3:08b}")
print(LINE)


"""
    0 & 1

    0000 0000
    0000 0001
    & -------
    0000 0000

    1 & 1
    0000 0001
    0000 0001
    & -------
    0000 0001

    2 & 2
    0000 0010
    0000 0010
    & -------
    0000 0010

    2 & 1
    0000 0010
    0000 0001
    & -------
    0000 0000

"""
