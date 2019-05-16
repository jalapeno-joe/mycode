#!/usr/bin/env python3
######## EXPLORE READ ########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across lineboundries (strips out \n)
configlist = configblog.splitlines()
## display lines with no "\n"
print(configlist)

## aleays close your file
configfile.close()

