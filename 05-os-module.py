import os

name = os.environ['HOME']
print(name)

home1 = os.getenv("HOME1", default="/")
print(home1)

with open("/tmp/1.txt", "w") as file:
    file.write("This is an example file.\n")
    file.write("It was created using the os module in Python.")


uptime = os.system('uptime')
type(os.system('uptime'))
