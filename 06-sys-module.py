import sys

print(sys.argv[0])

try:
    value = int(sys.argv[1])
except ValueError:
    print('Not Intiger')


# if isinstance(sys.argv[1], int):
#     print(str(sys.argv[1]) + " is suppose to be a number")


#print(int(sys.argv[1]) + int(sys.argv[2]))
