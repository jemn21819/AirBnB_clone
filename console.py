#!/usr/bin/python3
"""
    This is the Air bnb clone Console. It works to navigate the
    Air bnb Environmet.
    Much like a shell.
"""
import re
import cmd
import json
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import classes


class HBNBCommand(cmd.Cmd):
    """ Base Command file class """

    prompt = '(hbnb) '

    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}

#
#        Console interface and behavior.
#

    def do_create(self, argv):
        """ Creates a new object based on BaseModel """
        if len(argv) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.class_dict[argv]
            except KeyError:
                print("** class doesn't exist **")
            else:
                new_obj = cls()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, argv):
        """ Prints the string representation of an instance
        given the class name and id """
        if len(argv) == 0:
            print("** class name missing **")
        else:
            line = argv.split()
            if line[0] in models.class_dict:
                try:
                    key = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[key])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, argv):
        """ Destroys an instances given the class name & id """
        args = shlex.split(argv, posix=False)
        if len(args) == 0:
            return print("** class name missing **")
        elif args[0] not in classes:
            return print("** class doesn't exist **")
        elif len(args) == 1:
            return print("** instance id missing **")
        else:
            the_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in the_dict:
                del the_dict[key]
                storage.save()
            else:
                return print("** instance not found **")

    """def do_all(self, argv):
       Prints the string representation of all instances
        based or not on the class name
        args = shlex.split(argv, posix=False)
        if len(args) == 0:
            for value in storage.all().values():
                print(value)
        else:
            if args[0] not in classes:
                print("** class doesn't exits **")
            else:
                for key, value in storage.all().items():
                    if key == "{}.{}".format(args[0], value.id):
                        print(value)"""

    def do_all(self, line):
        """some comments here"""
        if len(line) == 0:
            print([str(v) for v in models.storage.all().values()])
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if line in k])

    """def do_update(self, argv):
        Updates an instance based on the class name and id
        by adding or updating attribute
        args = shlex.split(argv, posix=False)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            the_dict = storage.all()
            key = args[0] + "." + args[1]
            if key not in the_dict:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            the_dict = storage.all()
            args[3] = args[3].strip('"')
            key = args[0] + "." + args[1]
            if key in the_dict:
                setattr(the_dict[key], args[2], args[3])
                the_dict[key].save()"""
    def do_update(self, line):
        """some comments over here"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                try:
                                    setattr(obj, attr, val)
                                except AttributeError:
                                    print("** cannot set val: {}".format(val) +
                                          " for attr: ({}) **".format(attr))
                                else:
                                    obj.save()
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """ Does nothing on (empty line + 'Enter') """
        pass
#
#        EOF and quit Functions.
#

    def do_quit(self, line):
        """ --- quit help documentation ---
        The quit function closes the console gracefully """
        return True

    def do_EOF(self, line):
        """ --- EOF help documentation ---
        EOF force closes the console.
        Use (Ctrl + D) to force close the console. """
        print()
        return True

#
# Advanced Tasks Functions
#
if __name__ == '__main__':
    HBNBCommand().cmdloop()
