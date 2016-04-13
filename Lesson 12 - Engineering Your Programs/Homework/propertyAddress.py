"""
propertyAddress.py: An exercise in working with properties and filtering input.
"""
import re
import logging
from optparse import OptionParser
import configparser

config = configparser.RawConfigParser()
config.read("v:/workspace/Python3Homework12/src/propertyAddress.cfg")


logFormat = config.get("log", "format")
# I kept the levels lowercase, if that's alright.
levels = {'debug' : logging.DEBUG,
          'info' : logging.INFO,
          'warning' : logging.WARNING,
          'error' : logging.ERROR,
          'critical' : logging.CRITICAL 
          }

def startLogging(level):
    "Start logging with given filename and level."
    logging.basicConfig(filename = config.get("log", "output"), level = levels[level], format = logFormat)
    
def setLogLevel(level):
    logging.getLogger().setLevel(levels[level])    

class NameError(AttributeError):
    pass

class StateError(AttributeError):
    pass

class ZipCodeError(AttributeError):
    pass

class Address(object):
    
    def __init__(self, name, streetAddress, city, state, zipCode):
        self._name = name
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipCode = zipCode
        logging.info('Creating a new address.')
        
    @property
    def name(self):
        return self._name.title()
    
    @name.setter
    def name(self, value):
        """Raise an exception if attempt to change the name."""
        logging.error("NAME exception")
        raise NameError("You cannot change the name once set.")
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        """ Filter state input to only take two capital letters."""
        m = re.match(config.get("validators", "state"), value)
        if m:
            self._state = value
        else:
            logging.error("STATE exception")
            raise StateError("State must be standard two capital letter abbreviation.")

    @property
    def zipCode(self):
        return self._zipCode
    
    @zipCode.setter
    def zipCode(self, value):
        """Filter the zip code to only be a 5 digit zip."""
        m = re.match(config.get("validators", "zipCode"), value)
        if m: 
            self._zipCode = value
        else:
            logging.error("ZIPCODE exception")
            raise ZipCodeError("Zip must be exactly 5 digits long.")


    
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-l", "--level", dest = "level", action = "store", default = "info", help = "Set the level of the logger: debug, info, warning, error(default), critical")
    parser.add_option("-n", "--name", dest = "name", action = "store", help = "Sets the name value of the Address object.")
    parser.add_option("-a", "--address", dest = "address", action = "store", help = "Sets the streetAddress value of the Address object.")
    parser.add_option("-c", "--city", dest = "city", action = "store", help = "Sets the city value of the Address object.")
    parser.add_option("-s", "--state", dest = "state", action = "store", help = "Sets the state value of the Address object.")
    parser.add_option("-z", "--zipCode", dest = "zipCode", action = "store", help = "Sets the zipCode value of the Address object.")
    options, args = parser.parse_args()
    if options.level in levels.keys():
        startLogging(options.level)
    else:
        parser.error("Please choose a one of the following logging levels:\n debug, info, warning, error(default), or critical")
    if options.name and options.address and options.city and options.state and options.zipCode:
        try:
            newAddress = Address(options.name, options.address, options.city, options.state, options.zipCode)
        except StateError as e:
            parser.error("Option -s requires a valid US state abbreviation. \n" + str(e))
        except ZipCodeError as e:
            parser.error("Option -z requires a valid US zip code. \n" + str(e))
        print(newAddress.name, newAddress.city, newAddress.state)
    else:
        parser.error("Options -n, -a, -c, -s, and -z are all required.")
     