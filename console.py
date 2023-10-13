#!/usr/bin/python3
"""
Command interpreter for the HBNB project.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # Set your custom prompt

    def do_quit(self, arg):
        """
        Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using EOF (Ctrl +D)
        """
        print("")  # Print a newline
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
