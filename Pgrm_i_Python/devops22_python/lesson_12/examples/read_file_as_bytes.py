def main():
    with open('lesson_12/examples/cat.jpg', 'rb') as f:
        while True:
            to_send = f.read(4096)
            if not to_send:
                break
            print(len(to_send))
            # Send over socket


if __name__ == '__main__':
    main()
