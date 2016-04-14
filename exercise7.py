#!/usr/bin/env python

"""Stefano Pirrello Week 1 Excercise 7"""

import yaml
import json
from pprint import pprint as pp


print "YAML file:"
with open("mylist.yml") as myfile:
	mylist = yaml.load(myfile)
	print yaml.dump(mylist, default_flow_style = False)


print "JSON file:"
with open("mylist.json") as myfile:
	mylist = json.load(myfile)
	#print mylist#, default_flow_style = False)
	pp(mylist)