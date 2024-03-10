#!/usr/bin/python
"""
command line interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class command-line interface.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Help message for quit command
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handles EOF (Ctrl+D) to exit the program
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
