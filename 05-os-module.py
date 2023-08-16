import os

name = os.environ['HOME']
print(name)

home1 = os.getenv("HOME1", default="/")
print(home1)

with open("/tmp/1.txt", "w") as file:
    file.write("This is an example file.\n")
    file.write("It was created using the os module in Python.")


command = "ls -l"

# Execute the command using os.system()
exit_status = os.system(command)
print(exit_status)

# if exit_status == 0:
#     print("Command executed successfully.")
# else:
#     print("Command execution failed.")
