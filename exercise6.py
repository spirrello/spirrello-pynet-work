#!/usr/bin/env python

"""Stefano Pirrello Week 1 Excercise 6"""


import yaml
import json

mylist = ["beach", "abc", {"router" : "asr1001", "core" : "n9516", "firewall":"iptables"}]


with open('mylist.json', 'w') as json_outfile:
	json.dump(mylist, json_outfile)
	json_outfile.close()



with open('mylist.yml', 'w') as yml_outfile:
    yaml_format = yaml.dump(mylist, default_flow_style = False)
    #yaml_format = yaml.dump(mylist, "mylist.yml", default_flow_style = False)
    yml_outfile.write(yaml_format)
    yml_outfile.close()
