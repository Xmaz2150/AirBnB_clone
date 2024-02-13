#!/usr/bin/python3
""" user modele """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
