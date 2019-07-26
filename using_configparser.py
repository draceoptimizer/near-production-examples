#!/usr/bin/env python
#
#  This demonstrates the use of a config.ini from within python
#
def to_boolean(in_val):
    return in_val.upper() in ["True","1","Yes"]

import os
from configparser import ConfigParser
print("Start of Demo")
current_dir = os.getcwd()
ini_file_name = "config.ini"
ini_file = os.path.join(current_dir,ini_file_name)
config = ConfigParser()
config.read(ini_file)
print("The config file sections: {}".format(config.sections()))
#  Get some values
print("The Use Double flag: {}".format(config["Processing"]["Use_Double"]))
print(type(config["Processing"]["Use_Double"]))
print(type(to_boolean(config["Processing"]["Use_Double"])))
print(config["Processing"]["Use_Double"])
print("\nTest the False value")
print(to_boolean(config["Processing"]["Test_False"]))
#Note that long strings can be contained in the config file
print("\nNote:  We don't need to include any \" or \' in the command ini line since the whole line is treated as a string.\n")
print("The Weather columns: {}".format(config["Weather"]["columns"]))
print()
#To use them we split and put them in a list
print("\nNOTE:  One single line cleans up the ini input and removes leading and trailing white spaces.\n")
weather_columns = [x.strip() for x in config["Weather"]["columns"].split(",")]
print(weather_columns)
