#!/usr/bin/env python3
"""Defines the command interpreter that manages
(i.e creates, updates, retrieve, etc ..)the objects in our storage"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex


CLASSES = ["BaseModel"]


def check_args(args):
    """checks if arguments passed in line are valid
    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        An error message if args is none or if args is not a valid class"""

    args_list = shlex.split(args)

    if not args_list:
        print("** class name is missing **")
    elif args_list[0] not in CLASSES:
        print("** class does not exists **")
    else:
        return args_list


class CLI(cmd.Cmd):
    """Defines the methods that the command interpreter use to
    manage objects in storage"""

    prompt = "CLI:$ "
    intro = "Welcome to the Creatives Connect Command Line Interpreter!\n\n\
        Please input help or ? to display the commands available\n\
            Input help <command name> | ? <command name> to display\
                a command's usage"

    def emptyline(self):
        """An empty line + ENTER in our command interpreter should not
        execute anything"""
        pass

    def do_EOF(self):
        """End of file: exit the program"""
        return True

    def do_quit(self):
        """Exits the program"""
        exit()

    def postloop(self):
        """Executed when our cmd is about to return"""
        print()

    def do_create(self, line):
        args = check_args(line)
        if args:
            print(f'Object {args[0]}.{eval(args[0])().id} has been created!')
            storage.save()

    def help_create(self):
        print("\n".join([
            "create: create <class name>",
            "        Create a new instance of the class specified\
                and prints its id."
        ]))

    def do_show(self, line):
        args = check_args(line)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                obj = storage.get(args[0], args[1])
                if obj:
                    print(obj)
                else:
                    print("** instance not found **")

    def help_show(self):
        print("\n".join([
            "show: show <class name> <instance id>",
            "      Prints the string representation of an instance\
                based on its class name and id"
        ]))

    def do_all(self, line):
        args = shlex.split(line)
        objs = storage.all().values()

        if not args:
            print([str(obj) for obj in objs])
        else:
            if args[0] not in CLASSES:
                print("** class does not exists **")
            else:
                print([str(obj) for obj in objs if args[0] in str(obj)])

    def help_all(self):
        print("\n".join([
            "all: all [class name]",
            "     Prints the string representation of all instances\
                based on their class name"
        ]))

    def do_destroy(self, line):
        args = check_args(line)
        if args:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*args)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** instance not found **")

    def help_destory(self):
        print("\n".join([
            "destroy: destroy <class name> <instance id>",
            "         Deletes an instance based on its class name and id"
        ]))

    def do_update(self, line):
        args = check_args(line)
        if args:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                instance_id = f"{args[0]}.{args[1]}"
                if instance_id in storage.all():
                    if len(args) == 2:
                        print("** attributes missing **")
                    elif len(args) == 3:
                        print("** attribute value missing **")
                    else:
                        obj = storage.get(args[0], args[1])
                        if args[2] in type(obj).__dict__:
                            val_type = type(obj.__class__.__dict__[args[2]])
                            setattr(obj, args[2], val_type(args[3]))
                        else:
                            setattr(obj, args[2], args[3])
                else:
                    print("** no instance found **")
            storage.save()

    def help_update(self):
        print("\n".join([
            "update: update <class name> <instance id> <attribute name>\
                <attribute value>",
            "        Updates an instance based on the class name and id by\
                adding or updating attribute"
        ]))

    def do_count(self, line):
        count = 0
        for k, v in storage.all().items():
            if line == k.split(".")[0]:
                count += 1
        print(count)

    def help_count(self):
        print("\n".join([
            "count: count <class name>",
            "       counts the number of instances of a class"
        ]))


if __name__ == "__main__":
    CLI.cmdloop()
