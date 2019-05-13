#!/usr/bin/python2.7
# Was in SMN NOC and had to check if customers switches configuration is correct.
# You can either be a masochist and do it manually one-by-one or
# automate the checking hundreds of devices. 
  

import re,os
path = "./network-stuff/"
switches = os.listdir(path)

def checkswitch ( check ):
    if re.match("(.*)(Operating)(.*)", check):
        print ("Current Switch VTP mode: "), check,
    if re.match("(.*)(Domain)(.*)", check):
        print ("Current Switch VTP domain: "), check,
    if re.match("(.*)(rapid-pvst)(.*)", check):
        print ("Spanning-Tree-Mode is rapid-pvst: "), check,

    if re.match("(.*)([0123456789].*.active)(.*)", check):
        print "VLANs ", check[0:14], "\n"
    return 0

for switch in switches:
    file = os.path.join(path, switch)
    text = open(file, "r")
    print(file)
    vlanwritten = False

    for line in text:
        checkswitch(line)
    print("")
