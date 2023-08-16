import sys

print(sys.argv[0])

if isinstance(int(sys.argv[1]), int):
    print(str(sys.argv[1]) + " is suppose to be a number")

print(int(sys.argv[1]) + int(sys.argv[2]))
