"""
propertyAddress.py: An exercise in working with properties and filtering input.
"""
import re


class StateError(AttributeError):
    pass

class ZipCodeError(AttributeError):
    pass

class Address(object):
    
    def __init__(self, name, streetAddress, city, state, zipCode):
        self._name = name
        self.streetAddress = streetAddress
        self.city = city
        self._state = state
        self._zipCode = zipCode
        
    @property
    def name(self):
        return self._name.title()
    
    @name.setter
    def name(self, value):
        """Raise an exception if attempt to change the name."""
        raise AttributeError("You cannot change the name once set.")
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        """ Filter state input to only take two capital letters."""
        m = re.match(r"^[A-Z]{2}$", value)
        if m:
            self._state = value
        else:
            raise StateError("State must be standard two capital letter abbreviation.")

    @property
    def zipCode(self):
        return self._zipCode
    
    @zipCode.setter
    def zipCode(self, value):
        """Filter the zip code to only be a 5 digit zip."""
        m = re.match(r"^\d{5}$", value)
        if m: 
            self._zipCode = value
        else:
            raise ZipCodeError("Zip must be exactly 5 digits long.")

