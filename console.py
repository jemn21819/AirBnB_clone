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
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


def pattern(arg):
    """
    Retrieve the cmd method and the respective arguments according
    to a pattern so that they can be invoked under this scheme:
    <class>. <cmd> ([args, ...])
    """
    pattern = '\.([^.]+)\(|([^(),]+)[,\s()]*[,\s()]*'
    argmt = re.findall(pattern, arg)
    cmd = argmt[0][0]
    argmt = argmt[1:]
    line = ' '.join(map(lambda x: x[1].strip('"'), argmt))
    return cmd, line


def loop_dic(line, obj_upt):
    """
    Loop for update with format:
    <class name>.update(<id>, <dictionary representation>)
    """
    j = 4
    while j <= len(line):
        try:
            atrribute = line[j]
        except IndexError:
            print("** attribute name missing **")
        else:
            try:
                value = line[j+1]
            except IndexError:
                print("** value missing **")
            else:
                setattr(obj_upt, atrribute, value)
                obj_upt.save()
                if j+1 == len(line) - 1:
                    break
        j += 1


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
                cls = models.classes[argv]
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
            line = argv.split(' ')
            if line[0] in models.classes:
                try:
                    key = line[0] + "." + line[1]
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
        if len(argv) == 0:
            print("** class name missing **")
        else:
            line = argv.split(' ')
            if line[0] in models.classes:
                try:
                    key = line[0] + "." + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        objects = storage.all()
                        models.storage.delete(objects[key])
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, argv):
        """ Prints the string representation of all instances
        based or not on the class name """
        if len(argv) == 0:
            print([str(value) for value in models.storage.all().values()])
        elif argv not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items()
                   if argv in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            for i in range(len(line)):
                line[i] = line[i].strip("\"'\"{\"}:\"'")
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj_upt = models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            atrribute = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                value = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                setattr(obj_upt, atrribute, value)
                                obj_upt.save()
                                if len(line) >= 5:
                                    loop_dic(line, obj_upt)
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """ Does nothing on (empty line + 'Enter') """
        pass

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
