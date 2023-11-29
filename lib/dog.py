#!/usr/bin/env python3
class Dog:
    approved_breeds = [
    "Mastiff",
    "Chihuahua",
    "Corgi", 
    "Shar Pei", 
    "Beagle", 
    "French Bulldog",
    "Pug", 
    "Pointer"
    ]

    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed


    def name(self):
        return self._name
    
    def set_name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    def breed(self):
        return self._breed

    def set_breed(self, value):
        if value not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value
