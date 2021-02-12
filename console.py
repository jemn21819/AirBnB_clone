#!/usr/bin/python3
"""

"""
import cmd
import json
import shlex
from sys import argv
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Base Command file class """

    prompt = '(hbnb) '
    intro = "Welcome to our AirBnb clone console!"
    classes = {"BaseModel", "User", "Place", "City", "Amenity",
            "State", "Review"}

#
#        Help documentation section.
#

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

#
#        Console interface and behavior.
#

    def do_create(self, cls):
        """ Creates a new object based on BaseModel """
        if len(cls) == 0 or cls == "":
            return print("** class name missing **")
        elif cls not in classes:
            return print("** class doesn't exist")
        else:
            new_obj = eval(cls)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, argv):
        """ Prints the string representation of an instance
        given the class name and id
        """
        args = shlex.split(argv)
        if len(args) == 0 or args[0] == "":
            return print("** class name missing **")
        elif args[1] not in classes:
            return print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == "":
            return print("** instance id missing **")
        else:
            the_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in the_dict:
                print(the_dict[key])
            else:
                return print("** no instance found **")

    def do_destroy(self, argv):
        """ Destroys an instances given the class name & id """
        args = shlex.split(argv)
        if len(args) == 0 or args[0] = "":
            return print("** class name missing **")
        elif args[0] not in classes:
            return print("** class doesn't exist **")
        elif len(args) = 1 or args[1] = "":
            return print("** instance id missing **")
        else:
            the_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in the_dict:
                del the_dict[key]
                storage.save()
            else:
                return print("** instance not found **)


    def emptyline(self):
        """ Does nothing on (empty line + 'Enter') """
        pass

    def postloop(self):
        """ Prints new line after exit """
        print

#
#        EOF and quit Functions.
#

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
