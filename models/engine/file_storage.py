#!/usr/bin/python3
""" HBNB engine """
import json


class FileStorage():
    """ Storage class for class instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """

        return self.get_objs()

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        storage_objs = self.get_objs()

        key = "{}.{}".format(obj['__class__'], obj['id'])
        storage_objs[key] = obj

        self.objs_set(storage_objs)

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        
        path = self.get_path()
        storage_objs = self.get_objs()

        serialized_objects = {}
        for key, obj in storage_objs.items():
            serialized_objects[key] = obj
        with open(path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        path = self.get_path()
        storage_objs = self.get_objs()

        try:
            with open(path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = globals()[class_name]
                    instance = obj_cls(**value)
                    storage_objs[key] = instance
            self.objs_set(storage_objs)
        except FileNotFoundError:
            pass

    @classmethod
    def get_path(cls):
        """ storage path getter """
        return cls.__file_path

    @classmethod
    def get_objs(cls):
        """ get storage objs """
        return cls.__objects

    @classmethod
    def objs_set(cls, objs):
        """ instance no setter """
        cls.__objects = objs
