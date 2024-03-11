#!/usr/bin/python3
"""command-line interface."""

import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User




class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]
    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass
    def do_EOF(self, line):
        """Exit on EOF."""
        print()
        return True
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    def do_create(self, arg):
        """
          Create a new instance of BaseModel and save it to the JSON file.
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)
    def do_show(self, arg):
        """
        Show the string representation of an instance.
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")
    def do_all(self, arg):
        """Print the string representation of all instances or a specific class."""
        objects = storage.all()
        commands = shlex.split(arg)
        print(f"{commands = }")
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))
    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
    def default(self, arg):
        """
        Default behavior for cmd
        """
        arg_list = arg.split('.')
        incoming_class_name = arg_list[0]

        command = arg_list[1].split('(')

        incoming_method = command[0]
        incoming_xtra_arg = command[1].split(')')[0]
        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if incoming_method in method_dict.keys():
            return method_dict[incoming_method]("{} {}".format(incoming_class_name,incoming_xtra_arg))

        print("*** Unknown syntax: {}".format(arg))
        return False
    def do_count(self, arg):
        """
        Counts and retrieves the number of instances
        """
        objects = storage.all()

        commands = shlex.split(arg)
        if arg:
            incoming_class_name = commands[0]

        count = 0

        if commands:
            if incoming_class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == incoming_class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
