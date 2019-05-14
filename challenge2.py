#!/usr/bin/env python3

first_list = []
first_dict = {"first_name": "Monty", "last_name": "Python", "actions": ["Scooter", 2, "Moscow"]}

print("In {} {}, Eric Idle rode a {} {} {}".format(first_dict["first_name"], first_dict["last_name"], first_dict["actions"][0], first_dict["actions"][1], first_dict["actions"][2]))

first_list.extend(["horse", "to", "the Holy Grail"])
print(first_list)

first_dict.update({"actions":first_list})
print(first_dict)

print("In {} {}, Eric Idle rode a {} {} {}".format(first_dict["first_name"], first_dict["last_name"], first_dict["actions"][0], first_dict["actions"][1], first_dict["actions"][2]))
