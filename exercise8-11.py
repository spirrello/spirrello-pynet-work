#!/usr/bin/env python

"""Stefano Pirrello Week 1 Excercise 8 - 11"""

from ciscoconfparse import CiscoConfParse


#Exercise 8 
#The script should find all of the crypto map entries in 
#the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.
config_obj = CiscoConfParse("cisco_ipsec.txt")

cmaps = config_obj.find_all_children(r"crypto map CRYPTO")

# print type(cmaps)
# print len(cmaps)
print "\n\nExercise 8:"

for cmap in cmaps:
	print cmap
	
#Exercies 9
#Find all of the crypto map entries that are using PFS group2
config_obj = CiscoConfParse("cisco_ipsec.txt")
cmaps = config_obj.find_objects(r"crypto map CRYPTO")
print "\n\nExercise 9:"
#cmaps = config_obj.find_all_children(r"crypto map CRYPTO")
cmaps_list = []
for cmap in cmaps:
	if cmap.re_search_children(r"set\spfs\sgroup2"):
		cmaps_list.append(cmap)

print "Crytomaps using PFS Group 2:"
for i in cmaps_list:
	print i.text

#Exercies 10
#Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
config_obj = CiscoConfParse("cisco_ipsec.txt")
cmaps = config_obj.find_objects(r"crypto map CRYPTO")
print "\n\nExercise 10:"
#cmaps = config_obj.find_all_children(r"crypto map CRYPTO")
cmaps_list = []
for cmap in cmaps:
	if not cmap.re_search_children(r"set\stransform-set\sAES-SHA"):
		cmaps_list.append(cmap)

print "Crytomaps not using AES transform set:"
for i in cmaps_list:
	print i.text

print "\n\n"
