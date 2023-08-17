import subprocess

proc = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(proc)



