from woodmill_server import ControlCentral

# Client without sockets
# TODO replace direct access with socket
# TODO Add CMD


def main():
    control = ControlCentral()
    control.start()

    # Get status
    print(control.status())

    # produce lumber
    control.saw.cut()
    control.saw.cut()
    control.saw.cut()

    # see stats
    print(control.stats.proccessed_trees())

    # Close down
    control.stop()

    # Get status
    print(control.status())


if __name__ == '__main__':
    main()
