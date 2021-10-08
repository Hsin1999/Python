import os
a=os.path.dirname(__file__)
b=os.path.abspath(__file__)
print(b)
print(os.path.dirname(os.path.dirname(b)))
print(os.path.realpath("/usr/bin/python"))