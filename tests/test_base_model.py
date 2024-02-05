#!/usr/bin/python3
""" test module for Base model class """

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    """ Test class for Base model class"""

    def setUp(self):
        self.base_model = BaseModel()

    #3-4
    def test_initialization(self):
        """ Test the initialization of the BaseModel class  """

        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertEqual(type(self.base_model.id), str)
        self.assertEqual(type(self.base_model.created_at), datetime)
        self.assertEqual(type(self.base_model.updated_at), datetime)

    def test_str_method(self):
        """ Test the string reprs of the BaseModel instance """

        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """ Test the save method to ensure updated_at changes """

        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """ Test the to_dict method to ensure correct dictionary repr """

        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_to_dict_with_attributes(self):
        """ Test to_dict method when instance has additional attrs"""

        self.base_model.name = "Test Model"
        self.base_model.my_number = 42
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel',
            'name': 'Test Model',
            'my_number': 42
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_init_with_dict(self):
        """ Test initializing BaseModel with a dictionary """

        data = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:30:00.000000',
            '__class__': 'BaseModel',
            'custom_attr': 'value'
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_attr, 'value')
        self.assertEqual(instance.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(instance.updated_at, datetime(2022, 1, 2, 12, 30, 0))


if __name__ == '__main__':
    unittest.main()

