import sys

print(sys.argv[0])

try:
    value = int(sys.argv[1])
except ValueError:
    print('Not Intiger')
    sys.exit(1)
    

#print(int(sys.argv[1]) + int(sys.argv[2]))
