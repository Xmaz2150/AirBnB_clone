#!/usr/bin/python3
""" HBNB engine """
import json


class FileStorage():
    """ Storage class for class instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = globals()[class_name]
                    instance = obj_cls(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
