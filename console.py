#!/usr/bin/python3
"""
A command interpreter for the AirBnB project.
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program using EOF (Ctrl+D)
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class name>
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in [cls._name_ for cls in BaseModel._subclasses_()]:
                new_obj = BaseModel()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance.
        Usage: show <class name> <id>
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representations of all instances.
        Usage: all [class name]
        """
        args = shlex.split(line)
        obj_list = []

        if not args:
            for key, obj in storage.all().items():
                obj_list.append(str(obj))
        elif args[0] in storage.all_classes():
            for key, obj in storage.all_classes()[args[0]].values():
                obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            attribute_value = args[3].strip("\"'")
            obj = storage.all()[key]
            if hasattr(obj, attribute_name):
                setattr(obj, attribute_name, attribute_value)
                obj.save()
            else:
                print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
