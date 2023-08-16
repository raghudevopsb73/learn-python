import os

name = os.environ['HOME']
print(name)

home1 = os.getenv("HOME1", default=None)
print(home1)
