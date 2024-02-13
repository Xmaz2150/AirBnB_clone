#!/usr/bin/python3
""" user modele """
from models.base_model import BaseModel


class Review(BaseModel):
    """ user class """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
