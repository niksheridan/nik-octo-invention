#!/usr/bin/env python
class Banner:

    def __init__(self, message):
        self.banner = message
        self.reference = "This is s default reference message"

    def print_simple_banner(self):
        print(self.banner)

    def print_pretty_banner(self):
        print('+' + '=' * 50 + '+')
        print(self.banner)
        print('+' + '=' * 50 + '+')


def main():
    banner = Banner("yesh nishe!")
    banner.print_simple_banner()
    banner.print_pretty_banner()


if __name__ == "__main__":
    main()