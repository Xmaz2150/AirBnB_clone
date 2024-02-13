#!/usr/bin/python3
""" user modele """
from models.base_model import BaseModel


class City(BaseModel):
    """ user class """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
