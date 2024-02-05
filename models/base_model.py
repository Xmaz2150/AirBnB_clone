#!/usr/bin/python3
""" base class module """
from datetime import datetime
import uuid


class BaseModel:
    """ The class that future classes will inherit """

    def __init__(self, *args, **kwargs):
        """ initialulizes new instance"""
        
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ returns str representation of instance """

        class_name=self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updtes time when instance gets update """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns dict containing key/val pairs of instance """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
