#!/usr/bin/python3
"""
    This is the Air bnb clone Console. It works to navigate the
    Air bnb Environmet.
    Much like a shell.
"""
import re
import cmd
import models
from datetime import datetime


def pattern(arg):
    """ Changing the default input function to manage callable functions """
    pattern = '\.([^.]+)\(|([^(),]+)[,\s()]*[,\s()]*'
    argum = re.findall(pattern, arg)
    cmd = argum[0][0]
    argum = argum[1:]
    line = ' '.join(map(lambda x: x[1].strip('"'), argum))
    return cmd, line


def loop_dict(line, obj_update):
    """ looping function for the adv tasks"""
    idx = 4
    while idx <= len(line):
        try:
            attr = line[idx]
        except IndexError:
            print("** attribute name missing **")
        else:
            try:
                val = line[idx + 1]
            except IndexError:
                print("** no value found **")
            else:
                setattr(obj_update, attr, val)
                obj_update.save()
                if idx + 1 == len(line) - 1:
                    break
        idx += 1


class HBNBCommand(cmd.Cmd):
    """ Base Command file class """

    prompt = '(hbnb) '

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
        if len(argv) == 0:
            return print("** class name missing **")
        else:
            line = argv.split()
            if line[0] in models.class_dict:
                try:
                    key = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """rints all string representation of all instances
        based or not on the class name"""
        if len(line) == 0:
            print([str(v) for v in models.storage.all().values()])
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if line in k])

    def do_update(self, line):
        """pdates an instance based on the class name and id by
        adding or updating attribute"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split(' ')
            for i in range(len(line)):
                line[i] = line[i].strip("\"'\"{\"}:\"'")
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
                                setattr(obj, attr, val)
                                obj.save()
                                if len(line) >= 5:
                                    loop_dict(line, obj)
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """ Counts the number of instances of a class """
        instance_cnt = 0
        curr_dict = models.storage.all()
        for key, val in curr_dict.items():
            val = val.to_dict()
            if val['__class__'] == line:
                instance_cnt += 1
        print(instance_cnt)

    def do_Amenity(self, arg):
        """ helper function for amenity class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Amenity', line]))

    def do_User(self, arg):
        """ Helper function for User class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'User', line]))

    def do_BaseModel(self, arg):
        """ Helper function for BaseModel Class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'BaseModel', line]))

    def do_City(self, arg):
        """ Helper function for BaseModel Class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'City', line]))

    def do_Review(self, arg):
        """ Helper function for Review class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Review', line]))

    def do_State(self, arg):
        """ Helper function for State class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'State', line]))

    def do_Place(self, arg):
        """ Helper function for Place class"""
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Place', line]))

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
