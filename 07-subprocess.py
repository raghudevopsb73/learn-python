import subprocess

proc = subprocess.run(["ls", "-l"], stdout=None)
print(proc)



