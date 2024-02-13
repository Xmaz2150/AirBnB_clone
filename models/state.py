#!/usr/bin/python3
""" user modele """
from models.base_model import BaseModel


class State(BaseModel):
    """ user class """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
