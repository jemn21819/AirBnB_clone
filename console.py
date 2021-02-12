#!/usr/bin/python3
"""

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Base Command file class """

    prompt = '(hbnb) '
    intro = "Welcome to our AirBnb clone console!"

    """
        Help documentation section.
    """

    def do_help(self, args):
        """
    --- Get help on commands ---

        'help' or '?' with no arguments prints a list of available
         commands for which help is available

        'help <command>' or '? <command>' gives help on <command>

        """
# The only reason to define this method is for/
# the help method to appear in the docstring
        cmd.Cmd.do_help(self, args)

    """
        Console interface and behavior.
    """

    def emptyline(self):
        """ Does nothing on (empty line + 'Enter') """
        pass

    def postloop(self):
        """ Prints new line after exit """
        print

    """
        EOF and quit Functions.
    """

    def do_quit(self, line):
        """
    --- quit help documentation ---

        The quit function closes the console gracefully
        """
        return True

    def do_EOF(self, line):
        """
    --- EOF help documentation ---

        EOF force closes the console.

        Use (Ctrl + D) to force close the console.
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
