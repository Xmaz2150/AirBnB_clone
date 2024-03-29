#!/usr/bin/python3
""" heart of HBNB """
import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """

        if not arg:
            print(self.prompt)
            print("** class name missing **")
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                '''try:
                    objs = storage.get_objs()
                    obj_key = "{}.{}".format(obj_data[0], obj_data[1])
                    objs[obj_key]
                    self.do_update(arg)

                except (IndexError, KeyError):'''
                if len(obj_data) > 1:
                    new_obj = eval(class_name)(*obj_data)
                    storage.new(new_obj)
                    storage.save()
                else:
                    new_obj = eval(class_name)()
                    storage.new(new_obj)
                    storage.save()
                print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        if not arg:
            print("** class name missing **")
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                if len(obj_data) != 2:
                    print("** instance id missing **")
                else:
                    objs = storage.get_objs()
                    try:
                        obj_key = "{}.{}".format(obj_data[0], obj_data[1])
                        obj_dict = objs[obj_key]
                        new_obj = eval(class_name)(**obj_dict)
                        print(new_obj.__str__())
                    except KeyError:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (saves the change into the JSON file)
        """

        if not arg:
            print("** class name missing **")
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                if len(obj_data) != 2:
                    print("** instance id missing **")
                else:
                    objs = storage.get_objs()
                    try:
                        obj_key = "{}.{}".format(obj_data[0], obj_data[1])
                        objs.pop(obj_key)
                        storage.objs_set(objs)
                        storage.save()
                    except KeyError:
                        print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name
        """

        objs = storage.get_objs()
        objs_strs = []

        def populate_objs_str(objs_strs, class_n=""):
            if len(class_n) == 0:
                for key, value in objs.items():
                    obj = eval(key.split('.')[0])(**value)
                    objs_strs.append(obj.__str__())
            else:
                for key, value in objs.items():
                    if key.split('.')[0] == class_n:
                        obj = eval(class_n)(**value)
                        objs_strs.append(obj.__str__())

            return objs_strs

        if not arg:
            print(populate_objs_str(objs_strs, ""))
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                print(populate_objs_str(objs_strs, class_name))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (saves the change into the JSON file)
        """

        if not arg:
            print("** class name missing **")
        else:
            obj_data = arg.split(' ')
            class_name = obj_data[0]

            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                if len(obj_data) < 2:
                    print("** instance id missing **")
                else:
                    objs = storage.get_objs()
                    try:
                        obj_key = "{}.{}".format(obj_data[0], obj_data[1])
                        obj_dict = objs[obj_key]

                        if len(obj_data) < 3:
                            print("** attribute name missing **")
                        elif len(obj_data) < 4:
                            print("** value missing **")
                        else:
                            n_key = obj_data[2]
                            n_val = obj_data[3]

                            obj_dict[n_key] = n_val
                            new_obj = eval(class_name)(**obj_dict)
                            new_obj.updated_at = datetime.now()
                            storage.new(new_obj)
                            storage.save()
                            print(new_obj.id)

                    except KeyError:
                        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
