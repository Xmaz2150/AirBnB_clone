#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""

        if arg is None:
            print("** class name missing **")
        return None

    def do_show_(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        return None

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        return None

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        return None

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        return None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
