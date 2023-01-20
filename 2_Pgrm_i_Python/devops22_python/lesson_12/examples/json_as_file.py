import json


def main():

    with open("lesson_12/examples/my_json.json") as f:
        my_meetings = json.loads(f.read())
        # You can also load it directly with my_meetings = json.load(f)
        print(my_meetings)
        print(my_meetings["meetings"][0])


if __name__ == '__main__':
    main()
