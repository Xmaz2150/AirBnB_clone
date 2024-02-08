#!/usr/bin/python3
""" heart of HBNB """
import cmd
from models import storage
from models.base_model import BaseModel


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

        if not arg:
            print("** class name missing **")
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(obj_data) > 1:
                    new_obj = BaseModel(*obj_data)
                    storage.new(new_obj.to_dict())
                    storage.save()
                else:
                    new_obj = BaseModel()
                    storage.new(new_obj.to_dict())
                    storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""

        if not arg:
            print("** class name missing **")
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(obj_data) != 2:
                    print("** instance id missing **")
                else:
                    objs = storage.get_objs()
                    try:
                        obj_dict = objs["{}.{}".format(obj_data[0], obj_data[1])]
                        new_obj = BaseModel(**obj_dict)
                        print(new_obj.__str__())
                    except KeyError:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        return None

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""

        objs = storage.get_objs()
        objs_strs = []
        def populate_objs_str(objs_strs):
            for key, value in objs.items():
                obj = BaseModel(**value)
                objs_strs.append(obj.__str__())
            
            return objs_strs

        if not arg:
            print(populate_objs_str(objs_strs))
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                print(populate_objs_str(objs_strs))

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        return None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
