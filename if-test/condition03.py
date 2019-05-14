#!/usr/bin/env python3

## Collect input from user
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lower case string
## use the lower method to test if the input value matches expected value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to user.
print("Exiting the script")
