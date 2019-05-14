#!/usr/bin/env python3

##create a directory
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

##display parts of the directory
print(switch['hostname'])
print(switch['ip'])

##request a 'fake' key
#print(switch[lynx'])

##request a 'fake' key with .get() method
print("First test - .get()")
print(switch.get('lynx'))

print("Second test - .get()")
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

print("Third test - .get()")
print(switch.get('version'))

print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .valuse()")
print(switch.values())

print("Sixth test - .pop()")
switch.pop('version') # removes this key (and valuse) pair
print(switch.keys()) # notice the vluse of the version is gon
print(switch.values()) # notice the valuse 1.2

print("Seventh test - ADD a new valuse")
switch['adminlogin'] = 'karl08'
print(switch.keys())
print(switch.values())

print("Eighth test - ADD a new value")
switch['passwd'] = 'qwerty'
print(switch.keys())
print(switch.values())

